import config
from sheets import *
import markups as nav
from main import pie, all_bar_all, koment_bar
from aiogram import Bot, types, executor, Dispatcher

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Xush kelibsiz :)', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='ds')
async def ds(message: types.CallbackQuery):
    users_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                           reply_markup=nav.ds_mentors)


@dp.callback_query_handler(text='fs')
async def fs(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                           reply_markup=nav.fs_mentors)


@dp.callback_query_handler(text='se')
async def se(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                           reply_markup=nav.se_mentors)


# =========================================== MENTORS ==================================================================


@dp.callback_query_handler(text='m1')
async def m1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, 'Azodov Sarvar')
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m2')
async def m2(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, "Olloyorov Sirojiddin")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m3')
async def m3(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, 'Rasulov Rahmatulloh')
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m4')
async def m4(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, "Shomurodov Sarvarbek")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m5')
async def m5(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, "Shukurov Jasur")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m6')
async def m6(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, "Azizova Aziza")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m7')
async def m7(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, "Arslanova Nodira")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m8')
async def m8(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, "Alimbayeva Asalbonu")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m9')
async def m9(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_mentor(message.from_user.id, "Orifjonov Abdulaziz")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


# =========================================== COMMENTS =================================================================


# ESTIMATION
@dp.callback_query_handler(text='bad')
async def ds(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "Sababini tanlang",
                           reply_markup=nav.bad_comment)


@dp.callback_query_handler(text='good')
async def ds(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "Sababini tanlang",
                           reply_markup=nav.good_comment)


@dp.callback_query_handler(text='great')
async def ds(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "Sababini tanlang",
                           reply_markup=nav.great_comment)


# COMMENTS
@dp.callback_query_handler(text='bc1')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_qoniqarsiz(message.from_user.id, "Mentor o'z vaqtida ish joyida yo'q")
    add_sheets_qoniqarsiz(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Munosabad qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='bc2')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_qoniqarsiz(message.from_user.id, "Mentor umuman yordam bera olmadi")
    add_sheets_qoniqarsiz(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='bc3')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_qoniqarsiz(message.from_user.id, "Mentor yordam berishdan bosh tortdi")
    add_sheets_qoniqarsiz(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gdc1')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_qoniqarli(message.from_user.id, "Mentor ish joyiga kech keldi")
    add_sheets_qoniqarli(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gdc2')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_qoniqarli(message.from_user.id, "Mentor savolimga toliq jovob berolmadi")
    add_sheets_qoniqarli(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gdc3')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_qoniqarli(message.from_user.id, "Mentor javob berdi ammo muomilasizlik blan")
    add_sheets_qoniqarli(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gtc2')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_namunali(message.from_user.id, "Mentor barcha savoimga javob berdi")
    add_sheets_namunali(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gtc3')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_namunali(message.from_user.id, "Mentor juda ham yaxshi tushuntirdi")
    add_sheets_namunali(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='gtc4')
async def bc1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    add_namunali(message.from_user.id, "Mentor yangicha va qiziqarli usulda taqdimot qilib tushuntirdi")
    add_sheets_namunali(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldirganiz uchun rahmat😊', reply_markup=nav.mainMenu)


# ========================================== ADMIN ===================================================================


@dp.message_handler(commands=['admin'])
async def admin_system(message: types.Message):
    await bot.send_message(message.from_user.id, 'Please enter password')


@dp.callback_query_handler(text='adm_m')
async def admin_system(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    all_bar_all()
    img = open('image/all_plots.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Barcha mentorlarni analitikasi', reply_markup=nav.adm_menu)
    # await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.amentors)


@dp.callback_query_handler(text='adm_ds_m')
async def admin_ds_system(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.adsmentors)


@dp.callback_query_handler(text='adm_fs_m')
async def admin_ds_system(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.afsmentors)


@dp.callback_query_handler(text='adm_se_m')
async def admin_ds_system(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.afsmentors)


@dp.callback_query_handler(text='am1')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Azodov Sarvar")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Azodov Sarvar umumiy analitikasi', reply_markup=nav.viewcoment1)


@dp.callback_query_handler(text='coments_1')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Azodov Sarvar")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Azodov Sarvar qoyilgan kamentariyalar', reply_markup=nav.adm_menu)


@dp.callback_query_handler(text='am2')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Olloyorov Sirojiddin")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Olloyorov Sirojiddin umumiy analitikasi',
                         reply_markup=nav.viewcoment2)


@dp.callback_query_handler(text='coments_2')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Olloyorov Sirojiddin")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Olloyorov Sirojiddin qoyilgan kamentariyalar',
                         reply_markup=nav.adm_menu)


@dp.callback_query_handler(text='am3')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Rasulov Rahmatulloh")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Rasulov Rahmatulloh umumiy analitikasi',
                         reply_markup=nav.viewcoment3)


@dp.callback_query_handler(text='coments_3')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Rasulov Rahmatulloh")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Rasulov Rahmatulloh qoyilgan kamentariyalar',
                         reply_markup=nav.adm_menu)


@dp.callback_query_handler(text='am4')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Shomurodov Sarvarbek")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Shomurodov Sarvarbek umumiy analitikasi',
                         reply_markup=nav.viewcoment4)


@dp.callback_query_handler(text='coments_4')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Shomurodov Sarvarbek")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Shomurodov Sarvarbek qoyilgan kamentariyalar',
                         reply_markup=nav.adm_menu)


@dp.callback_query_handler(text='am5')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Shukurov Jasur")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Shukurov Jasur umumiy analitikasi', reply_markup=nav.viewcoment5)


@dp.callback_query_handler(text='coments_5')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Shukurov Jasur")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Shukurov Jasur qoyilgan kamentariyalar', reply_markup=nav.adm_menu)


@dp.callback_query_handler(text='am6')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Azizova Aziza")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Azizova Aziza umumiy analitikasi', reply_markup=nav.viewcoment6)


@dp.callback_query_handler(text='coments_6')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Azizova Aziza")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Azizova Aziza qoyilgan kamentariyalar', reply_markup=nav.adm_menu)


@dp.callback_query_handler(text='am7')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Arslanova Nodira")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Arslanova Nodira umumiy analitikasi', reply_markup=nav.viewcoment7)


@dp.callback_query_handler(text='coments_7')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Arslanova Nodira")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Arslanova Nodira qoyilgan kamentariyalar',
                         reply_markup=nav.adm_menu)


@dp.callback_query_handler(text='am8')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Alimbayeva Asalbonu")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Alimbayeva Asalbonu umumiy analitikasi',
                         reply_markup=nav.viewcoment8)


