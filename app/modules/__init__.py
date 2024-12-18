from aiogram import Router
from modules import (
    start
)


router = Router()


@router.startup()
async def on_startup() -> None:
    print("The bot has been launched!")


router.include_routers(
    start.router
)
