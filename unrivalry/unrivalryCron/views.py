from background_task import background
from django.contrib.auth.models import User

from django.shortcuts import render
from .debug import debug
import requests

# Create your views here.


@debug
def index():
    print("[CRONTAB] It is a cron")
    x = requests.get(
        'http://localhost:8000/api/social_user')
    print(x.text)


class CronViews():
    # @debug
    def index():
        print("[CRONTAB] It is a cron")
        x = requests.get(
            'http://localhost:8000/api/social_user')
        print(x.text)

    # @background(schedule=10)
    # def _background():
    #     print("[BACKGROUND] It is a cron")
    #     # x = requests.get(
    #     #     'http://localhost:8000/api/social_user')
    #     # print(x.text)
