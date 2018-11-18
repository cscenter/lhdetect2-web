from django.urls import reverse, resolve
from django.test import TestCase

from users.views import signup
from users.models import CustomUser
from users.forms import CustomUserCreationForm


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_index_view_is_available(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.index_url = reverse('index')

    def test_redirection(self):
        """
        A valid form submission should redirect the user to the home page
        """
        self.assertRedirects(self.response, self.index_url)

    def test_user_creation(self):
        self.assertTrue(CustomUser.objects.exists())

    def test_user_authentication(self):
        """
        Create a new request to an arbitrary page.
        The resulting response should now have `user` in its context after a successful sign up.
        """
        response = self.client.get(self.index_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})

    def test_signup_status_code(self):
        """
        An invalid form submission should return to the same page
        """
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_user_creation(self):
        self.assertFalse(CustomUser.objects.exists())
