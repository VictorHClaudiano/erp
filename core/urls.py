from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar-clientes/', views.listar_clientes, name='listar_clientes'),
    path('cadastrar-cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('excluir-cliente/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    
    # URLs para Contas a Pagar e Receber
    path('contas-pagar/', views.listar_contas_pagar, name='listar_contas_pagar'),
    path('contas_pagar/cadastrar/', views.cadastrar_conta_pagar, name='cadastrar_conta_pagar'),
    path('contas_pagar/excluir/<int:conta_id>/', views.excluir_conta_pagar, name='excluir_conta_pagar'),
    path('contas_pagar/editar/<int:conta_id>/', views.editar_conta_pagar, name='editar_conta_pagar'),

    path('contas-receber/', views.listar_contas_receber, name='listar_contas_receber'),
    path('contas-receber/cadastrar/', views.cadastrar_conta_receber, name='cadastrar_conta_receber'),
    path('contas-receber/excluir/<int:conta_id>/', views.excluir_conta_receber, name='excluir_conta_receber'),
    path('contas-receber/editar/<int:conta_id>/', views.editar_conta_receber, name='editar_conta_receber'),

    path('listar-estoque/', views.listar_estoque, name='listar_estoque'),
    path('estoque/cadastrar/', views.cadastrar_estoque, name='cadastrar_estoque'),
    path('estoque/excluir/<int:item_id>/', views.excluir_estoque, name='excluir_estoque'),
    path('estoque/editar/<int:item_id>/', views.editar_estoque, name='editar_estoque'),
]

