from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=65)
    text = models.TextField()
    tags = models.CharField(max_length=80)
    user = models.CharField(max_length=80)
    date = models.DateField(auto_now_add=True)
    isVisible = models.BooleanField(default=False)

    def __str__(self):
        return self.title




# Create your models here.
