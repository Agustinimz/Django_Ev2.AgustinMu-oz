from django.shortcuts import render, redirect
from reservas_App.models import reserva
from reservas_App.forms import FormReserva

# Create your views here.
def index(request):
    return render(request,'index.html')

def listaReservas(request):
    reservas = reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reserva.html', data)

def agregarReserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarReserva.html', data)

def eliminarReserva(request, id):
    res = reserva.objects.get(id = id)
    res.delete()
    return redirect('/reserva')

def actualizarReserva(request, id):
    res = reserva.objects.get(id = id)
    form = FormReserva(instance=res)
    if request.method == 'POST':
        form = FormReserva(request.POST, instance=res)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarReserva.html', data)
