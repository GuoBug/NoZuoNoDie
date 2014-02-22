#encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb
from model import *

def Contact(request):
	return render_to_response('aboutMe.html')

def HomePage(request):
	allBlog = Blog.objects.all().values()
	print type(allBlog)
	return render_to_response('home.html',{'bloginfo': allBlog})