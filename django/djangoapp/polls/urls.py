# archivo que está dentro de polls 
# urls.py
from django.urls import path
#importar la vista de views.py que está dentro de polls
from . import views

urlpatterns = [ #lista de urls
path("", views.index, name="index") #path vacío, la vista que se va a ejecutar, nombre de la vista
]
#esta vacio porque es la raiz de la app, si fuera polls/1/ sería polls/1/, polls/2/, etc...
