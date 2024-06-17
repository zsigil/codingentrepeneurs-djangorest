from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSeralizer
# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #serialization: model_instance->python dictionary
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSeralizer(instance).data
    return Response(data)
