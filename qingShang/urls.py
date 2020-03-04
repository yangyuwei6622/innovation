from django.urls import path
from qingShang import views

urlpatterns = [
    path('register/', views.register),
    path('register_handle/',views.register_handle),
    path('login/',views.login),
]