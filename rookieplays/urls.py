"""Defines URL patterns for Rookieplay App document analytics functionality"""

from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'rookieplays'
urlpatterns = [
    # Home page
    url(r'^$', views.upload, name='upload'),

    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #Page for adding a new entity
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    #Upload page.
    # path('upload/', views.upload, name='upload')
]
