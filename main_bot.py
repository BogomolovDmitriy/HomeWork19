import model_bot as m_b
from config import *
from aiogram.utils import executor

if __name__ == '__main__':
    print("server start")
    executor.start_polling(m_b.dp)
    