from django.test import TestCase
from users.forms import CustomUserCreationForm


class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = CustomUserCreationForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
