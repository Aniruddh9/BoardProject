from django.urls import resolve, reverse
from django.test import TestCase
from accounts.views import signup
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)

class SuccesfulSignupTest(TestCase):
    def setUp(self):
      url = reverse('signup')
      data = {
	'username' : 'Mike',
        'email' : 'john@gmail.com',
	'password1' : 'abcdef123456',
	'password2' : 'abcdef123456'
	     }
      self.response = self.client.post(url, data)
      self.home_url = reverse('home')

    def test_redirection(self):
      '''
      checks for redirection to home page upon succesful signup.
      '''
      self.assertRedirects(self.response,self.home_url)

    def test_UserCreation(self):
      '''
	checks for sucessful user creation
      '''
      self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
      response = self.client.get(self.home_url)
      user = response.context.get('user')
      self.assertTrue(user.is_authenticated)
