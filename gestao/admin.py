from django.contrib import admin
from . models import Abastecimento



class AbastecimentoAdmin(admin.ModelAdmin):
	list_display = ("veiculo","data","id","valor_gasto")
	search_fields = ("data","id")
	date_hierarchy = "data"
	ordering = ("-id",)
	raw_id_fields = ("veiculo",)
	

	
admin.site.register(Abastecimento,AbastecimentoAdmin)


"""
class BookAdmin(admin.ModelAdmin):
	list_display = ("title","publisher","publication_date")
	list_filter = ("publication_date",)	
	search_fields = ("title",)
	date_hierarchy = 'publication_date'
	ordering = ("-publication_date",)
	fields = ('title', 'authors', 'publisher', 'publication_date','num_pages')
	filter_horizontal = ("authors",)
	raw_id_fields = ('publisher',)
"""	
