import os
from tornado_app.app import options, run
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate.settings")

    django.setup()

    if options.port:
        run(port=options.port)
    else:
        run()
