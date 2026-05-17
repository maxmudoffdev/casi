
# casi/telegram_bot/bot.py
import asyncio
import logging
import random
from datetime import timedelta

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CopyTextButton
from django.conf import settings

logging.basicConfig(level=logging.INFO)

Token = "8765720511:AAFYx3YZ5GYRhIifB_PiXCQvI8tDG2Zv0Xs"
bot = Bot(token=Token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "👋 Salom! CASI platformasiga xush kelibsiz!\n"
            "Ro'yxatdan o'tish uchun platformaga o'ting."
        )
        return

    token = args[1]

    from asgiref.sync import sync_to_async
    from django.contrib.auth import get_user_model
    from django.utils import timezone

    User = get_user_model()

    try:
        get_user = sync_to_async(User.objects.get)
        user = await get_user(verification_token=token)
    except User.DoesNotExist:
        await message.answer("❌ Token noto'g'ri!")
        return

    # Token muddati o'tganmi?
    if user.verification_token_expires < timezone.now():
        await message.answer(
            "❌ Token muddati o'tdi!\n"
            "Qayta ro'yxatdan o'ting."
        )
        return

    # 6 ta code yaratish
    code = str(random.randint(100000, 999999))

    # Saqlash
    user.telegram_chat_id = message.chat.id
    user.telegram_verification_code = code
    user.telegram_code_expires = timezone.now() + timedelta(minutes=5)
    save_user = sync_to_async(user.save)
    await save_user()

    # Copy tugmasi
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📋 Copy code",
                copy_text=CopyTextButton(text=code)  # ✅
            )
        ]
    ])

    await message.answer(
        f"✅ Sizning tasdiqlash kodingiz:\n\n"
        f"<code>{code}</code>\n\n"
        f"⏰ 5 daqiqa ichida saytga kiriting!",
        parse_mode="HTML",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)
