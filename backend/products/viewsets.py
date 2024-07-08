from rest_framework import viewsets

from .models import Product
from .serializers import ProductSeralizer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> queryset
    get -> retrieve -> Product instance detail view
    post -> create new instance
    put -> update
    patch -> partial update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    lookup_field = 'pk' #default
    