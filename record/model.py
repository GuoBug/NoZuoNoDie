#encoding=utf-8
import MySQLdb
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    @classmethod
    def create(cls,title):
    	book = cls(title = title)
