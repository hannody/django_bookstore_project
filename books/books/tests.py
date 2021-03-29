# /books/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTest(TestCase):
    bookTitle = "Harry Potter"
    bookAuthor = "JK Rowling"
    bookPrice = "25.00"
    desiredResponseCode = 200
    noResponse_status_code= 404
    list_view_template = 'books/book_list.html'
    detail_view_template = 'books/book_detail.html'


    def setup(self):
        self.book = Book.objects.create(
            title= self.bookTitle,
            author= self.bookAuthor,
            price= self.bookPrice
        )

    # 1- Book listing
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', self.bookTitle)
        self.assertEqual(f'{self.book.author}', self.bookAuthor)
        self.assertEqual(f'{ self.book.price}', self.bookPrice)

    # 2- Book list view
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, self.desiredResponseCode)
        self.assertContains(response, self.bookTitle)
        self.assertTemplateUsed(response, template_name= self.list_view_template)

    # 3- Book detail view
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, self.desiredResponseCode)
        self.assertEqual(no_response.status_code, self.noResponse_status_code)
        self.assertContains(response, self.bookTitle)
        self.assertTemplateUsed(response, self.detail_view_template )

