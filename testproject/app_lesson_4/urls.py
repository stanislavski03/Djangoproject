from django.urls import path
from .views import view

urlpatterns = [
    path('lesson_4/', view),
]