from django.shortcuts import render, redirect
from .models import Saidas
from .forms import SaidaForm

def list_saida(request):
    saidas = Saidas.objects.all()
    template_name = 'list_saida.html'
    context = {
        'saidas': saidas,
    }
    return render(request, template_name, context)

def new_saida(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade - form.cleaned_data['quantidade']
            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()
            form.save()
            
            return redirect('saida:list_saida')
    else:
        
        template_name = 'new_saida.html'
        context = {
            'form': SaidaForm(),
        }
        
        return render(request, template_name, context)

def update_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    quantidade = saida.quantidade
    print('==> ', quantidade)
    if request.method == 'POST':
        form = SaidaForm(request.POST, instance=saida)
        if form.is_valid():
            print('===> ', quantidade, form.cleaned_data['quantidade'])
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade + quantidade - form.cleaned_data['quantidade']
            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('saida:list_saida')
    else:
        template_name = 'update_saida.html'
        context = {
            'form': SaidaForm(instance=saida),
            'pk': pk,
        }
        return render(request, template_name, context)
    
def delete_saida(request, pk):
    
    saida = Saidas.objects.get(pk=pk)
    saida.produto.quantidade = saida.produto.quantidade + saida.quantidade
    saida.produto.save()
    saida.delete()
    
    return redirect('saida:list_saida')

