from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher/<int:pk>/', views.teacher_view, name='teacher'),
]
