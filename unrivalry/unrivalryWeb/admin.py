from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(MusicForDistribution)
admin.site.register(Artist)
admin.site.register(MusicGenre)
admin.site.register(MusicSubGenre)
