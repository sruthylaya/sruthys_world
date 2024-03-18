from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_dream, name='my_dream'),
    path('newborn/', views.newborn, name='newborn'),
    path('accessories/', views.accessories, name='accessories'),
    path('diaper/', views.diaper, name='diaper'),
    path('lactos/', views.lactos, name='lactos'),
    path('toys/', views.toys, name='toys')
]
