from django.db import models
import datetime as dt

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	"""docstring for Question"""
	q_text = models.CharField(max_length=200)	
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.q_text
	
	def was_pub_recently(self):
		return self.pub_date >= timezone.now()

	def create_choices(self, choice, vote_num):
		"""
		Helpful choice creation method. Gonna need to read the documents
		But as of right now, this adds a choice to our question.
		"""
		return self.choice_set.create(choice_text = choice, votes = vote_num )
		print("I done diddly added {} to your {} set!".format(choice, self))


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

print(''' Here's some dandy little tips\n
	Change your models (in models.py).
	Run python manage.py makemigrations to create migrations for those changes
	Run python manage.py migrate to apply those changes to the database.
	''')

dt.timedelta(days = 1)	#Wonder what this means?
