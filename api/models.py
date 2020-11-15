from django.db import models
import datetime
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255,null=False,blank=False)
    desc = models.TextField(null=True,blank=False)
    image = models.ImageField(upload_to = 'pics',null=True, blank=True)
    time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title
    