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
                self.ability_score = {StatType.STR: 2, StatType.CHA: 1}
            case RaceType.DWF:
                self.speed = 25
                self.ability_score = {StatType.CON: 2}
            case RaceType.ELF:
                self.speed = 30
                self.ability_score = {StatType.DEX: 2}
            case RaceType.GNO:
                self.speed = 25
                self.ability_score = {StatType.INT: 2}
            case RaceType.HLF:
                self.speed = 25
                self.ability_score = {StatType.DEX: 2}
            case RaceType.HUM:
                self.speed = 30
                self.ability_score = {StatType.STR: 1, StatType.DEX: 1, StatType.CON: 1, StatType.INT: 1, StatType.WIS: 1, StatType.CHA: 1}
            case RaceType.HOR:
                self.speed = 30
                self.ability_score = {StatType.STR: 2, StatType.CON: 1}
            case RaceType.HEL:
                self.speed = 30
                self.ability_score = {StatType.CHA: 2}
                # Need to add choice to increase two abilities by +1
            case RaceType.TFL:
                self.speed = 30
                self.ability_score = {StatType.INT: 1, StatType.CHA: 2}
            case _:
                raise Exception("Ivalid Race")