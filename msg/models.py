from django.db import models

# Create your models here.
class Message(models.Model):
    rec_add = models.EmailField(null = False)
    title   = models.CharField(max_length = 255, null = True, required = False)
    message = models.TextField()

    def __str__(self):
        return self.title
