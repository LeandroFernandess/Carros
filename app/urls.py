"""
Configuração de URLs para o projeto app.

A lista `urlpatterns` roteia URLs para views. Para mais informações, veja:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Exemplos:
Views baseadas em funções
    1. Adicione um import:  from my_app import views
    2. Adicione uma URL ao urlpatterns:  path('', views.home, name='home')
Views baseadas em classes
    1. Adicione um import:  from other_app.views import Home
    2. Adicione uma URL ao urlpatterns:  path('', Home.as_view(), name='home')
Incluindo outra URLconf
    1. Importe a função include: from django.urls import include, path
    2. Adicione uma URL ao urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import (
    CarsListView,
    NewCarCreateView,
    CarDetailView,
    CarUpdateView,
    CarDeleteView,
)
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("cars/", CarsListView.as_view(), name="cars_list"),
    path("new_car/", NewCarCreateView.as_view(), name="new_car"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("car/<int:pk>/update", CarUpdateView.as_view(), name="car_update"),
    path("car/<int:pk>/delete", CarDeleteView.as_view(), name="car_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
