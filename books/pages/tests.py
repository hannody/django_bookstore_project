# pages/tests.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView

existsHttpCode = 200


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, existsHttpCode)

    def test_homepage_url_name(self):
        # reverse which is useful for testing our URLs
        self.assertEqual(self.response.status_code, existsHttpCode)

    # Testing for using the intended template
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):  # new
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):  # new
        self.assertNotContains(self.response,
                               'Hi there! I should not be on the page.')

    # HomePageView “resolves” a given URL path?
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
