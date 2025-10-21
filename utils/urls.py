from django.urls import path
from .views import (HomepageStatsAPIView, FooterStatsAPIView,
                    SocialMediaAPIView, LocationAPIView, PhoneNumberAPIView, EmailAPIView, WorkTimeAPIView)

urlpatterns = [
    path('homepage-stats/', HomepageStatsAPIView.as_view(), name='homepage_stats'),
    path('footer-stats/', FooterStatsAPIView.as_view(), name='footer_stats'),
    path('social-media/', SocialMediaAPIView.as_view(), name='social_media'),
    path('location/', LocationAPIView.as_view(), name='location'),
    path('phonenumber/', PhoneNumberAPIView.as_view(), name='phone_number'),
    path('email/', EmailAPIView.as_view(), name='email'),
    path('worktime/', WorkTimeAPIView.as_view(), name='worktime'),
]
