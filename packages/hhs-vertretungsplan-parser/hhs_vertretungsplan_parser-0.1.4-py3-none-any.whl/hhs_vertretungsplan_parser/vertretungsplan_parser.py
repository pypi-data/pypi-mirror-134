"""Parse responses from Heinrich-Hertz-Schule Vertretungsplan interface."""
from datetime import datetime, timezone
import re
import dateparser
from dateparser.search import search_dates
from typing import Dict, List
from bs4 import BeautifulSoup as bs


import aiohttp

from hhs_vertretungsplan_parser.const import BASE_URL, KEY_ALLE, LOGIN_TEXT, LOGIN_URL

from hhs_vertretungsplan_parser.model.vertretung import Vertretung


class HHSVertretungsplanParser:

    def __init__(self, session: aiohttp.ClientSession, user: str, password: str):
        self.session = session
        self.user = user
        self.password = password
        self.vertretungen = None
        self.status: str = None
    

    async def load_data(self) -> None:
        """Load all data and merge results."""
        overview_page = await self._login()
        self.status = None
        await self._load_vertretungen(overview_page)


    async def _load_from_hhs(self, get_url: str) -> str:
        response = await self.session.request(method="GET", url=get_url)
        response.raise_for_status()
        return await response.text()


    def _is_loggedin(self, body: str) -> bool:
        """Check if we're logged in already."""
        soup = bs(body, 'html.parser')
        result = soup.body.find(string=re.compile(LOGIN_TEXT))
        return result != None


    async def _login(self) -> str:
        """
        Perform login on HHS server.
        First check, if we're logged in already
        If not, do the login
        """
        body = await self._load_from_hhs(LOGIN_URL)

        if self._is_loggedin(body):
            return body

        """Try to login."""
        post_url = LOGIN_URL
        payload = {
            'benutzer': self.user,
            'pass': self.password
        }
        response = await self.session.request(method="POST", url=post_url, data=payload)
        response.raise_for_status()
        body = await response.text()

        if self._is_loggedin(body):
            return body

        """Throw an exception, if this failed."""
        raise AuthenticationException


    def _extract_table_urls(self, overview_page: str) -> List[str]:
        """Extract the urls of the data tables."""
        soup = bs(overview_page, 'html.parser')
        a_list = soup.select('a[target="_blank"]')
        url_list = []
        for a in a_list:
            url_list.append(BASE_URL + a['href'])
        return url_list


    async def _load_vertretungen(self, overview_page: str) -> None:
        """
        Load all data, extract it and arrange it.
        First check, how many tables exist.
        """
        url_list = self._extract_table_urls(overview_page)

        """Now load and extract the table data, store and sort it."""
        self.vertretungen = []
        for url in url_list:
            self.vertretungen.extend(await self._load_and_extract_table(url))

        self.vertretungen.sort()
    

    async def _load_and_extract_table(self, url: str) -> List[Vertretung]:
        """Load and individual table and create a list from it."""
        data = await self._load_from_hhs(url)
        return self._extract_table(data)


    def _extract_table(self, data) -> List[Vertretung]:
        """Extract the data from the table and organize in a list."""
        soup = bs(data, 'html.parser')

        """Check only once for the status."""
        if self.status == None:
            header_text = soup.select_one('table.mon_head td:nth-of-type(3)')
            time_string = header_text.contents[1].contents[8]
            time_string = str(time_string).strip().removeprefix('Stand: ')
            time = dateparser.parse(time_string, date_formats=['%d.%m.%Y %H:%M'], languages=['de'])
            self.status = time.astimezone().isoformat()

        """Now the heavy lifting."""
        date_text = soup.select_one('div.mon_title').string
        date = dateparser.parse(date_text, date_formats=['%-d.%-m.%Y %A'], languages=['de'])

        items = soup.select('tr.list.odd,tr.list.even')
        vertretungen = []

        for item in items:
            entries = item.select('td')
            """Sometimes there is more than one tutor group per table line."""
            tutor_group_string = entries[0].string.strip()
            tutor_group_list = tutor_group_string.split(", ")

            for tutor_group in tutor_group_list:
                vertretung = Vertretung()
                if len(tutor_group) == 0:
                    tutor_group = KEY_ALLE
                elif '.J' in tutor_group:
                    tutor_group = ''.join(filter(str.isdigit, tutor_group)) + KEY_ALLE
                vertretung.datum = date.astimezone().isoformat()
                vertretung.klasse = tutor_group
                vertretung.stunde = entries[1].string.strip()
                vertretung.vertreter = entries[2].string.strip()
                vertretung.fach = entries[3].string.strip()
                vertretung.raum = entries[4].string.strip()
                vertretung.text = entries[5].string.strip()
                vertretung.nach = entries[6].string.strip()
                vertretungen.append(vertretung)
        
        return vertretungen


class AuthenticationException(Exception):
    """Raised when authentication fails."""
    pass