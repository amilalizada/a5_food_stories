from django.urls import path
from core.views import home, ContactView, contact, export_view

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('export/', export_view, name='export'),
]