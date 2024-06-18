from rest_framework import generics

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
    