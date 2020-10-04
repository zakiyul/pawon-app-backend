from django.db import models


class LandingPage(models.Model):
    strongTitle = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    btnTitle = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media/hero/')

    def __str__(self):
        return self.title
