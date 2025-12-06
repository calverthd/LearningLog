from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # ← new route
    path('contact/', views.contact, name='contact'),  # ← new route
]
