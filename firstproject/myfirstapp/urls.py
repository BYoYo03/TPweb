from django.urls import path
from . import views

urlpatterns = [
    path('bonjour/',views.bonjour),
    path('saisie/',views.saisie),
    path('traitement/',views.traitement),
]