from rest_framework import mixins, viewsets

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
    

class ProductGenericViewSet(mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin, 
                            viewsets.GenericViewSet):
    '''
    get -> list -> queryset
    get -> retrieve -> Product instance detail view
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    lookup_field = 'pk' #default


#to customize endpoints, use these in urls.py
product_list_view = ProductGenericViewSet.as_view({'get':'list'})
product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})