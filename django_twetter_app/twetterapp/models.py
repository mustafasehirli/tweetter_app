from django.db import models

class Tweet(models.Model):
    nickName = models.CharField(max_length=20)
    messange = models.CharField(max_length=50)

    def __str__(self):
        return f"Tweet NickName : {self.nickName} Messange : {self.messange}"
