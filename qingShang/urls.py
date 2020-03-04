from django.urls import path
from qingShang import views

urlpatterns = [
    path('register/', views.register),
]