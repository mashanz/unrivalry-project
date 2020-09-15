from django_extensions.management.jobs import MinutelyJob
import requests
import os


class Job(MinutelyJob):
    help = "Request API"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filename = f"{BASE_DIR}/jobs.log"

    def execute(self):
        with open(self.filename, 'a') as f:
            x = requests.get(
                'http://localhost:8000/api/test')
            print(x.text, file=f)
        # from django.core import management
        # management.call_command("clearsessions")
