"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
    # detail page for a single topic
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]