from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.serializers import SerializerMethodField

from core.models import Categoria
from core.models import Editora
from core.models import Autor
from core.models import Livro
from core.models import Compra
from core.models import ItensCompra


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"


class EditoraNestedSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = ("nome",)
    # hermosa maneira de mostrar apenas o que eu quero no get


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
    
        
class LivroDetailSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    editora = EditoraNestedSerializer()
    autores = SerializerMethodField()
    # fea maneira de mostrar apenas o que eu quero no get
    
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
    
    def get_autores(self, instance):
        nomes_autores = []
        autores = instance.autores.get_queryset()
        for autor in autores:
            nomes_autores.append(autor.nome)
        return nomes_autores
        # mostra o nome e não o id


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total")
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco
    # valor total da compra
        

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email")
    status = SerializerMethodField()
    itens = ItensCompraSerializer(many=True)
        
    class Meta:
        model = Compra
        fields = ("id", "status", "usuario", "itens", "total")
        
    def get_status(self, instance):
        return instance.get_status_display()
