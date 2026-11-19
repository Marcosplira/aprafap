
from django.shortcuts import render
from .models import PublicacaoTransparencia

def home(request):
    return render(request, 'institucional/home.html')

def transparencia(request):
    publicacoes = PublicacaoTransparencia.objects.filter(
        publicado=True
    )

    categoria = request.GET.get('categoria')
    busca = request.GET.get('busca')

    if categoria:
        publicacoes = publicacoes.filter(
            categoria=categoria
        )

    if busca:
        publicacoes = publicacoes.filter(
            titulo__icontains=busca
        ) | publicacoes.filter(
            descricao__icontains=busca
        )

    return render(
        request,
        'institucional/transparencia.html',
        {
            'publicacoes': publicacoes,
            'categorias': PublicacaoTransparencia.CATEGORIAS,
            'categoria_atual': categoria or '',
            'busca_atual': busca or '',
        }
    )
