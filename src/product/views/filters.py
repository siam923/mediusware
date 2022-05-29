import django_filters
from product.models import Product, ProductVariantPrice, ProductVariant

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    price_to = django_filters.NumberFilter(field_name='variant__price', lookup_expr='gt', label='price_to')
    price_from = django_filters.NumberFilter(field_name='variant__price', lookup_expr='lt', label='price_from')
    productVariant = django_filters.ModelChoiceFilter(queryset=ProductVariant.objects.all(), label='variant')
    date = django_filters.DateFilter(field_name='created_at', lookup_expr='contains', label='Date')

    class Meta:
        model = Product
        fields = {}
