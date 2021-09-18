from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from datetime import datetime
from django.utils.crypto import get_random_string

class Command(BaseCommand):
        def handle(self, *args, **kwargs):
                # return super().handle(*args, **kwargs)
                total = kwargs["total"]
                for i in range(total):
                        User.objects.create_user(username= get_random_string(3), password = "1234")

                now = datetime.today()
                print(User.username)
                print(now)

        def add_arguments(self, parser):
                parser.add_argument("total", type = int) 