import sqlite3

from aiogram.dispatcher.filters.state import StatesGroup, State


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO persons_data (user_id) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM persons_data WHERE user_id = ?", (user_id,)).fetchall()
            # print(bool(len(result)))
            return bool(len(result))

    def add_quser(self, user_id, qwasar_user):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET q_user = ? WHERE user_id = ?",
                                       (qwasar_user, user_id,))

    def set_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET Full_name = ? WHERE user_id = ?",
                                       (name, user_id,))

    def set_path(self, user_id, path):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET path = ? WHERE user_id = ?", (path, user_id,))

    def set_t_user(self, user_id, t_user):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET t_user = ? WHERE user_id = ?", (t_user, user_id,))

    def set_phone_number(self, user_id, phone_number):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET phone_number = ? WHERE user_id = ?",
                                       (phone_number, user_id,))

    def set_season(self, user_id, season):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET season = ? WHERE user_id = ?", (season, user_id,))

    def set_stay(self, user_id, stay):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET stay = ? WHERE user_id = ?", (stay, user_id,))

    def set_encode(self, user_id, encode):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET encod = ? WHERE user_id = ?", (encode, user_id,))


    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM persons_data WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET signup = ? WHERE user_id = ?", (signup, user_id,))

    def del_data(self, user_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM persons_data WHERE user_id = ?", (user_id,))

    def serch_by_ph(self, path):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM persons_data WHERE path = ?", (path,)).fetchall()
            res = []
            for row in result:
                # val = str(row[2:])
                res.append(row[0])
                res.append(row[1])
                res.append(row[2])
                res.append(row[3])
                res.append(row[4])
                res.append(row[5])
                res.append(row[6])
                res.append(row[7])
                res.append(row[8])

            return res

    def serch_by_qw(self, srchq):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM persons_data WHERE q_user = ?", (srchq,)).fetchall()
            res = []
            for row in result:
                # val = str(row[2:])
                res.append(row[0])
                res.append(row[1])
                res.append(row[2])
                res.append(row[3])
                res.append(row[4])
                res.append(row[5])
                res.append(row[6])
                res.append(row[7])
                res.append(row[8])

            return res
            # return self.cursor.execute("SELECT * FROM persons_data WHERE q_user = 'yusupov_f'").fetchall()


    def get_encode(self):
        with self.connection:
            return self.cursor.execute("SELECT encod FROM persons_data ").fetchall()


class Registration(StatesGroup):
    qwasar_user = State()
    name = State()
    path = State()
    phone = State()
    season = State()
    stay = State()


class Search(StatesGroup):
    srch_by_qw = State()
    srch_by_ph = State()
