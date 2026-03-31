from enum import Enum
import math, json

class StatNames(Enum):
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

    def calc_modifier(self, stat):
        return math.floor((stat - 10)/2)
    
    def to_json(self):
        obj = {
            StatNames.STR: self.str,
            StatNames.DEX: self.dex,
            StatNames.CON: self.con,
            StatNames.INT: self.int,
            StatNames.WIS: self.wis,
            StatNames.CHA: self.cha
        }
        return json.dumps(obj)