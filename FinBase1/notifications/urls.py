from django.urls import path
from .views import NotificationListCreate, NotificationRetrieveUpdateDestroy, UnreadNotificationList, MarkAsRead, ClearAllNotifications

urlpatterns = [
    path('notifications/', NotificationListCreate.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationRetrieveUpdateDestroy.as_view(), name='notification-detail'),
    path('notifications/unread/', UnreadNotificationList.as_view(), name='unread-notification-list'),
    path('notifications/<int:pk>/mark-as-read/', MarkAsRead.as_view(), name='mark-as-read'),
    path('notifications/clear-all/', ClearAllNotifications.as_view(), name='clear-all-notifications'),
]