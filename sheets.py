import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account
import datetime

service_account_file = 'astrum-362912-af084cf04b2f.json'
SCOPES = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1G2b1LZMEiIYO1XaB0QrpzFmb-LWtZNNCPusy4xvt6R8'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()


def rldate():
    day = datetime.datetime.now()
    return f"{day.year}-{day.month}-{day.day}"


row_num = 0
DATA = pd.DataFrame(columns=["User_id", "Date", "Mentor", "Qoniqarsiz", "Qoniqarli", "Namunali"], index=range(0, 10))


def user_check(user):
    x = DATA[DATA["User_id"] == user].index
    y = DATA["Date"][x].values
    z = DATA["Mentor"][x].values
    day = datetime.datetime.now()
    day = f"{day.year}-{day.month}-{day.day}"
    if day in y:
        return True
    else:
        return False


def add_user(user):
    DATA.User_id[row_num] = user
    day = datetime.datetime.now()
    day = f"{day.year}-{day.month}-{day.day}"
    DATA.Date[row_num] = day
    globals()['row_num'] += 1


def add_mentor(user, mentor_name):
    x = DATA[DATA["User_id"] == user].index
    DATA["Mentor"][x] = mentor_name


def add_qoniqarsiz(user, koment):
    x = DATA[DATA["User_id"] == user].index
    DATA["Qoniqarsiz"][x] = koment


def add_qoniqarli(user, koment):
    x = DATA[DATA["User_id"] == user].index
    DATA["Qoniqarli"][x] = koment


def add_namunali(user, koment):
    x = DATA[DATA["User_id"] == user].index
    DATA["Namunali"][x] = koment


global frame_num
frame_num = 0

global sheets_num
sheets_num = 2


def add_sheets_qoniqarsiz(user):
    rdate = rldate()
    userid = DATA[DATA['User_id'] == user]
    frame = userid[userid['Date'] == rdate]
    # str(frame['User_id'].values)[1:-1]
    UPDATED_MESSAGES = [
        [frame['User_id'].values[0], frame['Date'].values[0], frame['Mentor'].values[0], frame['Qoniqarsiz'].values[0],
         None,
         None]]  # DATA.iloc[frame_num].values[0], DATA.iloc[frame_num].values[1], DATA.iloc[frame_num].values[2], DATA.iloc[frame_num].values[3],

    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range=f"data!A{sheets_num}", valueInputOption="USER_ENTERED",
                          body={'values': UPDATED_MESSAGES}).execute()
    globals()["sheets_num"] += 1
    globals()["frame_num"] += 1


def add_sheets_qoniqarli(user):
    rdate = rldate()
    userid = DATA[DATA['User_id'] == user]
    frame = userid[userid['Date'] == rdate]
    UPDATED_MESSAGES = [
        [frame['User_id'].values[0], frame['Date'].values[0], frame['Mentor'].values[0],
         None, frame['Qoniqarli'].values[0], None]]
    # UPDATED_MESSAGES = [ [DATA.iloc[frame_num].values[0], DATA.iloc[frame_num].values[1], DATA.iloc[frame_num].values[2], None, DATA.iloc[frame_num].values[3]]]
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range=f"data!A{sheets_num}", valueInputOption="USER_ENTERED",
                          body={'values': UPDATED_MESSAGES}).execute()
    globals()["sheets_num"] += 1
    globals()["frame_num"] += 1


def add_sheets_namunali(user):
    rdate = rldate()
    userid = DATA[DATA['User_id'] == user]
    frame = userid[userid['Date'] == rdate]

    UPDATED_MESSAGES = [[frame['User_id'].values[0], frame['Date'].values[0], frame['Mentor'].values[0],
                         None, None, frame['Namunali'].values[0]]]

    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range=f"data!A{sheets_num}", valueInputOption="USER_ENTERED",
                          body={'values': UPDATED_MESSAGES}).execute()
    globals()["sheets_num"] += 1
    globals()["frame_num"] += 1
