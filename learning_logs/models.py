from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    '''um assunto sobre o qual o usuário está aprendendo'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''devolve uma representação em string do modelo (tabela)'''
        return self.text

class Entry(models.Model):
    '''pode ter várias entry para 1 tópico'''
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...' # retorna apenas os 50 primeiro caracteres
 