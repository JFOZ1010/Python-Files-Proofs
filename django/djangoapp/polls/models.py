from django.db import models
import datetime
# Create your models here.

#definimos la primer clase (table), llamada questions {atributos: id, question_text, pub_date}
class Question(models.Model):
    """LA VENTAJA ES QUE DJANGO YA NOS CREA LA LLAVE PRIMARIA, LA HACE POR NOSOTROS"""
    #id = models.AutoField(primary_key=True) #definimos el campo id como autoincremental
    question_text = models.CharField(max_length=200) #definimos el campo question_text como un campo de tipo CharField, con un tamaño máximo de 200 caracteres
    pub_date = models.DateTimeField(auto_now_add=True) #definimos el campo pub_date como un campo de tipo DateTimeField, con una etiqueta 'date published'

    def __str__(self): #definimos el método __str__ para que nos devuelva el valor de la pregunta
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #devuelve True si la fecha de publicación es mayor o igual a la fecha actual menos 1 día


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #definimos el campo question como una llave foránea de la tabla Question, cada vez que se elimine un registro de la tabla Question, se eliminarán todos los registros de la tabla Choices que tengan como llave foránea el id de la tabla Question
    choice_text = models.CharField(max_length=200) #definimos el campo choice_text como un campo de tipo CharField, con un tamaño máximo de 200 caracteres
    votes = models.IntegerField(default=0) #definimos el campo votes como un campo de tipo IntegerField, con un valor por defecto de 0

    def __str__(self): #definimos el método __str__ para que nos devuelva el valor de la pregunta
        return self.choice_text
    