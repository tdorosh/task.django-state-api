from django.urls import path

from .views import RandomStateAPIView


urlpatterns = [
    path('random/', RandomStateAPIView.as_view(), name='random-state'),
]
