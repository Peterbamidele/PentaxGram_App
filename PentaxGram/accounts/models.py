from django.db import models


class Owner(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=20)
    bio = models . TextField(null=True)
    profile_picture = models.ImageField(default='user.png')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# Create your models here.
