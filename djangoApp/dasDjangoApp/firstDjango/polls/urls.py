from django.conf.urls import url

from . import views
#You link views from views.py to the url in this folder
#Time to namespace properly, or all hells will break loose.
app_name = 'polls'		#You'll have to tag this into your template htmls
urlpatterns = [
	
	url(r'^$',  views.IndexView.as_view(), name = 'index'),
	#ex is polls/23
	#Here's the important thing. If you are using the generic template, make sure to change your quest_id 
	#Or whatever you're capturing to match your query's primary key (pk)
	url(r'^(?P<pk>[0-9]+)/$',  views.DetailView.as_view(), name = 'detail'),	
	#ex is polls/23/results
	url(r'^(?P<pk>[0-9]+)/results/$',  views.ResultsView.as_view(), name = 'results'),
	url(r'^(?P<q_id>[0-9]+)/vote/$',  views.vote, name = 'vote'),

	]