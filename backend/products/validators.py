from rest_framework import serializers
from .models import Product


def validate_title(value): #validate_<field_name>
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"Title '{value}' already exists")
    return value