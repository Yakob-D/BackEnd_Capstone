from django.urls import path
from .views import CreateEventView, ListEventsView, UpdateEventView, DeleteEventView

urlpatterns = [
    #path for GET request to list events
    path('/', ListEventsView.as_view(), name='event-list'),
    #path for POST request to create an event
    path('create', CreateEventView.as_view(), name='event-create'),
    #path for PUT request to update an event with an id
    path('update/<int:pk>', UpdateEventView.as_view(), name='event-update'),
    #path for DELETE request to delete an event with an id
    path('delete/<int:pk>', DeleteEventView.as_view(), name='event-delete'),
]