from django.shortcuts import render

# Create your views here.

def bonjour(request):
    return render(request,"myfirstapp/bonjour.html")

def saisie(request):
    return render(request,"myfirstapp/saisie.html")

def traitement(request):
    nom = request.GET["nom"]
    return render(request,"myfirstapp/traitement.html", {"nom":nom})
