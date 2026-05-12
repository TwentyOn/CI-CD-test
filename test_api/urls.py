from rest_framework.urls import path

from .views import TestView

urlpatterns = [
    path('', TestView.as_view(), name='test')
]