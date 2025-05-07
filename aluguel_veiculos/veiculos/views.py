from django.shortcuts import render, get_object_or_404, redirect
from .models import Veiculo
from .forms import VeiculoForm

def listar_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/listar.html', {'veiculos': veiculos})

def criar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
        else:
            return render(request, 'veiculos/form.html', {'form': form, 'error': form.errors})
    else:
        form = VeiculoForm()
    return render(request, 'veiculos/form.html', {'form': form})

def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
        else:
            return render(request, 'veiculos/form.html', {'form': form, 'error': form.errors})
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculos/form.html', {'form': form})

def deletar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar_veiculos')
    return render(request, 'veiculos/confirmar_deletar.html', {'veiculo': veiculo})

def index(request):
    return render(request, 'veiculos/index.html')