from aiogram import Bot, Dispatcher
import config


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)