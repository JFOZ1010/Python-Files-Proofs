# archivo que está dentro de polls 
# urls.py
# from django.urls import path
#importar la vista de views.py que está dentro de polls
from . import views
from django.urls import path



app_name = "polls"
urlpatterns = [ #lista de urls
#ex: /polls/
path("", views.IndexView.as_view(), name="index"),
#ex: /polls/5/
path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
#ex: /polls/5/results/
path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#ex: /polls/5/vote/
path("<int:question_id>/vote/", views.vote, name="vote"),

#path vacío, la vista que se va a ejecutar, nombre de la vista
]
#esta vacio porque es la raiz de la app, si fuera polls/1/ sería polls/1/, polls/2/, etc...
