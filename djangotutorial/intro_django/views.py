from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("¡Hola Mundo!")

def hello_bogdan(request, name):
    return HttpResponse(f"Hola, {name}!")

def hello_num(request, name, num):
    # Aquí num llegará como un entero gracias al conversor <int:num>
    return HttpResponse(f"Hola {name}, tu número es {num}")