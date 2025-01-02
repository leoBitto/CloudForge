# backoffice/urls.py
from django.urls import path
from .views import BackofficeView

app_name = 'backoffice'

urlpatterns = [
    path('', BackofficeView.as_view(), name='backoffice'),
]