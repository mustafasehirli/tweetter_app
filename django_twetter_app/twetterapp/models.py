from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    messange = models.CharField(max_length=50)

    def __str__(self):
        return f"Tweet User : {self.username} Messange : {self.messange}"
