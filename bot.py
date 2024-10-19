import asyncio 

from aiogram.types import Message, WebAppInfo
from aiogram import Router, Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

def webapp_builder() -> InlineKeyboardBuilder   :
    builder = InlineKeyboardBuilder()
    builder.button(text="let's click", web_app=WebAppInfo(
        url="..."
        )
    )
    return builder.as_markup()


@router.message(CommandStart())
async  def start(message: Message)->None:
    await message.reply('Click, Click, Cllick!', reply_markup=webapp_builder())
        
async def main() ->None:

    bot = Bot(..., parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())