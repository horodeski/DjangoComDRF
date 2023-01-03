from django.contrib import admin

from core.models import Autor, Compra, ItensCompra, Livro, Categoria, Editora

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(ItensCompra)

class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)