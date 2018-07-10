from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class a_M_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    am_add = models.EmailField()

    def __str__(self):
        return self.user.username