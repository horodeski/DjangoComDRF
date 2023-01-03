from django.http import HttpResponse

def teste(request):
    return HttpResponse("Olá mundo!")

def teste2(request):
    return HttpResponse("la ele")