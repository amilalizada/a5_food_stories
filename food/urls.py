"""
URL configuration for food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from core.views import home, contact
from story.views import recipes, recipe, like_recipe, get_liked
from authentication.views import register, login, logout, user_profile, activate
from food import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('recipes/', recipes, name='recipes'),
    path('liked-recipes/', get_liked, name='liked_recipes'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe_single'),
    path('like_recipe/<int:pk>/', like_recipe, name='recipe_like'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
    path('social-auth/', include('social_django.urls', namespace="social")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
