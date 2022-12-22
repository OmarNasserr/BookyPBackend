from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from ..serializers import PlaygroundSerializer,PlaygroundListAllSerializer
from ..models import Playground
from ..pagination import PlaygroundPagination


class PlaygroundList(generics.ListAPIView):
    serializer_class = PlaygroundListAllSerializer
    queryset = Playground.objects.all()
    
    pagination_class=PlaygroundPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields=['p_name', 'city__city_name','city__governorate',
                     'open_time', 'close_time', 'price_per_hour','id']
    search_fields = ['p_name', 'city__city_name',
                     'open_time', 'close_time', 'price_per_hour','city__governorate__gov_name',]
    
    def get(self, request, *args, **kwargs):
        PlaygroundPagination.set_default_page_number_and_page_size(request)
        return super().get(request, *args, **kwargs)
    
    
