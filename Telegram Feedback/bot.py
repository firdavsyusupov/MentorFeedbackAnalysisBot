import config
import logging
import numpy as np
import markups as nav
import glob, os, os.path
from aiogram.dispatcher import FSMContext
from aiogram import Bot, types, executor, Dispatcher
from aiogram.types.message import ContentType, ContentTypes
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sql_1 import Databasee
from aiogram.types import ReplyKeyboardRemove

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
db = Databasee('db_astrum (3).db')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Yonalshingizni tanlang', reply_markup=nav.direction)
    else:
        await bot.send_message(message.from_user.id, "Salom :)", reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='ds')
async def ds(message: types.CallbackQuery):
    if db.get_signup(message.from_user.id) == 'settext':

        #if db.get_signup(message.from_user.id) == 'setdirection':
        db.set_directions(message.from_user.id, 'ds')
        db.set_signup(message.from_user.id, 'done')
        #await bot.delete_message(message.from_user.id, message.message_id)
        user_id = message.message.from_user.id
        await message.message.delete()
        await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                               reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='fs')
async def fs(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                           reply_markup=nav.mainMenu)
    if db.get_signup(message.from_user.id) == 'settext':
        db.set_directions(message.from_user.id, 'fs')
        db.set_signup(message.from_user.id, 'done')


@dp.callback_query_handler(text='se')
async def se(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    await bot.send_message(message.from_user.id, "O'z Munosabatingizni qoldirishingizni iltimos qilamiz!",
                           reply_markup=nav.mainMenu)
    if db.get_signup(message.from_user.id) == 'settext':
        db.set_directions(message.from_user.id, 'se')
        db.set_signup(message.from_user.id, 'done')


@dp.callback_query_handler(text='m1')
async def m1(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    #if db.add_mentor(message.from_user.id) == 'setmentor':
    db.add_users(message.from_user.id)
    db.add_mentor(message.from_user.id, 'Azodov Sarvar')
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m2')
async def m2(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor(message.from_user.id, "Olloyorov Sirojiddin")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m3')
async def m3(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor(message.from_user.id, 'Rasulov Rahmatulloh')
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m4')
async def m4(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor(message.from_user.id, "Shomurodov Sarvarbek")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m5')
async def m5(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor(message.from_user.id, "Shukurov Jasur")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m6')
async def m6(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor(message.from_user.id, "Azizova Aziza")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m7')
async def m7(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor(message.from_user.id, "Arslanova Nodira")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m8')
async def m8(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor(message.from_user.id, "Alimbayeva Asalbonu")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='m9')
async def m9(message: types.CallbackQuery):
    user_id = message.message.from_user.id
    await message.message.delete()
    db.add_mentor(message.from_user.id,"Orifjonov Abdulaziz")
    await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)


@dp.callback_query_handler(text='bc1')
async def bc1(message: types.CallbackQuery):
    pass


@dp.callback_query_handler(text='bc2')
async def bc1(message: types.CallbackQuery):
    pass


@dp.callback_query_handler(text='bc3')
async def bc1(message: types.CallbackQuery):
    pass

@dp.callback_query_handler(text='bdc1')
async def bc1(message: types.CallbackQuery):
    pass

@dp.callback_query_handler(text='bdc2')
async def bc1(message: types.CallbackQuery):
    pass

@dp.callback_query_handler(text='bdc3')
async def bc1(message: types.CallbackQuery):
    pass

@dp.callback_query_handler(text='btc1')
async def bc1(message: types.CallbackQuery):
    pass

@dp.callback_query_handler(text='btc2')
async def bc1(message: types.CallbackQuery):
    pass

@dp.callback_query_handler(text='btc3')
async def bc1(message: types.CallbackQuery):
    pass

@dp.callback_query_handler(text='btc4')
async def bc1(message: types.CallbackQuery):
    pass



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


@dp.message_handler(content_types=['text'])
async def other_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Reaktsiya qoldirish':
            await bot.send_message(message.from_user.id, 'Assalomu aleykum 😊', reply_markup=types.ReplyKeyboardRemove())
            #await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.mentors)
            if db.get_directions(message.from_user.id) == 'ds':
                await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.ds_mentors)
            elif db.get_directions(message.from_user.id) == 'fs':
                await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.fs_mentors)
            elif db.get_directions(message.from_user.id) == 'se':
                await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.se_mentors)



        if message.text == 'Data Science':
            await bot.send_message(message.from_user.id, 'Ok', reply_markup=nav.direction.ReplyKeyboardRemove())
            if db.get_signup(message.from_user.id) == 'settext':
                db.set_directions(message.from_user.id, 'ds')
                db.set_signup(message.from_user.id, 'done')

while True:
    try:
        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=True)
    except:
        continue
    break
