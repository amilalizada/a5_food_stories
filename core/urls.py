from django.urls import path
from core.views import home, ContactView, contact

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]