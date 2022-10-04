from django.contrib import admin
from .models import Question, Choice

# Register your models here.
admin.site.register(Question) #registramos la clase Question en el admin
admin.site.register(Choice) #registramos las clases Question y Choice en el admin de django