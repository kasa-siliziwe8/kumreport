from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_report, name='track_report'),
]
