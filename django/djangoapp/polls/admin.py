from django.contrib import admin
from .models import Question, Choice
from django import forms
from django.forms.models import BaseInlineFormSet

#esta clase lo que hace es que no se pueda crear una opcion sin texto, es decir, que no se pueda dejar vacio el campo de texto
class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """Check that at least one choice has been entered."""
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
            for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one choice required.')

class ChoiceInLine(admin.TabularInline):
    model = Choice
    formset = AtLeastOneRequiredInlineFormSet
    extra = 1 
    exclude = ['votes']

class QuestionAdmin(admin.ModelAdmin): 

    inlines = (ChoiceInLine, )

    def save_format(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.save()
        form.save()
        formset.save()



    fields = ["question_text", "pub_date"] #el orden en que se muestran los campos en el admin
    inLines = [ChoiceInLine] #los campos que se muestran en el admin
    list_display = ("question_text", "pub_date", "was_published_recently") #los campos que se muestran en el admin
    list_filter = ["pub_date"] #los campos que se muestran en el admin
    search_fields = ["question_text"] #los campos que se muestran en el admin

# Register your models here.
admin.site.register(Question, QuestionAdmin) #registramos la clase Question en el admin
#admin.site.register(Choice) #regisxtramos las clases Question y Choice en el admin de django