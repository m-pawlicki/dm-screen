from enum import Enum
from .stats import StatType

class ClassType(Enum):
    BAR = "Barbarian"
    BRD = "Bard"
    CLR = "Cleric"
    DRD = "Druid"
    FTR = "Fighter"
    MNK = "Monk"
    PAL = "Paladin"
    RGR = "Ranger"
    ROG = "Rogue"
    SOR = "Sorcerer"
    WRK = "Warlock"
    WIZ = "Wizard"

class Classes():
    def __init__(self, job: ClassType):
        match job:
            case ClassType.BAR:
                self.hit_die = 12
                self.saving_throw = [StatType.STR, StatType.CON]
            case ClassType.BRD:
                self.hit_die = 8
                self.saving_throw = [StatType.DEX, StatType.CHA]
            case ClassType.CLR:
                self.hit_die = 8
                self.saving_throw = [StatType.WIS, StatType.CHA]
            case ClassType.DRD:
                self.hit_die = 8
                self.saving_throw = [StatType.INT, StatType.WIS]
            case ClassType.FTR:
                self.hit_die = 10
                self.saving_throw = [StatType.STR, StatType.CON]
            case ClassType.MNK:
                self.hit_die = 8
                self.saving_throw = [StatType.STR, StatType.DEX]
            case ClassType.PAL:
                self.hit_die = 10
                self.saving_throw = [StatType.WIS, StatType.CHA]
            case ClassType.RGR:
                self.hit_die = 10
                self.saving_throw = [StatType.STR, StatType.DEX]
            case ClassType.ROG:
                self.hit_die = 8
                self.saving_throw = [StatType.DEX, StatType.INT]
            case ClassType.SOR:
                self.hit_die = 6
                self.saving_throw = [StatType.CON, StatType.CHA]
            case ClassType.WRK:
                self.hit_die = 8
                self.saving_throw = [StatType.WIS, StatType.CHA]
            case ClassType.WIZ:
                self.hit_die = 6
                self.saving_throw = [StatType.INT, StatType.WIS]
            case _:
                raise Exception("Invalid Class")