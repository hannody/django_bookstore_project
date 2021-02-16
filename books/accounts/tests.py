from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

# Create your tests here.
from accounts.forms import CustomUserCreationForm
from accounts.views import SignupPageView


class CustomUserTests(TestCase):
    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create(
            username='testUserName', 
            email='test@email.com', 
            password='Q1w2e3r4'
        )

        self.assertEqual(user.username, 'testUserName')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        user_model = get_user_model()
        admin_user = user_model.objects.create_superuser(
            username='superadmin',
            email= 'superadmin@email.com',
            password = 'Q1w2e3r4'
        )

        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')


    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )