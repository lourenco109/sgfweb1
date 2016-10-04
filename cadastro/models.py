from django.db import models

# Create your models here.
class Veiculo(models.Model):
	veiculo = models.CharField(max_length=20)
	placa = models.CharField(max_length=20)
	
	def __str__(self):
		return self.veiculo