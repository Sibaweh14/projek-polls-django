from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse('halo nama saya guslizen effayed')

def otherIndex(request):
	return HttpResponse('ini ali siddiq')