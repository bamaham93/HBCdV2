from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .views import signup, sign_in, sign_out


class TestUsersApp(TestCase):
    """
    """

    # def SetUp(self):
    #     """
    #     """

    @classmethod
    def setUpTestData(cls):
        """
        """
        cls.user = User.objects.create_user(username='bamaham', email='babablacksheep@gmail.com', password='top secret')
        cls.my_user = User.objects.get()

        cls.user = User.objects.create_superuser('bamaham2004', 'www.@gmail.com', 'top secrets')
        cls.super_user = User.objects.get(username='bamaham2004')

    def test_users_created_correctly(self):
        """
        Tests that these users have the correct credentials.
        """
        # For testing unprivileged access, and to check for improper access to privileged information.
        user = self.my_user
        self.assertEqual(user.username, 'bamaham')
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.is_active, True)

        # For testing privileged access, admin pages.
        super_user = self.super_user
        self.assertEqual(super_user.username, 'bamaham2004')
        self.assertEqual(super_user.is_staff, True)
        self.assertEqual(super_user.is_superuser, True)
        self.assertEqual(super_user.is_active, True)

    def test_user_signup_page(self):
        """"
        Tests the page, form, submission, and handling for the user account signup page.
        """
        c = self.client
        url = '/auth/signup/'

        # Checks GET requests.
        response = c.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/signup.html')

        # Checks POST requests
        response1 = c.post(url, {'username': 'bamainthewind', 'email': 'bamaham5009@gmail.com', 'password1': 'Secret!Inthebeginning', 'password2': 'Secret!Inthebeginning'}, follow=False)
        self.assertEqual(response1.status_code, 302)

        # Tests that the newly created user can be recalled from the DB.
        # If not, results in a failed test.
        User.objects.get(username='bamainthewind')

    def test_login_page(self):
        """
        """

        c = self.client
        url = '/auth/login'
        response = c.get(url)

        # TODO Check this response is correct.
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed('users/login.html')

    def test_logout_page(self):
        c = self.client
        url = '/auth/logout'
        response = c.get(url)
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed('/auth/logout.html')
