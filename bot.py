import asyncio
import logging
from loader import bot
from handlers import dp
from misc import set_my_commands

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)
async def main():
    logger.info("Starting bot")
    # start
    set_my_commands()

    try:
        await dp.start_polling(bot)
    finally:
        logger.info("Stopping bot")
        await dp.storage.close()
        await bot.session.close()

    return "some json"


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("EXIT!")
#%%
