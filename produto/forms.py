from django.forms import ModelForm,Select, Textarea,TextInput
from .models import Produtos

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'cor', 'descricao']
        widgets = {'produto': TextInput(attrs={'style': 'width: 100%;'}),
                   'cor': Select(attrs={'style': 'width: 100%;'}),
                   'descricao': Textarea(attrs={'cols': 200, 'rows': 5, 'style': 'width:100%'}),}