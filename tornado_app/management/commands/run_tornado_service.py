from django.core.management.base import BaseCommand

from tornado_app import app


class Command(BaseCommand):
    help = "Run Tornado service"

    def add_arguments(self, parser):
        parser.add_argument(
            '--port',
            default=None,
            help='Port for tornado application to listen on',
        )

    def handle(self, *args, **options):
        if options['port']:
            app.run(port=options['port'])
        else:
            app.run()

        return None
