from django.contrib import admin
from .models import Pais, Estado, Cidade


# Register your models here
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['nome']


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 0


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']
    inlines = [CidadeInline]
