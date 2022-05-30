from django.views import generic
from django.shortcuts import render, reverse
from product.models import Product, Variant, ProductVariantPrice, ProductVariant
from .filters import ProductFilter
from django.db.models import Q


class CreateProductView(generic.CreateView):
    template_name = 'products/create.html'
    model = Product 
    fields = '__all__'
    # def get_context_data(self, **kwargs):
    #     context = super(CreateProductView, self).get_context_data(**kwargs)
    #     variants = Variant.objects.filter(active=True).values('id', 'title')
    #     context['product'] = True
    #     context['variants'] = list(variants.all())
    #     return context
    def get_absolute_url(self): # new
        return reverse('/')

def is_valid_queryparam(param):
    return param != '' and param is not None

class ProductListView(generic.ListView):
    context_object_name = 'product_list'
    template_name = 'products/list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = Product.objects.all()
        title = self.request.GET.get('title')
        price_from = self.request.GET.get('price_from')
        price_to = self.request.GET.get('price_to')
        date = self.request.GET.get('date')
        variant = self.request.GET.get('variant')
        # print(title)
        if is_valid_queryparam(title):
            qs = qs.filter(title__icontains=title)
        
        if is_valid_queryparam(price_from) :
            qs = qs.filter(variant__price__gte=price_from)
        
        if is_valid_queryparam(price_to) :
            qs = qs.filter(variant__price__lte=price_to)
        
        if is_valid_queryparam(date):
            qs = qs.filter(created_at__contains=date)
        
        if is_valid_queryparam(variant):
            qs = qs.filter(product_variant__variant_title__contains=variant)
               
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_prod = Product.objects.all().count()
        context['prod_count'] = count_prod
        context['variants'] = ProductVariant.objects.all()
        return context



