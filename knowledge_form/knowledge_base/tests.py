from urllib import request, response
from django.http import HttpRequest
from django.test import TestCase
from knowledge_base.views import top

# Create your tests here.
class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        # request = HttpRequest()
        # response = top(request)
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
        
    def test_top_retruns_expected_content(self):
        # request = HttpRequest()
        # response = top(request)
        response = self.client.get("/")
        self.assertEqual(response.content,b"Hello World")
