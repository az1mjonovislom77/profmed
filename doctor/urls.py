from django.urls import path
from .views import (DoctorAPIView)

urlpatterns = [
    path('doctors/', DoctorAPIView.as_view(), name='doctors_list'),
    # path('detail/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctors_detail')

]
