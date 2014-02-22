#encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb
from model import *

def Contact(request):
	return render_to_response('aboutMe.html')

def HomePage(request):
	blog = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
	blog.save()
	return render_to_response('aboutMe.html')