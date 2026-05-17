# telegram_bot/management/commands/run_bot.py
import asyncio
from django.core.management.base import BaseCommand
from casi.telegram_bot.bot import main


class Command(BaseCommand):
    help = "Run Telegram bot"

    def handle(self, *args, **kwargs):
        self.stdout.write("🤖 Bot ishga tushdi...")
        asyncio.run(main())
