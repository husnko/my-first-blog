from django.db import models

class User(models.Model):
    user_id = models.IntegerField
    user_nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.user_nickname
