from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return HttpResponse('<h1>Esta é a página inicial</h1>')
