from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("authors", views.add_authors),
    path("add_book", views.add_book),
    path("add_author", views.add_author),
    path("books/<int:id>", views.book_display),
    path("authors/<int:id>", views.authors_info),
    path("addbookauthor/<int:id>", views.addbookauthor),
    path("addauthorbook/<int:id>", views.addauthorbook),


]
