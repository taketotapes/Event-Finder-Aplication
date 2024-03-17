from django.urls import path
from .views import ReviewListCreate, ReviewRetrieveUpdateDestroy

urlpatterns = [
    path('reviews/', ReviewListCreate.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroy.as_view(), name='review-detail')
]
