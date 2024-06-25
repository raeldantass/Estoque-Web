from django.forms import ModelForm, Select, TextInput
from .models import Entradas

class EntradaForm(ModelForm):
    class Meta:
        model = Entradas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {'produto': Select(attrs={'style': 'width: 100%;'}),
                   'quantidade':TextInput(attrs={'class':'valores', 'style':'width:100%'}),
                   'preco':TextInput(attrs={'class':'valores', 'style':'width:100%'}),
}