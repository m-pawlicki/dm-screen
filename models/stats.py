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