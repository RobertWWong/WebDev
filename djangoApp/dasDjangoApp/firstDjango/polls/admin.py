from django.contrib import admin
from .models import Question, Choice

# Register your models here. So you can see it on admind site

admin.site.register([Question,Choice])