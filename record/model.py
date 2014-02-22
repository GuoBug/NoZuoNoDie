#encoding=utf-8
import MySQLdb
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    context = models.TextField()
    category = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title