from enum import Enum
from stats import StatType

class RaceType(Enum):
    DRB = "Dragonborn"
    DWF = "Dwarf"
    ELF = "Elf"
    GNO = "Gnome"
    HLF = "Halfling"
    HUM = "Human"
    HOR = "Half-Orc"
    HEL = "Half-Elf"
    TFL = "Tiefling"

class Races():
    def __init__(self, race: RaceType):
        match race:
            case RaceType.DRB:
                self.speed = 30
            case RaceType.DWF:
                self.speed = 25
            case RaceType.ELF:
                self.speed = 30
            case RaceType.GNO:
                self.speed = 25
            case RaceType.HLF:
                self.speed = 25
            case RaceType.HUM:
                self.speed = 30
            case RaceType.HOR:
                self.speed = 30
            case RaceType.HEL:
                self.speed = 30
            case RaceType.TFL:
                self.speed = 30
            case _:
                raise Exception("Ivalid Race")