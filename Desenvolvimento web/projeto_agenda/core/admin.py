from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('Tarefa', 'Data_tarefa', 'data_criacao')
    list_filter = ('Data_tarefa',)

# Register your models here.
admin.site.register(Evento, EventoAdmin)


