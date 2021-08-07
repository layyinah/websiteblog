from django.db import models
import datetime


# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='blog')
    auth = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ('name',)
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'




    def __str__(self):
        return '{}'.format(self.name)

