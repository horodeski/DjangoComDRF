from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):  # hermosa CRUD completa
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
