from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect  , HttpResponse
from django.urls import reverse
from django.views import generic

from django.utils import timezone as tz
from .models import Question, Choice
# Create your views here. You will be assigning url regex via urls.py of your resepect view directory
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		'''Return the last five published questions.'''
		# return Question.objects.order_by('-pub_date')[:5]
		return Question.objects.filter(pub_date__lte=tz.now()
			).order_by('-pub_date')[:5]

#Now our views will be an object itself
class DetailView (generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		'''Only get published questions'''
		return Question.objects.filter(pub_date__lte=tz.now())
	
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, q_id):
	quest = get_object_or_404(Question, pk = q_id)
	try:
		selected_choice = quest.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist) :
		whoopsies = {'question': quest, 'error_message': "You didn't select a choice, pham."}
		return render(request, 'polls/detail.html', whoopsies)
	else:
		selected_choice.votes +=1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse ( "polls:results", args=(quest.id,)))

	# return HttpResponse("You're voting on question %s." % q_id)

