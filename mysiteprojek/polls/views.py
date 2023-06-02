from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse('halo nama saya guslizen effayed, saya adalah seorang programmer yang sukses')

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def result(request, question_id):
	response = "you're looking at ther result of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
