

from celery import shared_task

@shared_task
def run_bot():
    from casi.telegram_bot.bot import start_bot
    start_bot()
