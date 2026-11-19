from django.shortcuts import render
from django.db.models import Q
from .models import PublicacaoTransparencia

def home(request):
    ultimas_publicacoes = PublicacaoTransparencia.objects.filter(
        publicado=True
    ).order_by('-id')[:3]

    return render(
        request,
        'institucional/home.html',
        {'ultimas_publicacoes': ultimas_publicacoes}
    )

def transparencia(request):
    publicacoes = PublicacaoTransparencia.objects.filter(publicado=True)

    categoria = request.GET.get('categoria')
    busca = request.GET.get('busca')

    if categoria:
        publicacoes = publicacoes.filter(categoria=categoria)

    if busca:
        publicacoes = publicacoes.filter(
            Q(titulo__icontains=busca) | Q(descricao__icontains=busca)
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
