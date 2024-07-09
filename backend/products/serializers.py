from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators

class ProductSeralizer(serializers.ModelSerializer):
    update_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')

    email = serializers.EmailField(write_only=True) #won't show up in list, but can be added at creation
    title = serializers.CharField(validators=[validators.unique_product_title])
    name = serializers.CharField(source='title', read_only=True) #identical field to title
    
    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'update_url',
            'email',
            'name',
            'pk',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]

    # def validate_title(self, value): #validate_<field_name>
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"Title '{value}' already exists")
    #     return value



    def create(self, validated_data):
        #we do not do anything, just call super
        obj = super().create(validated_data)
        return obj

    def get_update_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk":obj.pk}, request=request)