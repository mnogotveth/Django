from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View
from .models import Book


def first(request) :
    return HttpResponse('Hello World')

class Second(View):
    def get(self, request):
        return HttpResponse(self.output)

    # books = Book.objects.all()
    # books = Book.objects.filter(is_published = True)
    book = Book.objects.get(id = 1)

    output = ''

    # for book in books:
    #     output += (f'We have {book.title} with ID {book.id} in our Database<br>')

    output = (f'We have {book.title} with ID {book.id} in our Database<br>')
