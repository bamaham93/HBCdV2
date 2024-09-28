from django.test import TestCase
from django.contrib.auth.models import User
from prayer.models import Request
from .forms import RequestForm
from .models import Request


# Create your tests here.
class TestRequestsApp(TestCase):
    """
    """

    # def SetUp(self):
    #     """
    #     :return:
    #     """

    def test_home_page(self):
        c = self.client
        url = '/'
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')
