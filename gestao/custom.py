from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg
 
from . models import Abastecimento
 
class TotalAveragesChangeList(ChangeList):
    #provide the list of fields that we need to calculate averages and totals
    fields_to_total = ['valor_gasto',]
 
 
 
    def get_total_values(self, queryset):
        """
        Get the totals
        """
        #basically the total parameter is an empty instance of the given model
        total =  Abastecimento()
        total.custom_alias_name = "Totals" #the label for the totals row
        for field in self.fields_to_total:
            setattr(total, field, queryset.aggregate(Sum(field)).items()[0][1])
        return total
 
 
    def get_average_values(self, queryset):
        """
        Get the averages
        """
        average =  Abastecimento()
        average.custom_alias_name = "Averages" #the label for the averages row
 
        for field in self.fields_to_total:
            setattr(average, field, queryset.aggregate(Avg(field)).items()[0][1])
        return average
 
 
    def get_results(self, request):
        """
        The model admin gets queryset results from this method
        and then displays it in the template
        """
        super(TotalAveragesChangeList, self).get_results(request)
        #first get the totals from the current changelist
        total = self.get_total_values(self.query_set)
        #then get the averages
        average = self.get_average_values(self.query_set)
        #small hack. in order to get the objects loaded we need to call for 
        #queryset results once so simple len function does it
        len(self.result_list)
        #and finally we add our custom rows to the resulting changelist
        self.result_list._result_cache.append(total)
        self.result_list._result_cache.append(average)
