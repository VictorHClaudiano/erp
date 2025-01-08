from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, ContaPagar, ContaAReceber
from django.contrib import messages


def index(request):
    return render(request, 'core/index.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/listar_clientes.html', {'clientes': clientes})

def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if not (nome and email and telefone):
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'core/cadastrar_cliente.html')

        # Criar cliente no banco de dados
        Cliente.objects.create(nome=nome, email=email, telefone=telefone)
        messages.success(request, "Cliente cadastrado com sucesso!")
        return redirect('listar_clientes')

    return render(request, 'core/cadastrar_cliente.html')

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if not (nome and email and telefone):
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'core/editar_cliente.html', {'cliente': cliente})

        # Atualizar os dados do cliente
        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        cliente.save()

        messages.success(request, "Cliente atualizado com sucesso!")
        return redirect('listar_clientes')

    return render(request, 'core/editar_cliente.html', {'cliente': cliente})

def excluir_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.delete()
        messages.success(request, "Cliente excluído com sucesso!")
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado!")

    return redirect('listar_clientes')

# Criar conta a pagar
def listar_contas_pagar(request):
    contas = ContaPagar.objects.all()
    return render(request, 'core/listar_contas_pagar.html', {'contas': contas})

def cadastrar_conta_pagar(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        vencimento = request.POST.get('vencimento')
        pago = request.POST.get('pago') == "on"

        if not (descricao and valor and vencimento):
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'core/cadastrar_conta_pagar.html')

        # Criar uma nova conta a pagar no banco de dados
        ContaPagar.objects.create(descricao=descricao, valor=valor, vencimento=vencimento, pago=pago)
        messages.success(request, "Conta a pagar cadastrada com sucesso!")
        return redirect('listar_contas_pagar')

    return render(request, 'core/cadastrar_conta_pagar.html')

def excluir_conta_pagar(request, conta_id):
    try:
        conta = ContaPagar.objects.get(id=conta_id)
        conta.delete()
        messages.success(request, "Conta excluída com sucesso!")
    except ContaPagar.DoesNotExist:
        messages.error(request, "Conta não encontrada!")

    return redirect('listar_contas_pagar')

def editar_conta_pagar(request, conta_id):
    conta = get_object_or_404(ContaPagar, id=conta_id)

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        vencimento = request.POST.get('vencimento')
        pago = request.POST.get('pago') == "on"

        if not (descricao and valor and vencimento):
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'core/editar_conta.html', {'conta': conta})

        # Atualizar os dados da conta
        conta.descricao = descricao
        conta.valor = valor
        conta.vencimento = vencimento
        conta.pago = pago
        conta.save()

        messages.success(request, "Conta atualizada com sucesso!")
        return redirect('listar_contas_pagar')

    return render(request, 'core/editar_conta.html', {'conta': conta})

def listar_contas_receber(request):
    contas = ContaAReceber.objects.all()
    return render(request, 'core/listar_contas_receber.html', {'contas': contas})

def cadastrar_conta_receber(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        vencimento = request.POST.get('vencimento')
        pago = request.POST.get('pago') == "on"

        if not (descricao and valor and vencimento):
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'core/cadastrar_conta_receber.html')

        # Criar uma nova conta a receber no banco de dados
        ContaAReceber.objects.create(descricao=descricao, valor=valor, vencimento=vencimento, pago=pago)
        
        messages.success(request, "Conta a receber cadastrada com sucesso!")
        
        # Redirecionar para a lista de contas a receber
        return redirect('listar_contas_receber')

    return render(request, 'core/cadastrar_conta_receber.html')

def excluir_conta_receber(request, conta_id):
    try:
        conta = ContaAReceber.objects.get(id=conta_id)
        conta.delete()
        messages.success(request, "Conta excluída com sucesso!")
    except ContaAReceber.DoesNotExist:
        messages.error(request, "Conta não encontrada!")

    return redirect('listar_contas_receber')  # Redireciona para a lista de contas a receber

def editar_conta_receber(request, conta_id):
    conta = get_object_or_404(ContaAReceber, id=conta_id)

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        vencimento = request.POST.get('vencimento')
        pago = request.POST.get('pago') == "on"

        if not (descricao and valor and vencimento):
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'core/editar_conta_receber.html', {'conta': conta})

        # Atualizar os dados da conta
        conta.descricao = descricao
        conta.valor = valor
        conta.vencimento = vencimento
        conta.pago = pago
        conta.save()

        messages.success(request, "Conta atualizada com sucesso!")
        return redirect('listar_contas_receber')  # Redireciona para a lista de contas a receber

    return render(request, 'core/editar_conta_receber.html', {'conta': conta})