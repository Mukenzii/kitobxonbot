from ...views import bot
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Bot working"

    def handle(self, *args, **options):
        self.stdout.write("Bot starting...")
        bot.set_webhook(url="https://kitobxon-marafoni.xayrli.uz/webhook")