from django.core.management.base import BaseCommand
from thedatabet.betway import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()