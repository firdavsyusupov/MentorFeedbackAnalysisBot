from aiogram import Bot, Dispatcher, executor, types
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import face_recognition
import glob, os, os.path
import numpy as np
import asyncio

import markups as nav
from main_s import Database
from main_s import Registration
from main_s import Search

API_TOKEN = '5466643678:AAH9fnTyC0CAwSktV3tZUgalUam006vPfCs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

db = Database('data.db')

admin_id = '1784921501'  # Abdulaziz
admin_id_1 = "5161784802"  # Abubakr


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        db.set_t_user(message.from_user.id, message.from_user.username)
        await bot.send_message(message.from_user.id, "Siz Registrasiyani boshladingiz\nIsmingizni kiriting")
        await Registration.name.set()
    else:
        await bot.send_message(message.from_user.id, "Siz registrasiyadan otib bolgansiz!", reply_markup=nav.mainMenu)


@dp.message_handler(state=Registration.name)
async def state_name(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(name=answer)
    await bot.send_message(message.from_user.id, "Qwasar nikingizni kiriting")
    await Registration.qwasar_user.set()


@dp.message_handler(state=Registration.qwasar_user)
async def state_qwname(message: types.Message, state: FSMContext):
    answer = message.text.lower()

    await state.update_data(qwasar_user=answer)
    await bot.send_message(message.from_user.id, "Telefon nomeringizni kiriting")
    await Registration.phone.set()


@dp.message_handler(state=Registration.phone)
async def state_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(phone=answer)
    await bot.send_message(message.from_user.id, "Qaysi seasonda o'qiysiz?")
    await Registration.season.set()


@dp.message_handler(state=Registration.season)
async def state_season(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(season=answer)
    await bot.send_message(message.from_user.id, "Qaysi xonada otirasiz?")
    await Registration.stay.set()


@dp.message_handler(state=Registration.stay)
async def state_stay(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(stay=answer)
    await bot.send_message(message.from_user.id, "Rasimingizni tashlang")
    await Registration.path.set()


@dp.message_handler(state=Registration.path, content_types=['photo'])
async def state_path(message: types.Message, state: FSMContext):
    if db.get_signup(message.from_user.id) == 'setnickname':
        answer = message.text
        await message.photo[-1].download(destination_dir='/Users/student/PycharmProjects/Face_bot/image_known')
        file_photo = await bot.get_file(message.photo[-1].file_id)

        await state.update_data(path=answer)
        data = await state.get_data()
        name = data.get('name')
        q_user = data.get('qwasar_user')
        phone = data.get('phone')
        season = data.get('season')
        stay = data.get('stay')
        path = file_photo['file_path']
        load_im = face_recognition.load_image_file("image_known/" + path)
        encode = face_recognition.face_encodings(load_im)[0]

        print(name)
        print(q_user)
        print(phone)
        print(season)
        print(stay)
        print(path)
        try:
            db.set_name(message.from_user.id, name)
            db.add_quser(message.from_user.id, q_user)
            db.set_phone_number(message.from_user.id, phone)
            db.set_season(message.from_user.id, season)
            db.set_stay(message.from_user.id, stay)
            db.set_path(message.from_user.id, path)
            db.set_encode(message.from_user.id, encode)

            db.set_signup(message.from_user.id, "done")
            await bot.send_message(message.from_user.id, "Registrasiya muvafiqiyatli otti!", reply_markup=nav.mainMenu)
            await state.finish()
        except:
            db.del_data(message.from_user.id)
            await bot.send_message(message.from_user.id, "Bu Qwasar username registrasiyadan o'tgan")


@dp.message_handler()
async def bot_mesaage(message: types.Message):
    if message.text == "Qwasar user boyicha qidirish":
        await bot.send_message(message.from_user.id, "Qwasar user yozing")
        await Search.srch_by_qw.set()
    if message.text == "Rasm bo'yicha qidirish":
        await bot.send_message(message.from_user.id, "Rasm tashlang")

        await Search.srch_by_ph.set()


@dp.message_handler(state=Search.srch_by_qw)
async def bot_mesaage(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    await state.update_data(sqw=answer)
    data = await state.get_data()
    srchqw = data.get('sqw')
    # print(db.serch_by_qw(srchqw)[3])
    try:

        name = db.serch_by_qw(srchqw)[2]
        q_user = db.serch_by_qw(srchqw)[1]
        photo = open("image_known/" + db.serch_by_qw(srchqw)[3], "rb")
        t_user = db.serch_by_qw(srchqw)[4]
        phone = db.serch_by_qw(srchqw)[5]
        season = db.serch_by_qw(srchqw)[6]
        stay = db.serch_by_qw(srchqw)[7]

        await bot.send_photo(message.from_user.id, photo,
                             f"Ismi: {name}\nTelegram user name: @{t_user}\nTelefon raqami: {phone}\nSeason: {season}\nOtiradigan xonasi: {stay}")

    except:

        await bot.send_message(message.from_user.id, "Bu odam registrasiyadan o'tmagan")

    await state.finish()


@dp.message_handler(state=Search.srch_by_ph, content_types=['photo'])
async def bot_srch(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(sqwph=answer)
    data = await state.get_data()
    await message.photo[-1].download(destination_dir='/Users/student/PycharmProjects/Face_bot/image_unknown')

    file_photo = await bot.get_file(message.photo[-1].file_id)
    path = file_photo['file_path']
    # print(path)
    # sqwph = data.get('sqwph')
    # print(file_photo)

    # get the path/directory
    folder_dir = "/Users/student/PycharmProjects/Face_bot/image_known/photos"
    a = []
    for images in os.listdir(folder_dir):
        a.append(images)

    # try:
    data = ''
    for i in range(len(a)):
        en_ims = np.array(db.get_encode())
        for en_im in en_ims:

            # print(i)
            # known = face_recognition.load_image_file("image_known/photos/" + a[i])
            unknown = face_recognition.load_image_file("image_unknown/" + path)
            image_2_en = face_recognition.face_encodings(unknown)[0]
            # image_1_en = face_recognition.face_encodings(known)[0]

            res = face_recognition.compare_faces([image_2_en], en_im, tolerance=0.5)
            print(res)
            print(path)


            # for b in range(len(a)):
            if res == [True]:
                data +="1"
                # print("One")
            if res == [False]:
                data += "0"
                # print("Zero")

    if '1' in data:
        b = data.index('1')
        name = db.serch_by_ph("photos/" + a[b])[2]
        q_user = db.serch_by_ph("photos/" + a[b])[1]
        photo = db.serch_by_ph("photos/" + a[b])[3]
        t_user = db.serch_by_ph("photos/" + a[b])[4]
        phone = db.serch_by_ph("photos/" + a[b])[5]
        season = db.serch_by_ph("photos/" + a[b])[6]
        stay = db.serch_by_ph("photos/" + a[b])[7]
        # print(name)
        await bot.send_message(message.from_user.id,
                               f"Ismi: {name}\nTelegram user name: @{t_user}\nTelefon raqami: {phone}\nSeason: {season}\nOtiradigan xonasi: {stay}")
        mydir = "/Users/student/PycharmProjects/Face_bot/image_unknown/photos"
        filelist = glob.glob(os.path.join(mydir, "*.jpg"))
        for f in filelist:
            os.remove(f)
    elif '0' in data:
        await bot.send_message(message.from_user.id,
                                               "Bu odam registrasiyadan o'tmagan, yoki yuborgan rasimingiz tiniq emas(yuz qismi toliq korinishi kerak)")
        mydir = "/Users/student/PycharmProjects/Face_bot/image_unknown/photos"
        filelist = glob.glob(os.path.join(mydir, "*.jpg"))
        for f in filelist:
            os.remove(f)




    # except:
    #     await bot.send_message(message.from_user.id,
    #                               "Bu odam registrasiyadan o'tmagan, yoki yuborgan rasimingiz tiniq emas(yuz qismi toliq korinishi kerak)")
    #     mydir = "/Users/student/PycharmProjects/Face_bot/image_unknown/photos"
    #     filelist = glob.glob(os.path.join(mydir, "*.jpg"))
    #     for f in filelist:
    #         os.remove(f)










    # for i in range(len(a)):
    #     p = 0
    #
    #     try:
    #
    #
    #         known = face_recognition.load_image_file("image_known/photos/" + a[i])
    #         unknown = face_recognition.load_image_file("image_unknown/" + path)
    #         image_2_en = face_recognition.face_encodings(unknown)[0]
    #         image_1_en = face_recognition.face_encodings(known)[0]
    #
    #         res = face_recognition.compare_faces([image_2_en], image_1_en, tolerance=0.5)
    #         print(res)
    #
    #         # print(len(a))
    #         for p in  range(len(a)):
    #             data = ''.join(str(res))
    #             print(data)
    #             print(len(a))
    #
    #             print(p)
    #
    #             if res == [True]:
    #                 # print("This is Abdulaziz")
    #                 name = db.serch_by_ph("photos/" + a[i])[2]
    #                 q_user = db.serch_by_ph("photos/" + a[i])[1]
    #                 photo = db.serch_by_ph("photos/" + a[i])[3]
    #                 t_user = db.serch_by_ph("photos/" + a[i])[4]
    #                 phone = db.serch_by_ph("photos/" + a[i])[5]
    #                 season = db.serch_by_ph("photos/" + a[i])[6]
    #                 stay = db.serch_by_ph("photos/" + a[i])[7]
    #                 # print(name)
    #                 await bot.send_message(message.from_user.id,
    #                                        f"Ismi: {name}\nTelegram user name: @{t_user}\nTelefon raqami: {phone}\nSeason: {season}\nOtiradigan xonasi: {stay}")
    #                 mydir = "/Users/student/PycharmProjects/Face_bot/image_unknown/photos"
    #                 filelist = glob.glob(os.path.join(mydir, "*.jpg"))
    #                 for f in filelist:
    #                     os.remove(f)
    #
    #                 break
    #             else:
    #                 # continue
    #                 await bot.send_message(message.from_user.id,
    #                                        "Bu odam registrasiyadan o'tmagan, yoki yuborgan rasimingiz tiniq emas(yuz qismi toliq korinishi kerak)")
    #             # break
    #
    #             # mydir = "/Users/student/PycharmProjects/Face_bot/image_unknown/photos"
    #
    #             # filelist = glob.glob(os.path.join(mydir, "*.jpg"))
    #             #
    #             # for f in filelist:
    #             #     os.remove(f)
    #
    #
    #
    #
    #     except:
    #         await bot.send_message(message.from_user.id,
    #                                "Bu odam registrasiyadan o'tmagan, yoki yuborgan rasimingiz tiniq emas(yuz qismi toliq korinishi kerak)")
    #         mydir = "/Users/student/PycharmProjects/Face_bot/image_unknown/photos"
    #         filelist = glob.glob(os.path.join(mydir, "*.jpg"))
    #         for f in filelist:
    #             os.remove(f)
    #         break














        # print(res)

        # print(a[i])

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)