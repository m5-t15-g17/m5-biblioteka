from django.urls import path
from . import views

urlpatterns = [
    path("loan/copy/<int:pk>", views.LoanView.as_view()),
]