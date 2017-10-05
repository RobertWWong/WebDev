from django.shortcuts import render

from django.http import HttpResponse


def index(request):
	print("Yes, do treat your HttpResponses as html iterpreter.")
	return HttpResponse("Hellow World, welcome to my polling of 'Robert Developing Skills as stated in his resume.\n<br>Rate me")

# Create your views here.
