from django.db import models

# Create your models here.
class Dashboard(models.Model):
    pass

class ServerProfiling(models.Model):
    pass

class Album(models.Model):
    pass

class Music(models.Model):
    pass

class Settings(models.Model):
    pass

class AdminDashboard(models.Model):
    class Meta:
        permissions = (
            ("dashboard", "Dashboard"),
            ("server_profiling", "Server Profiling"),
            ("album", "Album"),
            ("music", "Music"),
        )