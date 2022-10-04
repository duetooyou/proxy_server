from rest_framework import generics
from api.serializers import PetrolSerializer
from store.models import PetrolStore


class PetrolView(generics.ListAPIView):
    serializer_class = PetrolSerializer
    queryset = PetrolStore.objects.all()

    def get_view_name(self):
        return f'Список АЗС'
