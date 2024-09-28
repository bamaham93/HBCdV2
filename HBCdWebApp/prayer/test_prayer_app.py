from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TestRequestsApp(TestCase):
    """
    """

    def test_home_page(self):
        """
        Checks the home page.
        """
        c = self.client
        url = '/'
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')

        # For regression testing; May be removed later?
        self.assertContains(response, 'Harvest Baptist Church')
        self.assertContains(response, 'First Name')
        self.assertContains(response, 'Last Name')
        self.assertContains(response, 'Answered?')
        self.assertContains(response, 'Description')
        self.assertContains(response, 'Add Prayer Request')
        self.assertContains(response, 'Home')
        self.assertContains(response, 'Accounts')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Logout')
        self.assertContains(response, 'Signup')

        url1 = 'home'
        response1 = c.get(reverse(url1))
        self.assertEqual(response1.status_code, 200)