@dp.callback_query_handler(text='coments_8')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Alimbayeva Asalbonu")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Alimbayeva Asalbonu qoyilgan kamentariyalar',
                         reply_markup=nav.adm_menu)


@dp.callback_query_handler(text='am9')
async def admin_nodira(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    pie("Orifjonov Abdulaziz")
    img = open('image/mentor_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Orifjonov Abdulaziz umumiy analitikasi',
                         reply_markup=nav.viewcoment9)


@dp.callback_query_handler(text='coments_9')
async def admin_nodira(message: types.CallbackQuery):
    koment_bar("Orifjonov Abdulaziz")
    img = open('image/mentor_barh_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, img, 'Orifjonov Abdulaziz qoyilgan kamentariyalar',
                         reply_markup=nav.adm_menu)


# ==========================================+++++++===================================================================


@dp.message_handler(content_types=['text'])
async def other_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Reaktsiya qoldirish':
            # BLOCK -> USER CHEK
            if user_check(message.from_user.id):
                await bot.send_message(message.from_user.id, 'Siz bir kunda bir marotaba, reaksiya qoldirolisiz :)')
            else:
                add_user(message.from_user.id)
                await bot.send_message(message.from_user.id, 'Assalomu aleykum 😊',
                                       reply_markup=types.ReplyKeyboardRemove())
                await bot.send_message(message.from_user.id, 'Yonalshingizni tanlang', reply_markup=nav.direction)

        if message.text == 'asd':
            await bot.send_message(message.from_user.id, 'Welcome to admin system :)')
            await bot.send_message(message.from_user.id, 'Analysis', reply_markup=nav.adm_analysis)

        if message.text == 'Back':
            await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(message.from_user.id, 'Analysis', reply_markup=nav.adm_analysis)

        if message.text == 'Add Mentor ➕':
            await bot.send_message(message.from_user.id, 'Yonalish tanlang:', reply_markup=nav.admPanel_DFS)


while True:  # A loop to restart the bot if something goes wrong
    try:
        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=True)
    except:
        continue
    break
