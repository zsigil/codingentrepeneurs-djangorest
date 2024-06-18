from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSeralizer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        # adding data through serializer 
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


#not used any more
class ProductListAPIView(generics.ListAPIView):
    '''
    not used view because we used ListCreate
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    #lookup_field = "pk"
    


#not used any more
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
        # get request -> detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSeralizer(obj, many=False).data
            return Response(data)
        
        # list -> list view
        queryset = Product.objects.all()
        data = ProductSeralizer(queryset, many=True).data
        return Response(data)

    if method== "POST":
        #create an item
        serializer  = ProductSeralizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "bad data"}, status=400)