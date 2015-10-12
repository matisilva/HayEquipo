from django.shortcuts import render
#For render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
#For manage of data
from models import Asistencia
#For forms
from forms import AsistenciaForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.
def index(request):
    latest_asistencias = Asistencia.objects.order_by('-A_fecha')
    context = {'latest_asistencias': latest_asistencias}
    return render(request, 'Asistencias/index.html', context)

def details(request, A_id):
    return HttpResponse("Detalles de la asistencia: %s" % A_id)

def assist(request):
    if request.POST:
        form = AsistenciaForm(request.POST)
        #if is_valid():
        form.save()
        #Save and reload
        return HttpResponseRedirect('/asistencias/')
    else:
        form = AsistenciaForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('Asistencias/crear_asistencia.html', args)
