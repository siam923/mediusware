from django.views import generic
from django.shortcuts import render
from product.models import Product, Variant, ProductVariantPrice
from .filters import ProductFilter


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(generic.ListView):
    model = Product 
    context_object_name = 'product_list'
    template_name = 'products/list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_prod = Product.objects.all().count()
        context['prod_count'] = count_prod
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context



def filterview(request):
    qs = Product.objects.all()
    count_prod = qs.count()
    title = request.GET.get('title')
    price_from = request.GET.get('price_form')
    price_to = request.GET.get('price_to')
    print(title)
    context = {
        'product_list': qs,
        'prod_count': count_prod
    }
    return render(request, "products/list.html", {})