from rest_framework import generics

from .models import Product
from .serializers import ProductSeralizer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    #lookup_field = "pk"
    