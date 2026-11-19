
from django.db import models


class PublicacaoTransparencia(models.Model):

    CATEGORIAS = [
        ('financeiro', 'Recursos financeiros'),
        ('maquinario', 'Maquinários agrícolas'),
        ('implemento', 'Implementos agrícolas'),
        ('equipamento', 'Equipamentos'),
        ('prestacao', 'Prestação de contas'),
    ]

    titulo = models.CharField(max_length=200)

    categoria = models.CharField(
        max_length=30,
        choices=CATEGORIAS
    )

    descricao = models.TextField()

    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )

    data_recebimento = models.DateField(
        blank=True,
        null=True
    )

    orgao_responsavel = models.CharField(
        max_length=200,
        blank=True
    )

    documento = models.FileField(
        upload_to='transparencia/',
        blank=True,
        null=True
    )

    data_publicacao = models.DateTimeField(
        auto_now_add=True
    )

    publicado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = 'Publicação de Transparência'
        verbose_name_plural = 'Publicações de Transparência'

    def __str__(self):
        return self.titulo
