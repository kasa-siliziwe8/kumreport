from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_submission, name='report_submission'),
]
