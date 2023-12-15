from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    Tarefa = models.CharField(max_length=100)
    Descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    Data_tarefa = models.DateTimeField(verbose_name='Data da Tarefa')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data do Registro')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        db_table = 'Tarefas_agendadas'
    
    def __str__(self):
        return self.Tarefa
