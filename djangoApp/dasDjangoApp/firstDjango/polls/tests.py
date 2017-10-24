from django.test import TestCase as TC

import datetime as dt
from django.utils import timezone as tz
from django.urls import reverse
 
from .models import Question

# Create your tests here.

class ModelTestsQuestion(TC):
	'''Here's a class to test if our Question model is behaving as it's suppose to'''

	def test_wasPubRec_withFuture(self):
		'''here's to make sure our pub_recent return false on dates that are in the future'''
		time = tz.now() + dt.timedelta(days=30)
		futureQ = Question(pub_date = time)
		self.assertIs(futureQ.was_pub_recently(), False)

	def test_waspubrec_oldQuestion(self):
		time = tz.now() - dt.timedelta(days=1, seconds= 1)
		oldQ = Question(pub_date=time)
		self.assertIs(oldQ.was_pub_recently() , False)

	def test_waspubrec_recentQuestion(self):
		time = tz.now() -dt.timedelta(hours = 23, minutes = 59, seconds = 59)
		recQ = Question(pub_date=time)
		self.assertIs(recQ.was_pub_recently() , True)


class IndexViewTestsQuestion(TC):

	def test_no_q(self):
		"""For case of no questions"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code ,200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_past_questions(self):
		'''Question with past pub_dates are displayed on index'''
		create_question(q_text='Past question.', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question.>'])

	def test_future_questions(self):
		'''You shouldn't be allowed to create question with future dates'''
		create_question(q_text="Future Questions" , days= 30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, 'No polls are available.')
		self.assertQuerysetEqual(response.context['latest_question_list'], [])	

	def test_futurePast_question(self):
		create_question(q_text="Future Questions" , days= 30)
		create_question(q_text='Past question.', days=-30)
		response = self.client.get(reverse('polls:index'))
		expected = ['<Question: Past question.>']
		self.assertQuerysetEqual(response.context['latest_question_list'], expected)
	
	def test_cantCopyAndPasteThisStuff8C_question(self):
		create_question(q_text="Past Q1." , days= -50)
		create_question(q_text='Past Q2.', days=-30)
		response = self.client.get(reverse('polls:index'))
		expected = ['<Question: Past Q2.>','<Question: Past Q1.>']	#Okay, this quesery set sure as fuck isn't testing set vs set
		self.assertQuerysetEqual(response.context['latest_question_list'], expected)
	
def DetailViewTestQuestion (self):
	def test_future_q(self):
		futureQ = create_question('The future is here!', 150)
		url = reverse('polls:detail', args=(futureQ.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)

	def test_past_q(self):
	    pastQ = create_question('I am the Past.', -123)
	    url = reverse('polls:detail', args= (pastQ.id))
	    response = self.client.get(url)
	    self.assertContains(response, pastQ.q_text)

# Helper functions here
def create_question(q_text, days):
		'''
		Create questions with arguments q_text and the days 
		(negative days are in the past, positive days are in the future)
		'''
		time = tz.now() + dt.timedelta(days=days)
		return Question.objects.create(q_text =q_text, pub_date = time)
