import sqlite3
from utils import config

class CharacterDatabase(object):
    def __init__(self, filename=config.DB_NAME):
        self.db_filename = filename
        db = sqlite3.connect(self.db_filename)
        c = db.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS character_base
            (char_id INTEGER PRIMARY KEY, 
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

    def add_character(self, char_name, player_name, job, level, bg, race, alignment, exp, str, dex, con, int, wis, cha):
        try:
            db = sqlite3.connect(self.db_filename)
            c = db.cursor()
            c.execute(
                """INSERT into character_base(
                character_name, 
                player_name, 
                class, 
                level, 
                background, 
                race, 
                alignment, 
                exp, 
                strength, 
                dexterity, 
                constitution, 
                intelligence, 
                wisdom, 
                charisma)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, (char_name, player_name, job, level, bg, race, alignment, exp, str, dex, con, int, wis, cha)
                )
            db.commit()
            c.close()
        except sqlite3.Error as e:
            print(e)

    def update_character(self, char_id, char_name="", player_name="", job="", level="", bg="", race="", alignment="", exp="", str="", dex="", con="", int="", wis="", cha=""):
        db = sqlite3.connect(self.db_filename)
        c = db.cursor()
        c.execute(
            """UPDATE character_base set 
            character_name=?, 
            player_name=?, 
            class=?, 
            level=?, 
            background=?, 
            race=?, 
            alignment=?, 
            exp=?, 
            strength=?, 
            dexterity=?, 
            constitution=?,
            intelligence=?,
            wisdom=?,
            charisma=? 
            WHERE char_id=?
            """, (char_name, player_name, job, level, bg, race, alignment, exp, str, dex, con, int, wis, cha, char_id)
            )
        db.commit()
        c.close()

    def delete_character_by_name(self, char_name):
        db = sqlite3.connect(self.db_filename)
        c = db.cursor()
        c.execute(
            "DELETE from character_base where character_name=?", (char_name,)
            )
        db.commit()
        c.close()

    def delete_character_by_id(self, char_id):
        db = sqlite3.connect(self.db_filename)
        c = db.cursor()
        c.execute(
            "DELETE from character_base where char_id=?", (char_id,)
            )
        db.commit()
        c.close()

    def list_characters(self):
        db = sqlite3.connect(self.db_filename)
        c = db.cursor()
        c.execute(
            "SELECT * from character_base"
            )
        characters = c.fetchall()
        c.close()
        return characters

    def get_character_by_id(self, char_id):
        db = sqlite3.connect(self.db_filename)
        c = db.cursor()
        c.execute(
            "SELECT * from character_base WHERE char_id=?", (char_id,)
            )
        characters = c.fetchall()
        c.close()
        return characters[0]

    def get_character_by_name(self, char_name):
        db = sqlite3.connect(self.db_filename)
        c = db.cursor()
        c.execute(
            "SELECT * from character_base WHERE character_name=?", (char_name,)
            )
        characters = c.fetchall()
        c.close()
        return characters[0]