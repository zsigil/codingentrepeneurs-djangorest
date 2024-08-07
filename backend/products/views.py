from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

from .models import Product
from .serializers import ProductSeralizer


class ProductListCreateAPIView(StaffEditorPermissionMixin,UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        #print(serializer.validated_data)
        # adding data through serializer 
        email = serializer.validated_data.pop('email')  #email is not in the model!, we have to pop
        #print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=user)
    

#not used any more
class ProductListAPIView(generics.ListAPIView):
    '''
    not used view because we used ListCreate
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer


class ProductDetailAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    #lookup_field = "pk"
    

class ProductUpdateAPIView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
    

class ProductDeleteAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    #lookup_field = "pk"


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    lookup_field = 'pk' #you only have to declare this if you want to change that
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)


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