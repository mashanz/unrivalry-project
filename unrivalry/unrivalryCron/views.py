from background_task import background
from django.contrib.auth.models import User

from django.shortcuts import render
from .debug import debug
import requests
import os
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = f"{BASE_DIR}/unrivalryCron/cron.log"


@debug
def index():
    with open(filename, 'a') as f:
        print("[CRONTAB] It is a cron", file=f)
        x = requests.get(
            'http://localhost:8000/api/social_user')
        print(x.text, file=f)


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
