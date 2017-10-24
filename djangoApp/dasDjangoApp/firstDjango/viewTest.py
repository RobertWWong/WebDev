#First, setup your test environment 
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstDjango.settings")
django.setup()

#Then perform the actual setup
from django.test.utils import setup_test_environment as ste
ste()


#From here, we'll be testing if we are send and receiving correctly
from django.test import Client
from django.urls import reverse

client = Client()
response = client.get('/')
response.status_code

response = client.get (reverse('polls:index'))
print(response.status_code)
print('\n\n')
print(response.content)
print('\n\n')
print(response.context['latest_question_list'])