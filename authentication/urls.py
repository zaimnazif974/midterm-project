from django.urls import path
from authentication.views import register, login_user, logout_user

app_name = 'authentication'

urlpatterns = [
    path('', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout')
]