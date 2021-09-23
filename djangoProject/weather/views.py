from django.http import HttpResponse

def index(request):
    return HttpResponse("Hier wird man mal das Wetter sehen können")
