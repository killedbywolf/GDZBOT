from aiogram import executor
from handlers import dp


if __name__ == '__main__':
    print('Бот запущен')
    executor.start_polling(dp)