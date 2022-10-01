from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

ds = InlineKeyboardButton('Data Science', callback_data='ds')
fs = InlineKeyboardButton('Full Stack', callback_data='fs')
se = InlineKeyboardButton('SoftWere Engineer', callback_data='se')

btn_start = KeyboardButton('Reaktsiya qoldirish')
btn_ds = KeyboardButton('Data Science')
btn_fs = KeyboardButton('Full Stack')
btn_se = KeyboardButton('Software Engineer')

bad = InlineKeyboardButton('qoniqarsiz☹️', callback_data='bad')
good = InlineKeyboardButton('qoniqarli😐', callback_data='good')
great = InlineKeyboardButton('namunali😊', callback_data='great')

bad_comment_1 = InlineKeyboardButton("Mentor o'z vaqtida ish joyida yo'q", callback_data='bc1')
bad_comment_2 = InlineKeyboardButton("Mentor umuman yordam bera olmadi", callback_data='bc2')
bad_comment_3 = InlineKeyboardButton("Mentor yordam berishdan bosh tortdi", callback_data='bc3')

good_comment_1 = InlineKeyboardButton("Mentor ish joyiga kech keldi", callback_data='gdc1')
good_comment_2 = InlineKeyboardButton("Mentor savolimga toliq jovob berolmadi", callback_data='gdc2')
good_comment_3 = InlineKeyboardButton("Mentor javob berdi ammo muomilasizlik blan", callback_data='gdc3')

# great_comment_1 = InlineKeyboardButton("Mentor o'z vaqtida ish joyida", callback_data='gtc1')
great_comment_2 = InlineKeyboardButton("Mentor barcha savoimga javob berdi", callback_data='gtc2')
great_comment_3 = InlineKeyboardButton("Mentor juda ham yaxshi tushuntirdi", callback_data='gtc3')
great_comment_4 = InlineKeyboardButton("Mentor yangicha va qiziqarli usulda taqdimot qilib tushuntirdi", callback_data='gtc4')

mentor_se_1 = InlineKeyboardButton("Azodov Sarvar", callback_data='m1')
mentor_se_2 = InlineKeyboardButton("Olloyorov Sirojiddin", callback_data='m2')
mentor_fs_3 = InlineKeyboardButton("Rasulov Rahmatulloh", callback_data='m3')
mentor_fs_4 = InlineKeyboardButton("Shomurodov Sarvarbek", callback_data='m4')
mentor_fs_5 = InlineKeyboardButton("Shukurov Jasur", callback_data='m5')
mentor_fs_6 = InlineKeyboardButton("Azizova Aziza", callback_data='m6')
mentor_ds_7 = InlineKeyboardButton("Arslanova Nodira", callback_data='m7')
mentor_ds_8 = InlineKeyboardButton("Alimbayeva Asalbonu", callback_data='m8')
mentor_ds_9 = InlineKeyboardButton("Orifjonov Abdulaziz", callback_data='m9')

#                   ________________________________________
# ================================= ADMIN ===========================================
#                   ________________________________________

mentor_ase_1 = InlineKeyboardButton("Azodov Sarvar", callback_data='am1')
mentor_ase_2 = InlineKeyboardButton("Olloyorov Sirojiddin", callback_data='am2')
mentor_afs_3 = InlineKeyboardButton("Rasulov Rahmatulloh", callback_data='am3')
mentor_afs_4 = InlineKeyboardButton("Shomurodov Sarvarbek", callback_data='am4')
mentor_afs_5 = InlineKeyboardButton("Shukurov Jasur", callback_data='am5')
mentor_afs_6 = InlineKeyboardButton("Azizova Aziza", callback_data='am6')
mentor_ads_7 = InlineKeyboardButton("Arslanova Nodira", callback_data='am7')
mentor_ads_8 = InlineKeyboardButton("Alimbayeva Asalbonu", callback_data='am8')
mentor_ads_9 = InlineKeyboardButton("Orifjonov Abdulaziz", callback_data='am9')


mentor_coment1 = InlineKeyboardButton("Komentariyalari", callback_data='coments_1')
mentor_coment2 = InlineKeyboardButton("Komentariyalari", callback_data='coments_2')
mentor_coment3 = InlineKeyboardButton("Komentariyalari", callback_data='coments_3')
mentor_coment4 = InlineKeyboardButton("Komentariyalari", callback_data='coments_4')
mentor_coment5 = InlineKeyboardButton("Komentariyalari", callback_data='coments_5')
mentor_coment6 = InlineKeyboardButton("Komentariyalari", callback_data='coments_6')
mentor_coment7 = InlineKeyboardButton("Komentariyalari", callback_data='coments_7')
mentor_coment8 = InlineKeyboardButton("Komentariyalari", callback_data='coments_8')
mentor_coment9 = InlineKeyboardButton("Komentariyalari", callback_data='coments_9')

viewcoment1 = InlineKeyboardMarkup(row_width=1)
viewcoment1.insert(mentor_coment1)
viewcoment2 = InlineKeyboardMarkup(row_width=1)
viewcoment2.insert(mentor_coment2)
viewcoment3 = InlineKeyboardMarkup(row_width=1)
viewcoment3.insert(mentor_coment3)
viewcoment4 = InlineKeyboardMarkup(row_width=1)
viewcoment4.insert(mentor_coment4)
viewcoment5 = InlineKeyboardMarkup(row_width=1)
viewcoment5.insert(mentor_coment5)
viewcoment6 = InlineKeyboardMarkup(row_width=1)
viewcoment6.insert(mentor_coment6)
viewcoment7 = InlineKeyboardMarkup(row_width=1)
viewcoment7.insert(mentor_coment7)
viewcoment8 = InlineKeyboardMarkup(row_width=1)
viewcoment8.insert(mentor_coment8)
viewcoment9 = InlineKeyboardMarkup(row_width=1)
viewcoment9.insert(mentor_coment9)

