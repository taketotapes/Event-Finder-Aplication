from django.urls import path
from .views import TicketListView, TicketCreateView, TicketDetailView

app_name = 'unique_admin_namespace'

urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='tickets-list'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]
