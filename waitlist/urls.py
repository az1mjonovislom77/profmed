from django.urls import path
from .views import (WaitListAPIView)

urlpatterns = [
    path('waitlist/', WaitListAPIView.as_view(), name='wait-list'),
]
