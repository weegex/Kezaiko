import asyncio
import logging
import modules

from aiogram import Bot, Dispatcher
from utils import Secrets


def setup(token: str) -> tuple[Bot, Dispatcher]:
    bot = Bot(
        token=token
    )

    dp = Dispatcher()

    dp.include_router(
        modules.router
    )

    return (bot, dp)


async def run(bot: Bot, dp: Dispatcher) -> None:
    logging.basicConfig(level=logging.NOTSET)

    await dp.start_polling(bot)


if __name__ == "__main__":
    secrets = Secrets()

    try:
        asyncio.run(
            run(
                *setup(
                    token=secrets.token
                )
            )
        )
    except KeyboardInterrupt:
        print("Stoping...")
