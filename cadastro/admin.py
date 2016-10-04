from django.contrib import admin
from . models import Veiculo

class VeiculoAdmin(admin.ModelAdmin):
	list_display = ("veiculo","placa")
	search_fields = ("veiculo","placa")
	ordering = ("veiculo",)
	
# Register your models here.
admin.site.register(Veiculo,VeiculoAdmin)