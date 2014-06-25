"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Post

class PostTests(TestCase):
	def test_str(self):
		my_title = Post(title='This is a basic title for a basic test case')
		self.assertEquals(str(my_title), 'This is a basic title for a basic test case',)
