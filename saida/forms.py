from django.forms import ModelForm, Select, Textarea, TextInput
from .models import Saidas

class SaidaForm(ModelForm):
    class Meta:
        model = Saidas
        fields = [
            'produto', 'quantidade', 'preco'
            ]
        widgets = {'produto': Select(attrs={'style': 'width: 100%;'}),
                   'quantidade':TextInput(attrs={'class':'valores', 'style':'width:100%'}),
                   'preco':TextInput(attrs={'class':'valores', 'style':'width:100%'}),
}