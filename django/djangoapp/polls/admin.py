from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin): 
    fields = ["pub_date", "question_text"] #el orden en que se muestran los campos en el admin
    inLines = [ChoiceInLine] #los campos que se muestran en el admin


# Register your models here.
admin.site.register(Question, QuestionAdmin) #registramos la clase Question en el admin
#admin.site.register(Choice) #regisxtramos las clases Question y Choice en el admin de django