from aiogram import Bot, Dispatcher
# import redis
# from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.memory import MemoryStorage
import config


class Fee():
    type: str
    size: int


fee = Fee()
storage = MemoryStorage()
bot = Bot(token=config.token)
dp = Dispatcher(bot=bot, storage=storage)