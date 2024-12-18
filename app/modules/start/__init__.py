from aiogram import Router, filters, types


router = Router()


@router.message(filters.CommandStart())
async def start_command(message: types.Message) -> None:
    await message.answer(
        text="Hello, world!!!"
    )
