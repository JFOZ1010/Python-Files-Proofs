from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

#esta es una function based views, el index es la vista general. 
"""
def index(request):
    latest_question_list = Question.objects.all()
    #return HttpResponse("Estás en la pagina principal de Polls.")
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list}) #renderiza el template index.html, que está dentro de la carpeta polls, y le pasa como contexto la variable latest_question_list

def detail(request, question_id): #definimos la función detail, que recibe como parámetro el request y el question_id, para que nos devuelva el detalle de la pregunta
    #question = Question.objects.get(pk=question_id) #obtenemos la pregunta que tiene el id que le pasamos
    question = get_object_or_404(Question, pk=question_id) #si no encuentra la pregunta, devuelve un 404
    return render(request, "polls/detail.html", {
        "question": question
    })


def results(request, question_id): #esta es para ver la cantidad de votos que tiene cada pregunta
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {
        "question": question #esta es la pregunta que se va a mostrar
        })

def vote(request, question_id): #esta es para votar
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1 #incrementa el número de votos, para que se guarde en la base de datos
        selected_choice.save() #guarda los cambios en la base de datos
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) #redirige a la vista results, con el id de la pregunta que se votó
"""
#esta es una class based views, el index es la vista general.

class IndexView(generic.ListView):
    template_name = "polls/index.html" #el template que va a usar
    context_object_name = "latest_question_list" #esta es la vista para ver el detalle de la pregunta

    def get_queryset(self): #este metodo es para obtener el queryset, que es la lista de objetos que se va a mostrar
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5] #devuelve las últimas 5 preguntas

class DetailView(generic.DetailView):
    model = Question #el modelo que va a usarse
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"

def vote(request, question_id): #esta es para votar
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        
    except (KeyError):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# Create your views here.














