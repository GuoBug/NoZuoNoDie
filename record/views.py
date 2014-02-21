#encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb

def hello(request):
	return render_to_response('aboutMe.html')