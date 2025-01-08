from django.contrib import admin
from .models import Cliente, ContaPagar, ContaAReceber

admin.site.register(Cliente)
admin.site.register(ContaPagar)
admin.site.register(ContaAReceber)
admin.site.site_header = "Administração do Sistema ERP"
admin.site.site_title = "Painel Administrativo"
admin.site.index_title = "Bem-vindo ao Painel de Administração"