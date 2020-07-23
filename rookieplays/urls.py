"""Defines URL patterns for rookieplays"""

from django.urls import paths
from . import views

app_name = 'rookieplays'
urlpatterns = [
# Home page
path('', views.index, name='index'),
]
