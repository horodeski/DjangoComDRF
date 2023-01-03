from django.contrib import admin

from core.models import Autor, Compra, Livro, Categoria, Editora

admin.site.register(Compra)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Autor)