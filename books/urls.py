from django.urls import path
from .views import BookView
from . import views


urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view()),
]
