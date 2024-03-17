from django.urls import path
from .views import EventListView, EventCreateView, EventRetrieveUpdateDestroy, EventDetailView

app_name = 'unique_admin_namespace'

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('create_event/', EventCreateView.as_view(), name='create-event'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroy.as_view(), name='event-retrieve-update-destroy'),
    path('events_detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]

