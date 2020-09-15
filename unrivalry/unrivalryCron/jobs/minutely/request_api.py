from django_extensions.management.jobs import MinutelyJob
import requests


class Job(MinutelyJob):
    help = "Request API"

    def execute(self):
        x = requests.get(
            'http://localhost:8000/api/social_user')
        print(x.text)
        # from django.core import management
        # management.call_command("clearsessions")
