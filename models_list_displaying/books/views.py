from django.views import generic
from books.models import Book
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'

    def get_queryset(self):
        if not self.kwargs:
            return Book.objects.order_by('pub_date')
        return Book.objects.filter(pub_date=self.kwargs['pub_date'])

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        if self.kwargs:
            prev_books = Book.objects.filter(pub_date__lt=self.kwargs['pub_date']).order_by('-pub_date')
            if prev_books.exists():
                prev_date = str(prev_books[0].pub_date)
            else:
                prev_date = None
            context['prev_date'] = prev_date

            next_books = Book.objects.filter(pub_date__gt=self.kwargs['pub_date']).order_by('pub_date')
            if next_books.exists():
                next_date = str(next_books[0].pub_date)
            else:
                next_date = None
            context['next_date'] = next_date

        return context
