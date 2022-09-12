import sqlite3
import datetime
from aiogram.dispatcher.filters.state import StatesGroup, State


class Databasee:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))

    # def get_direction(self, user_id, direction):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT direction FROM users WHERE user_id = ?", (user_id,)).fetchall()
    #         for row in result:
    #             signup = str(row[0])
    #         return signup
    #
    # def set_direction(self, user_id, direction):
    #     with self.connection:
    #         return self.cursor.execute("UPDATE users SET direction = ? WHERE user_id = ?", (direction, user_id,))

    def get_directions(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT direction FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_directions(self, user_id, direction):
        with self.connection:
            return self.cursor.execute("UPDATE users SET direction = ? WHERE user_id = ?", (direction, user_id,))

    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?", (signup, user_id,))

    #=================================================================================================================
    def add_users(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'mentors' ('user_id') VALUES (?)", (user_id,))

    def date_time(self, user_id, date):
        # day = datetime.date.today().day
        # mounth = datetime.date.today().month
        # year = datetime.date.today().year
        # real_date = f"{day}/{mounth}/{year}"
        with self.connection:
            return self.cursor.execute("UPDATE mentors SET 'date' = ? WHERE 'user_id'=? ", (date, user_id,))

    def add_mentor(self, user_id, mentor):
        with self.connection:
            return self.cursor.execute("UPDATE mentors SET mentorlar = ? WHERE user_id=? ", (mentor, user_id,))

    def add_qoniqarsiz(self, user_id, qoniqarsiz):
        with self.connection:
            return self.cursor.execute("UPDATE mentors SET qoniqarsiz = ? WHERE user_id=? ", (qoniqarsiz, user_id,))

    def add_qoniqarli(self, user_id, qoniqarli):
        with self.connection:
            return self.cursor.execute("UPDATE mentors SET qoniqarli = ? WHERE user_id=? ", (qoniqarli, user_id,))

    def add_namunali(self, user_id, namunali):
        with self.connection:
            return self.cursor.execute("UPDATE mentors SET namunali = ? WHERE user_id=? ", (namunali, user_id,))



