"""Vertretung representation with all properties."""
from dataclasses import dataclass


@dataclass
class Vertretung:
    datum: str = None
    klasse: str = None
    stunde: str = None
    vertreter: str = None
    fach: str = None
    raum: str = None
    text: str = None
    nach: str = None
    

    def __lt__(self, other):
        """Make Vertretung sortable."""
        if self.klasse.zfill(3) < other.klasse.zfill(3):
            return True
        if self.klasse.zfill(3) == other.klasse.zfill(3):
            if self.datum < other.datum:
                return True
            if self.datum == other.datum:
                if self.stunde < other.stunde:
                    return True
        return False


    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(Datum={self.datum}, Klasse={self.klasse}, Stunde={self.stunde}, Vertreter={self.vertreter}, Fach={self.fach}, Raum={self.raum})"
        )