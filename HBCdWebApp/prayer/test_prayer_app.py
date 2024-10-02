import unittest

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group, GroupManager
from .models import Request
# from .views import is_member_of


# Create your tests here.
class TestRequestsApp(TestCase):
    """
    """

    @classmethod
    def setUpTestData(cls):
        """"""
        User.objects.create(username='bamaham1000@gmail.com', password="None")
        User.objects.create(username="IamAuser", password="None")
        Request.objects.create(first_name="Jacob", last_name="McGowin")

        group = Group(name="Prayer Group")
        cls.prayer_group = group
        group.save()

        User.objects.create_user(username='bamaham1200')
        cls.nonmember_user = User.objects.get(username="bamaham1200")

        User.objects.create_user(username="bamaham1500")
        member_user = User.objects.get(username="bamaham1500")
        member_user.groups.add(group)
        member_user.save()
        cls.member_user = member_user

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
        # self.assertContains(response, 'First Name')
        # self.assertContains(response, 'Last Name')
        # self.assertContains(response, 'Answered?')
        # self.assertContains(response, 'Description')
        self.assertContains(response, 'Add Prayer Request')
        self.assertContains(response, 'Home')
        self.assertContains(response, 'Accounts')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Logout')
        self.assertContains(response, 'Signup')

        url1 = 'home'
        response1 = c.get(reverse(url1))
        self.assertEqual(response1.status_code, 200)

    def test_data_access_restricted_to_group_members(self):
        """
        :return:
        Test that the page DOES NOT contain the sensitive information.
        """

        c = self.client
        nonmember = c.force_login(self.nonmember_user)
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Jacob McGowin")
        self.assertTemplateUsed(response, "prayer/home.html")

    @unittest.expectedFailure
    def test_data_access_restricted_to_group_members_xfail(self):
        """
        :return:
        """
        c = self.client
        nonmember = c.force_login(self.nonmember_user)
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Jacob McGowin")
        self.assertContains(response, "Jacob McGowin")
        self.assertTemplateUsed(response, "prayer/home.html")

    # def test_is_member_of(self):
    #     """
    #     Fails due to for loop in template. Why?
    #     """
    #     # print(Group.objects.get())
    #     # print(self.member_user.groups.get())
    #     try:
    #         self.assertTrue(is_member_of(self.member_user, "Prayer Group", self.member_user.groups.get()))
    #     except TypeError as e:
    #         print(e)
    #         pass
    #     self.assertTrue(is_member_of(self.member_user, "Prayer Group", self.member_user.groups.get()))
