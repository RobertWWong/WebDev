#Created a db demo setup, for the Question "What's time is it?"
#Didn't really want to type it out everytime I start the shell

from polls.models import Question as q, Choice as c
from django.utils import timezone as tz
q1 = q.objects.get(pk=1)
print("Okay, q and q1 has been set up for inshell access!")	
print("""
		So far, you can add new questions via Question.create_choices(q_text, vote#)
		However, this was abstracted from 
		Question.choice_set.create(choice_text , votes) 
		//with the args being your Choice Model	fields

		You can select your choice in the same manner as your questions
		""")

yourShellAPi= """
 The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
Choice.objects.filter(question__pub_date__year=current_year)
"""
if __name__ =='__main__':		
	q1 = q.objects.get(pk=1)
	print("You started straight into this file fam.\n\n")
	print("Okay, q and q1 has been set up for inshell access!")
	
	q.objects.all()
	q1.choice_set.all()