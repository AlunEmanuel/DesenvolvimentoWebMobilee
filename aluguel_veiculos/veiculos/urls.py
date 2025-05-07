from django.urls import path
from . import views

app_name = 'veiculos'  # Namespace para evitar conflitos de nomes de rotas

urlpatterns = [
    path('', views.listar_veiculos, name='listar'),  # Lista de veículos
    path('criar/', views.criar_veiculo, name='criar'),  # Criar um novo veículo
    path('editar/<int:pk>/', views.editar_veiculo, name='editar'),  # Editar veículo
    path('deletar/<int:pk>/', views.deletar_veiculo, name='deletar'),  # Deletar veículo
]