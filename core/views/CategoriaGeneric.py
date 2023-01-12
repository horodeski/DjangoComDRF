from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Categoria
from core.serializers import CategoriaSerializer

class CategoriasListGeneric(ListCreateAPIView): #get e post 
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' #busca por id
    queryset = Categoria.objects.all() #patch e delete (eu achokk) 
    serializer_class = CategoriaSerializer
