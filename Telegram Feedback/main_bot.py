import json
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import config
import logging
import DateTime
import numpy as np
import markups as nav
import glob, os, os.path
from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram import Bot, types, executor, Dispatcher
from sql_1 import Databasee
from aiogram.types import ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)
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

        class Form(StatesGroup):
            # btn = State()
            mentor = State()
            reaktiya = State()
            sabab = State()
            bad = State()
            good = State()
            great = State()

        @dp.message_handler(state=Form.mentor)
        async def process_name(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['mentor'] = message.text
            await Form.next()
            await bot.send_message(message.from_user.id, 'Mentorni tanglang', reply_markup=nav.se_mentors)

        @dp.message_handler(state=Form.reaktiya)
        async def process_name(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['reaktsiya'] = message.text
            await Form.next()
            await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)

        @dp.message_handler(state=Form.sabab)
        async def process_name(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['sabab'] = message.text
            await Form.next()
            await bot.send_message(message.from_user.id, 'Reaktsiya qoldiring', reply_markup=nav.estimation)



@dp.callback_query_handler(text='ds')
async def ds(message: types.CallbackQuery):
    if db.get_signup(message.from_user.id) == 'settext':
        db.set_directions(message.from_user.id, 'ds')
        db.set_signup(message.from_user.id, 'done')
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


@dp.message_handler(content_types=['text'])
async def other_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Reaktsiya qoldirish':
            await bot.send_message(message.from_user.id, 'Assalomu aleykum 😊',
                                   reply_markup=types.ReplyKeyboardRemove())
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

        if message.text == 'astrum#2021':
            await bot.send_message(message.from_user.id, 'Analysis', reply_markup=nav.adm_analysis)
            pass



while True:
    try:
        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=True)
    except:
        continue
    break
