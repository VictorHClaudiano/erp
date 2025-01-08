from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome

class ContaPagar(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao


class ContaAReceber(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descricao} - {self.valor} - {'Pago' if self.pago else 'Pendente'}"
