from googleapiclient.discovery import build
from google.oauth2 import service_account
import datetime
import sqlite3
import pandas as pd

service_account_file = 'astrum-362912-af084cf04b2f.json'
SCOPES = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1G2b1LZMEiIYO1XaB0QrpzFmb-LWtZNNCPusy4xvt6R8'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
# def real_date_get():                        # search date = datetime.datetime(2022, 6, 1)   # 1-year, 2-mounth, 3-day
#     day = datetime.datetime.now()           # left = datetime.datetime(2022, 6, 1)
#     return day                              # right = datetime.datetime(2022, 6, 1)


# ochirib tawiman bowqa faylga otkazganimdan keyn
def rldate():
    day = datetime.datetime.now()
    return f"{day.year}-{day.month}-{day.day}"

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        date = rldate()
        with self.connection:
            return self.cursor.execute("INSERT INTO all_table (User_id, Date) VALUES (?, ?) ", (user_id, date))

    def add_mentor(self, user_id, mentor):
        date = rldate()
        with self.connection:
                return self.cursor.execute("UPDATE all_table SET Mentor = ? WHERE user_id = ? and Date = ? ", ( mentor, user_id, date ) )

    def add_qoniqarsiz(self, user_id, qoniqarsiz):
        date = rldate()
        with self.connection:
            return self.cursor.execute( "UPDATE all_table SET Qoniqarsiz = ? WHERE user_id = ? and Date = ? ", (qoniqarsiz, user_id, date ) )

    def add_qoniqarli(self, user_id, qoniqarli):
        date = rldate()
        with self.connection:
            return self.cursor.execute("UPDATE all_table SET Qoniqarli = ? WHERE user_id = ? and Date = ?", (qoniqarli, user_id, date ) )

    def add_namunali(self, user_id, namunali):
        date = rldate()
        with self.connection:
            return self.cursor.execute("UPDATE all_table SET Namunali = ? WHERE user_id = ? and Date = ?", (namunali, user_id, date ) )

    def user_verification(self, user_id):
        real_date = rldate()
        with self.connection:
            result = self.cursor.execute(f"SELECT Date FROM all_table WHERE User_id = {user_id}").fetchall()
        if result:
            result_len = len(result)
            res_date = result[result_len-1][0]
            if real_date == res_date:
                return True
            else:
                return False
        else:
            return False

    def get_data(self, user):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM all_table WHERE User_id = {user}").fetchall()
        return result

    def get_date_verification(self, user):
        date = rldate()
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM all_table WHERE User_id = {user}").fetchall()
        for x in result:
            date1 = x[1]
            if date1 == date:
                return result

    def add_sheets(self, user):
        data = self.get_date_verification(user=user)
        if data:
            UPDATED_MESSAGES = data[:]
            sheet.values().update( spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=f"data!A2", valueInputOption="USER_ENTERED",
                                  body={'values': UPDATED_MESSAGES } ).execute()



    def admin_add_mentor_ds(self, mentor):
        with self.connection:
            return self.cursor.execute( "INSERT INTO mentors ('Data Science') VALUES (?)", (mentor,) )

    def admin_add_mentor_fl(self, mentor):
        with self.connection:
            return self.cursor.execute( "INSERT INTO mentors ('Full Stack') VALUES (?)", (mentor,) )

    def admin_add_mentor_sf(self, mentor):
        with self.connection:
            return self.cursor.execute( "INSERT INTO mentors ('Software engineer') VALUES (?)", (mentor,) )


    def admin_remov_ds(self, mentor):
        with self.connection:
            return self.cursor.execute( "DELETE FROM mentors WHERE mentors.'Data Science' = (?)", (mentor,) )

    def admin_remov_fl(self, mentor):
        with self.connection:        # DELETE FROM table_name WHERE [condition];
            return self.cursor.execute( "DELETE FROM mentors WHERE mentors.'Full Stack' = (?)", (mentor,) )

    def admin_remov_sf(self, mentor):
        with self.connection:        # DELETE FROM table_name WHERE [condition];
            return self.cursor.execute( "DELETE FROM mentors WHERE mentors.'Software engineer' = (?)", (mentor,) )

    def admin_get_ds(self):
        with self.connection:
            return  self.cursor.execute(f"SELECT mentors.'Data Science' FROM mentors").fetchall()

    def admin_get_fl(self):
        with self.connection:
            return self.cursor.execute(f"SELECT mentors.'Full Stack' FROM mentors").fetchall()

    def admin_get_sf(self):
        with self.connection:
            return self.cursor.execute(f"SELECT mentors.'Software engineer' FROM mentors").fetchall()


    def get_users(self):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM users").fetchall()
            all_list = []
            for x in result:
                all_list.append(x[0])
            return all_list


    def admin_add_user(self, user_id):
        with self.connection:
            user = self.cursor.execute("SELECT * FROM users").fetchall()
            list_id = []
            for x in user:
                if x[0] not in list_id:
                   list_id.append(x[0])
            if user_id not in list_id:
                return self.cursor.execute(f"INSERT INTO users (user) VALUES ({user_id})" )


    def get_data_all(self):
        sql_query = pd.read_sql_query("SELECT * FROM all_table", self.connection)
        return pd.DataFrame(sql_query, columns=['User_id', 'Date', 'Mentor', "Qoniqarsiz", "Qoniqarli", "Namunali"])
