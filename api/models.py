from django.db import models
import datetime
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255,null=False,blank=False)
    desc = models.TextField(null=True,blank=False)
    link = models.CharField(max_length=255,null=True,blank=False)
    image = models.ImageField(upload_to = 'pics',null=True, blank=True)
    logo = models.ImageField(upload_to = 'logo',null=True, blank=True)
    time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title
    