from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("loan/copy/<int:pk>/", views.LoanView.as_view()),
    path("loan/<int:pk>/",views.LoanViewUpdate.as_view())
]