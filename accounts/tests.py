from django.test import TestCase
from accounts.models import RiddanceUser, RiddanceProfile


class TestUserCreation(TestCase):

    def setUp(self):
        self.user = RiddanceUser.objects.create_user("example@example.com", '123123')

    def test_if_user_creation_signal_creates_user_profile(self):
        profile = RiddanceProfile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)

    def test_first_name_max_length(self):
        max_length = self.user._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)







