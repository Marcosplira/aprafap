
from django.contrib import admin
from .models import PublicacaoTransparencia

@admin.register(PublicacaoTransparencia)
class PublicacaoTransparenciaAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'categoria',
        'orgao_responsavel',
        'data_recebimento',
        'publicado',
    )

    list_filter = (
        'categoria',
        'publicado',
        'data_publicacao',
    )

    search_fields = (
        'titulo',
        'descricao',
        'orgao_responsavel',
    )

    list_editable = ('publicado',)

    readonly_fields = ('data_publicacao',)

    fieldsets = (
        ('Informações da publicação', {
            'fields': (
                'titulo',
                'categoria',
                'descricao',
            )
        }),
        ('Dados do recebimento', {
            'fields': (
                'valor',
                'data_recebimento',
                'orgao_responsavel',
            )
        }),
        ('Documentação', {
            'fields': ('documento',)
        }),
        ('Publicação', {
            'fields': (
                'publicado',
                'data_publicacao',
            )
        }),
    )