from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSeralizer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'url',
            'pk',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)