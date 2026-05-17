from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_verification_email(user_id):
    from casi.users.models import User
    user = User.objects.get(id=user_id)
    verify_link = f"http://127.0.0.1:8000/api/users/verify/?token={user.verification_token}"
    send_mail(
        subject="Email Verification - CASI",
        message=f"Click to verify:\n{verify_link}\n\nExpires in 10 minutes.",
        from_email="noreply@casi.uz",
        recipient_list=[user.email]
    )


@shared_task
def send_verification_telegram(chat_id, code):
    import asyncio
    from aiogram import Bot
    Token = "8765720511:AAFYx3YZ5GYRhIifB_PiXCQvI8tDG2Zv0Xs"
    async def send():
        bot = Bot(token=Token)
        await bot.send_message(
            chat_id=chat_id,
            text=f"✅ CASI verification code:\n\n<b>{code}</b>\n\n⏰ 3 daqiqa ichida kiriting!",
            parse_mode="HTML"
        )
        await bot.session.close()

    asyncio.run(send())




