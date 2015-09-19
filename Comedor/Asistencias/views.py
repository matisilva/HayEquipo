from django.shortcuts import render
#For render
from django.http import HttpResponse
from django.shortcuts import render
#For manage of data
from models import Asistencia


# Create your views here.
def index(request):
    latest_asistencias = Asistencia.objects.order_by('-A_fecha')
    context = {'latest_asistencias': latest_asistencias}
    return render(request, 'Asistencias/index.html', context)

def details(request, A_id):
    return HttpResponse("Detalles de la asistencia: %s" % A_id)
