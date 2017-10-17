from django.conf.urls import url

from . import views


#You link views from views.py to the url in this folder

#Time to namespace properly, or all hells will break loose.
app_name = 'polls'		#You'll have to tag this into your template htmls
urlpatterns = [
	url(r'^$',  views.index, name = 'index'),
	
	#ex is polls/23
	url(r'^(?P<q_id>[0-9]+)/$',  views.detail, name = 'detail'),
	
	#ex is polls/23/results
	url(r'^(?P<q_id>[0-9]+)/results/$',  views.results, name = 'results'),
	url(r'^(?P<q_id>[0-9]+)/vote/$',  views.vote, name = 'vote')
	]