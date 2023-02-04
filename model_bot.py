from config import * 
import requests
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

bot = Bot(token = tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_comand(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я покажу тебе сводку погоды.")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={openweather_keys}&units=metric&lang={lang}'
        )
        data = r.json()

        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = round((data["main"]["pressure"] * 0.750064), 2)
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
        f"Погода в городе {city}\nТемпература: {temperature} С\n"
        f"Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст.\n"
        f"Скорость ветра: {wind} м/с\nВосход солнца: {sunrise_timestamp}\n"
        f"Закат: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
        f"Хорошего дня!"
        )
        
    except:
        await message.reply("Проверьте название города")