from django.contrib import admin

# Register your models here.
from .models import  Choice,Question

class ChoiceInLine(admin.StackedInline):
	'''This class would directly allow us to add a bunch of choices during Question creation'''
	model = Choice
	extra = 3	#This means in our admin page, it will create... 3 new Choice bars 

class QuestionAdmin(admin.ModelAdmin):
	"""What this does is change the orientation and our questions. And what it will display
	However, it still does not display the choiceset of our questions
	"""

	fieldsets = [
	(None				,	{'fields': ['q_text']} ),
	('Date information', 	{'fields': ['pub_date']	, 'classes':['collapse'] }),		#notice the class
	]

	inlines = [ChoiceInLine]			#don't understand inlines variable. is it a field in ModelAdmin?

#What these methods do is display to the admin page a list of available items located
#within our database. So our admins to actually to do RESTful things.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)		#Don't need this if using inline classes