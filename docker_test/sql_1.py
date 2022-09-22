import sqlite3
import datetime


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

    # =================================================================================================================

    def add_users(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'mentorss' ('user_id') VALUES (?)", (user_id,))

    def date_time(self, user_id, date):
        with self.connection:
            return self.cursor.execute("UPDATE mentorss SET datetimes = ? WHERE 'user_id'=? ", (date, user_id,))

    def add_mentor(self, user_id, mentor):
        with self.connection:
            return self.cursor.execute("UPDATE mentorss SET mentorlar = ? WHERE user_id=? ", (mentor, user_id,))

    def add_qoniqarsiz(self, user_id, qoniqarsiz):
        with self.connection:
            return self.cursor.execute("UPDATE mentorss SET qoniqarsiz = ? WHERE user_id=? ", (qoniqarsiz, user_id,))

    def add_qoniqarli(self, user_id, qoniqarli):
        with self.connection:
            return self.cursor.execute("UPDATE mentorss SET qoniqarli = ? WHERE user_id=? ", (qoniqarli, user_id,))

    def add_namunali(self, user_id, namunali):
        with self.connection:
            return self.cursor.execute("UPDATE mentorss SET namunali = ? WHERE user_id=? ", (namunali, user_id,))

    def add_limit(self, user_id, limit):
        with self.connection:
            return self.cursor.execute("UPDATE mentorss SET limited = ? WHERE user_id = ?", (limit, user_id))

    def get_limit(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT limited FROM mentorss WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def add_lim(self, user_id, limit):
        with self.connection:
            result = self.cursor.execute("[delete] or [update][set limited = 'val'] from < mentorss > where < user_id", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup



    # def date_time(self, user_id, date):
    #     with self.connection:
    #         return self.cursor.execute(f"INSERT INTO mentorss VALUES ({date}) WHERE mentorss.user_id = user_id ")
    #  # cursor.execute(f"INSERT INTO {today} VALUES ('{name}', '{product_name}', '{price}', '{phone}', '{description}', '{product_url}')")
    # def add_mentor(sself, user_id, mentor)s:
    #     with self.connection:
    #         return self.cursor.execute(f"INSERT INTO mentorss VALUES ({mentor}s)  ")
    #
    # def add_qoniqarsiz(self, user_id, qoniqarsiz):
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO mentorss SET qoniqarsiz = ? WHERE user_id=? ", (qoniqarsiz, user_id,))
    #
    # def add_qoniqarli(self, user_id, qoniqarli):
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO mentorss SET qoniqarli = ? WHERE user_id=? ", (qoniqarli, user_id,))
    #
    # def add_namunali(self, user_id, namunali):
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO mentorss SET namunali = ? WHERE user_id=? ", (namunali, user_id,))




# connection = sqlite3.connect('db_astrum (3).db')
# cursor = connection.cursor()
# db = Databasee('db_astrum (3).db')
# def get_database():
#     df = pd.read_sql(
#         'SELECT [ID]\
#         ,[user_id]\
#         ,[datatimes]\
#         ,[mentorlsar]\
#         ,[qoniqarsiz]\
#         ,[qoniqarli]\
#         ,[namunali]\
#     FROM mentorss',
#     db,
#         index_col='ID')
#     print(df)
# get_database()
