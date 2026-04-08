import sqlite3
from utils import config

class CharacterDatabase(object):
    def __init__(self, filename=config.DB_NAME):
        self.db_filename = filename
        db = sqlite3.connect(self.db_filename)
        c = db.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS character_base
            (id INTEGER PRIMARY KEY, 
            character_name TEXT, 
            player_name TEXT,
            class TEXT,
            level INTEGER,
            background TEXT,
            race TEXT,
            alignment TEXT,
            exp INTEGER,
            strength INTEGER,
            dexterity INTEGER,
            constitution INTEGER,
            intelligence INTEGER,
            wisdom INTEGER,
            charisma INTEGER
            )"""
        )
        db.commit()
        c.close()

    def add_character(self):
        pass

    def update_character(self):
        pass

    def delete_character(self):
        pass

    def list_characters(self):
        pass

    def get_character(self):
        pass