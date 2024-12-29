# authentication/urls.py
from django.urls import path
from .views import LoginView, LogoutView, ProtectedView, TokenStatusView

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/protected/', ProtectedView.as_view(), name='protected'),
    path('api/token-status/', TokenStatusView.as_view(), name='token-status'),
]