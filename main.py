import asyncio
import aiogram
from aiogram import Bot, Dispatcher, Router, html
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from downloader import download_music
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

dp = Dispatcher()

@dp.message(Command("start"))
async def start (message: Message):
    await message.answer(
        "Привет, друг! 👋\n"
        "Добро пожаловать в лучший поиск треков!\n"
        "Просто пришли мне ссылку и я найду mp3 версию :)"
    )

    await message.answer(
        "Ты можешь импортировать видео в формате mp3 и mp4.\n"
        "Что послушаем? 🎵"
    )

@dp.message(Command("help"))
async def help (message: Message):
    await message.answer("Просто пришли мне ссылку и я найду mp3 версию :)")

@dp.message(Command("Lol"))
async def funny (message: Message):
    await message.answer_sticker("CAACAgIAAxkBAAMiagzWorubEVKzLRUTZ2jD00kI3C8AAkdZAAId0SBLTDROIH-Fiyg7BA")

# @dp.message()
# async def mus_download(message: Message):
#     url = message.text
#     await message.answer("Начинаю скачивание...")
#     file_path = download_music(url)

#     audio = FSInputFile(file_path)

#     await message.answer_audio(audio)

@dp.message()
async def mus_download(message: Message):
    url = message.text
    await message.answer("Начинаю скачивание...")






async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен...")