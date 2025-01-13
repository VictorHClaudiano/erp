# Generated by Django 5.1.4 on 2025-01-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vencimento', models.DateField()),
                ('tipo', models.CharField(choices=[('pagar', 'Conta a Pagar'), ('receber', 'Conta a Receber')], max_length=10)),
                ('pago', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='ContaPagar',
        ),
        migrations.DeleteModel(
            name='ContaReceber',
        ),
    ]