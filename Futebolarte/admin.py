from django.contrib import admin
from .models import Clube, Jogador
from cadastros_comuns.models import Cidade
from django.utils.html import format_html


# Register your models here.
class JogadorInline(admin.TabularInline):
    model = Jogador
    extra = 0


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    search_fields = ['nome']


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['escudo_img', 'nome', 'cidade', 'fundacao', 'divisao', 'ver_detalhes']
    list_display_links = ['nome', 'ver_detalhes']
    list_filter = ['divisao']
    search_fields = ['nome', 'cidade__nome']
    inlines = [JogadorInline]


    @admin.display(description='Escudo')
    def escudo_img(self, obj):
        url = 'Não possui'

        if (obj.escudo):
            url = obj.escudo.url
    
        return format_html(f'<img src="{url}" style="max-width:80px; max-height:80px"/>')
    
                       
    def ver_detalhes(self, obj):
        return format_html("<p style='color: blue'>Ver Detalhes</p>")