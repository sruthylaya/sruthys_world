from django.urls import path
from . import views

urlpatterns = [
    path('theme/', views.theme, name='theme')
]