adm_mentors = InlineKeyboardButton('Barcha mentorlar', callback_data='adm_m')
adm_ds_mentors = InlineKeyboardButton('Data Science', callback_data='adm_ds_m')
adm_fs_mentors = InlineKeyboardButton('Full Stack', callback_data='adm_fs_m')
adm_se_mentors = InlineKeyboardButton('Software Engineer', callback_data='adm_se_m')

amentors = InlineKeyboardMarkup(row_width=1)
amentors.insert(mentor_ase_1)
amentors.insert(mentor_ase_2)
amentors.insert(mentor_afs_3)
amentors.insert(mentor_afs_4)
amentors.insert(mentor_afs_5)
amentors.insert(mentor_afs_6)
amentors.insert(mentor_ads_7)
amentors.insert(mentor_ads_8)
amentors.insert(mentor_ads_9)


adsmentors = InlineKeyboardMarkup(row_width=1)
adsmentors.insert(mentor_ads_7)
adsmentors.insert(mentor_ads_8)
adsmentors.insert(mentor_ads_9)

afsmentors = InlineKeyboardMarkup(row_width=1)
afsmentors.insert(mentor_afs_3)
afsmentors.insert(mentor_afs_4)
afsmentors.insert(mentor_afs_5)
afsmentors.insert(mentor_afs_6)

asementors = InlineKeyboardMarkup(row_width=1)
asementors.insert(mentor_ase_1)
asementors.insert(mentor_ase_2)

adm_analysis = InlineKeyboardMarkup(row_width=1)
adm_analysis.insert(adm_mentors)
adm_analysis.insert(adm_ds_mentors)
adm_analysis.insert(adm_fs_mentors)
adm_analysis.insert(adm_se_mentors)

btn_admBackMenu = KeyboardButton('Back')
btn_week = KeyboardButton('Hafta')
btn_day = KeyboardButton('Kun')

btn_adminMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btn_adminMenu.add(btn_week)
btn_adminMenu.add(btn_day)

adm_menu = ReplyKeyboardMarkup(resize_keyboard=True)
adm_menu.add(btn_admBackMenu)

# ADM PANEL
btn_addmentor = KeyboardButton('Add Mentor ➕')
btn_admPanel = ReplyKeyboardMarkup(resize_keyboard=True)
btn_admPanel.add(btn_addmentor)

# ADM LIST
admPanel_ds = InlineKeyboardButton('Data Science', callback_data='ds_panel')
admPanel_fs = InlineKeyboardButton('Full Stack', callback_data='fs_panel')
admPanel_se = InlineKeyboardButton('Software Engineer', callback_data='se_panel')

admPanel_DFS = InlineKeyboardMarkup(row_width=1)
admPanel_DFS.insert(admPanel_ds)
admPanel_DFS.insert(admPanel_fs)
admPanel_DFS.insert(admPanel_se)

# ===================================================================================

direction = InlineKeyboardMarkup(row_width=1)
direction.insert(ds)
direction.insert(fs)
direction.insert(se)

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btn_start)

directionMenu = ReplyKeyboardMarkup(resize_keyboard=True)
directionMenu.add(btn_ds)
directionMenu.add(btn_fs)
directionMenu.add(btn_se)

estimation = InlineKeyboardMarkup(row_width=1)
estimation.insert(bad)
estimation.insert(good)
estimation.insert(great)

bad_comment = InlineKeyboardMarkup(row_width=1)
bad_comment.insert(bad_comment_1)
bad_comment.insert(bad_comment_2)
bad_comment.insert(bad_comment_3)

good_comment = InlineKeyboardMarkup(row_width=1)
good_comment.insert(good_comment_1)
good_comment.insert(good_comment_2)
good_comment.insert(good_comment_3)

great_comment = InlineKeyboardMarkup(row_width=1)
#great_comment.insert(great_comment_1)
great_comment.insert(great_comment_2)
great_comment.insert(great_comment_3)
great_comment.insert(great_comment_4)

se_mentors = InlineKeyboardMarkup(row_width=1)
se_mentors.insert(mentor_se_1)
se_mentors.insert(mentor_se_2)

fs_mentors = InlineKeyboardMarkup(row_width=1)
fs_mentors.insert(mentor_fs_3)
fs_mentors.insert(mentor_fs_4)
fs_mentors.insert(mentor_fs_5)
fs_mentors.insert(mentor_fs_6)

ds_mentors = InlineKeyboardMarkup(row_width=1)
ds_mentors.insert(mentor_ds_7)
ds_mentors.insert(mentor_ds_8)
ds_mentors.insert(mentor_ds_9)

mentors = InlineKeyboardMarkup(row_width=1)
mentors.insert(mentor_se_1)
mentors.insert(mentor_se_2)
mentors.insert(mentor_fs_3)
mentors.insert(mentor_fs_4)
mentors.insert(mentor_fs_5)
mentors.insert(mentor_fs_6)
mentors.insert(mentor_ds_7)
mentors.insert(mentor_ds_8)
mentors.insert(mentor_ds_9)