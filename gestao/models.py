from django.db import models

from cadastro.models import Veiculo




# Create your models here.

class Abastecimento (models.Model):
	veiculo = models.ForeignKey(Veiculo)
	data = models.DateField()
	valor_gasto = models.DecimalField(max_digits=5, decimal_places=2, default = "100,00", verbose_name="valor gasto(R$)")
