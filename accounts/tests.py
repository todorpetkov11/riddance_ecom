from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from accounts.forms import RiddanceProfileForm
from accounts.models import RiddanceUser, RiddanceProfile


class TestUserCreation(TestCase):

    def setUp(self):
        self.user = RiddanceUser.objects.create_user("example@example.com", '123123')

    def test_if_user_creation_signal_creates_user_profile(self):
        profile = RiddanceProfile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)

    def test_email_max_length(self):
        max_length = self.user._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)


class TestProfile(TestCase):

    def setUp(self):
        self.user = RiddanceUser.objects.create_user("example@example.com", '123123')

    def test_profile_edit_invalid_full_name_should_raise(self):
        profile = RiddanceProfile.objects.get(user=self.user)
        profile.full_name = 'asdasd'
        profile.telephone_number = '0888252525'

        try:
            profile.full_clean()
            profile.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_profile_edit_single_name_should_raise(self):
        profile = RiddanceProfile.objects.get(user=self.user)
        profile.full_name = 'Todor'
        profile.telephone_number = '0888252525'

        try:
            profile.full_clean()
            profile.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_if_profile_created_valid_full_name(self):
        profile = RiddanceProfile.objects.get(user=self.user)
        profile.full_name = 'Todor Todor'
        profile.telephone_number = '0888252525'
        profile.full_clean()
        profile.save()
        self.assertIsNotNone(profile)

    def test_if_profile_invalid_phone_number_raise_error(self):
        profile = RiddanceProfile.objects.get(user=self.user)
        profile.full_name = 'Todor Todor'
        profile.telephone_number = '9888252525'
        try:
            profile.full_clean()
            profile.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_if_profile_letters_in_phone_number_raise_error(self):
        profile = RiddanceProfile.objects.get(user=self.user)
        profile.full_name = 'Todor Todor'
        profile.telephone_number = 'qwer123123'
        try:
            profile.full_clean()
            profile.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)


class TestForms(TestCase):

    def setUp(self):
        self.user = RiddanceUser.objects.create_user("example@example.com", '123123')

    def test_profile_form_save_valid(self):
        data = {'full_name': 'Todor Petkov',
                'telephone_number': '0888123123',
                }
        form = RiddanceProfileForm(data)
        self.assertTrue(form.is_valid())

    def test_profile_form_save_invalid(self):
        data = {'full_name': 'asdasd',
                'telephone_number': '0g88123123',
                }
        form = RiddanceProfileForm(data)
        self.assertFalse(form.is_valid())


class TestAccountViews(TestCase):

    def setUp(self):
        self.test_client = Client()
        self.user = RiddanceUser.objects.create_user("example@example.com", '123123')
        self.test_client.login(email='example@example.com', password='123123')

    def test_profile_details_return_template_and_context(self):
        pk = self.user.profile.pk
        response = self.test_client.get(f'/accounts/profile_details/{pk}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='profile_templates/profile_details.html')
        self.assertIsInstance(response.context['profile'], RiddanceProfile)

    def test_edit_profile_details_return_template_and_context(self):
        pk = self.user.profile.pk
        response = self.test_client.get(f'/accounts/edit_profile/{pk}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='profile_templates/edit_profile.html')
        self.assertIsInstance(response.context['profile'], RiddanceProfile)
        self.assertIsInstance(response.context['form'], RiddanceProfileForm)

    def test_logout_user_redirects_to_landing(self):
        response = self.test_client.post(f'/accounts/logout/')
        self.assertRedirects(response, '/about_us/')

    def test_login_user_redirects_to_login(self):
        self.test_client.logout()
        response = self.test_client.get(f'/accounts/login/')
        self.assertTemplateUsed(response, 'account_templates/user_login.html')
