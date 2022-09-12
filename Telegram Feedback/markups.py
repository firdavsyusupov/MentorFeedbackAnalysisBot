from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

ds = InlineKeyboardButton('Data Science', callback_data='ds')
fs = InlineKeyboardButton('Full Stack', callback_data='fs')
se = InlineKeyboardButton('SoftWere Engineer', callback_data='se')

btn_start = KeyboardButton('Reaktsiya qoldirish')
btn_ds = KeyboardButton('Data Science')
btn_fs = KeyboardButton('Full Stack')
btn_se = KeyboardButton('SoftWere Engineer')

bad = InlineKeyboardButton('qoniqarsiz☹️', callback_data='bad')
good = InlineKeyboardButton('qoniqarli😐', callback_data='good')
great = InlineKeyboardButton('namunali😊', callback_data='great')

bad_comment_1 = InlineKeyboardButton("Mentor o'z vaqtida ish joyida yo'q", callback_data='bc1')
bad_comment_2 = InlineKeyboardButton("Mentor umuman yordam bera olmadi", callback_data='bc2')
bad_comment_3 = InlineKeyboardButton("Mentor yordam berishdan bosh tortdi", callback_data='bc3')

good_comment_1 = InlineKeyboardButton("Mentor ish joyiga kech keldi", callback_data='gdc1')
good_comment_2 = InlineKeyboardButton("Mentor savolimga toliq jovob berolmadi", callback_data='gdc2')
good_comment_3 = InlineKeyboardButton("Mentor javob berdi ammo muomilasizlik blan", callback_data='gdc3')

great_comment_1 = InlineKeyboardButton("Mentor o'z vaqtida ish joyida", callback_data='gtc1')
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


direction = InlineKeyboardMarkup(row_width=1)
direction.insert(ds)
direction.insert(fs)
direction.insert(se)

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True)
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
great_comment.insert(great_comment_1)
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