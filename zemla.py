import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest

# Loggingni yoqamiz — terminalda nimalar bo'layotganini ko'ramiz
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8782359002:AAEN_zkmcPdYbTua2K9buir-9erhjGyexCM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def join_request_handler(request: ChatJoinRequest):
    user = request.from_user
    chat = request.chat
    
    user_name = user.full_name or user.username or "Foydalanuvchi"
    channel_name = chat.title or "Bizning kanal/guruh"

    welcome_text = (
        f"Assalomu alaykum, {user_name}! 👋\n\n"
        f"{channel_name} ga xush kelibsiz!\n"
        "Sizning so'rovingiz qabul qilindi.\n"
        "Admin tez orada ko'rib chiqadi va tasdiqlaydi. Biroz kuting 😊"
    )

    # Faqat lichkaga xabar yuboramiz
    try:
        await bot.send_message(
            chat_id=user.id,
            text=welcome_text,
            # parse_mode="MarkdownV2"   # agar kerak bo'lsa qo'shishingiz mumkin
        )
        logger.info(f"Xabar yuborildi → {user.id} ({user_name})")
    except Exception as e:
        logger.error(f"Lichkaga xabar yuborib bo'lmadi: {e} | User: {user.id}")


async def main():
    logger.info("Bot ishga tushdi... (faqat xabar yuboradi, tasdiqlamaydi)")
    await dp.start_polling(bot, allowed_updates=["chat_join_request"])


if __name__ == "__main__":
    asyncio.run(main())
