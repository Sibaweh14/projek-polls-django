from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.http import Http404
# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	context = {
		"latest_question_list": latest_question_list,
	}
	return render(request,"polls/index.html", context)


def detail(request, question_id):
	try:
		question = Question.objects.get(id=question_id)
	except Question.DoesNotExist:
		raise Http404('Question doesnt exist')
	return render(request, 'polls/detail.html', {'question':question})


def result(request, question_id):
	response = "you're looking at ther result of question %s."
	return HttpResponse(response % question_id)



def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
