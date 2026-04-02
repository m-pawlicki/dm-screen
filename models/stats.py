from enum import Enum
import math

class StatType(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"

class Stats():

    def __init__(self, str, dex, con, int, wis, cha):
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.str_mod = self.calc_modifier(self.str)
        self.dex_mod = self.calc_modifier(self.dex)
        self.con_mod = self.calc_modifier(self.con)
        self.int_mod = self.calc_modifier(self.int)
        self.wis_mod = self.calc_modifier(self.wis)
        self.cha_mod = self.calc_modifier(self.cha)

    def calc_modifier(self, stat):
        return math.floor((stat - 10)/2)
    
    def to_obj(self):
        obj = {
            StatType.STR: self.str,
            StatType.DEX: self.dex,
            StatType.CON: self.con,
            StatType.INT: self.int,
            StatType.WIS: self.wis,
            StatType.CHA: self.cha
        }
        return obj
    
    def calc_init(self):
        return self.dex_mod
    
    def calc_ac(self):
        return 10 + self.dex_mod
    
    def calc_perception(self):
        return 10 + self.wis_mod
    
    def calc_proficiency(self, level):
        if level >= 1 and level <= 4:
            return 2
        elif level >= 5 and level <= 8:
            return 3
        elif level >= 9 and level <= 12:
            return 4
        elif level >= 13 and level <= 16:
            return 5
        else:
            return 6