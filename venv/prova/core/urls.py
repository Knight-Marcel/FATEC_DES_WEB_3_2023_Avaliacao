from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro),
    path('listar/', views.index, name='listar')
]