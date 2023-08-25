from django.shortcuts import render, redirect
from .forms import  AlunoForm, ResponsavelForm
from .models import Aluno, Responsavel


# Create your views here.

def formulario(request):
    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST)
        responsavel_form = ResponsavelForm(request.POST)

        if aluno_form.is_valid() and responsavel_form.is_valid():
            # Salvar o objeto Responsavel separadamente
            responsavel = responsavel_form.save()

            # Criar o objeto Aluno, mas não salvar ainda
            aluno = aluno_form.save(commit=False)

            # Associar o Responsavel ao Aluno
            aluno.responsavel = responsavel

            # Salvar o objeto Aluno agora, pois agora ele tem um Responsavel associado
            aluno.save()

            # Redirecionar para alguma página de sucesso, caso desejado
            return redirect('pagina_de_sucesso')
    else:
        aluno_form = AlunoForm()
        responsavel_form = ResponsavelForm()

    return render(request, 'formulario.html', {
        'aluno_form': aluno_form,
        'responsavel_form': responsavel_form,
    })
    
def pagina_de_sucesso(request):
    return render(request, 'pagina_de_sucesso.html')