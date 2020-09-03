"""Defines URL patterns for Rookieplay App document analytics functionality"""

from django.conf.urls import url
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rookieplays'
urlpatterns = [
    # Home page
    # path('', views.upload, name='index'),
    # path('', views.index, name='index'),

    path('', views.upload, name='upload'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    #Page for adding a new entity
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    #Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    path('documents/<int:pk>/', views.delete_document, name='delete_document'),

    #Upload page.
    # path('upload/', views.upload, name='upload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
