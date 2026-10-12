from django.contrib import admin
from django.urls import path
from .views import BookView,UpdateView

urlpatterns = [
    path('books/',BookView.as_view()),
    path('books/update/<int:pk>/',UpdateView.as_view()),
]
