from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSeralizer(serializers.ModelSerializer):
    update_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')

    class Meta:
        model = Product
        fields = [
            'url',
            'update_url',
            'pk',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]

    def get_update_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk":obj.pk}, request=request)