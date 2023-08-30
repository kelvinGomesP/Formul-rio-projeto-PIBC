from django import forms
from .models import  Aluno, Responsavel


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['Autorizo', 'Nome', 'Matrícula', 'Sexo' ,  'Renda_Própria', 'Mora_Com_Pais', 'Trabalha', 'Quantidade_Filhos', 'Raca', 'Estado_Civil']
        exclude = ['Responsável']
        widgets = {
           # 'Data_Nascimento': forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/aaaa'}),
            'Matricula': forms.NumberInput(attrs={'min': 1000000, 'max': 9999999}),
        }
    def clean_matricula(self):
        matricula = self.cleaned_data['Matricula']
        if len(str(matricula)) != 7:
            raise forms.ValidationError('A Matrícula deve conter exatamente 7 dígitos.')
        return matricula

class ResponsavelForm(forms.ModelForm):
    
    class Meta:
        model = Responsavel
        fields = '__all__'