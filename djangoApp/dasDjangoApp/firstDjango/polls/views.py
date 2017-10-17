from django.shortcuts import get_object_or_404,render

from django.http import HttpResponse  	#Dont need this if we use render()
from django.http import Http404

from django.template import loader 		#Dont need this if we use render()

from .models import Question
# Create your views here. You will be assigning url regex via urls.py of your resepect view directory

def index(request):
	# print("Yes, do treat your HttpResponses as html iterpreter.")

	#We don't want to hard-code our views. Wouldn't be OOP.
	latest_q_list = Question.objects.order_by('-pub_date')[:5]

	# Here's one way to render your html files, but it's a bit klunky
	# template = loader.get_template('polls/index.html')
	# context = {
	# 'latest_q_list' : latest_q_list
	# }
	context ={				#Think of your context as the data-bound value,  or ng-model
		'latest_q_list': latest_q_list
	}
	yourTemplatePath = 'polls/index.html'	#Since we have set up our template folder, 
	#and we won't need to import loader and HttpResponse if we use Render like this

	return render(request,  yourTemplatePath, context)



#Add some more views to our polls
def detail( request, q_id):
	"""
	Time to write some 404 cases:
	Here's a hint, it's a helper function for django.shortcuts get_object_or_404
	"""
	question = get_object_or_404(Question, pk=q_id)
	# try:
	# 	question = Question.objects.get(pk= question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Yeah, that's not a question at all. Well, around here that is.")
	return render(request, 'polls/detail.html', {"question": question})


def results(request, q_id):
	response = "You're looking at question %s." 
	return HttpResponse(response % q_id)		#Use a str var to later format it
def vote(request, q_id):
	return HttpResponse("You're voting on question %s." % q_id)

