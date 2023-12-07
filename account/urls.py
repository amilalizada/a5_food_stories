from django.urls import path
from account.views import register, login, logout

app_name = 'account'
urlpatterns = [
    path('', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]