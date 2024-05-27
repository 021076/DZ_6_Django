from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'catalog'


# def product_list(request):
#     catalog = Product.objects.all()
#     context = {"catalog": catalog}
#     return render(request, 'catalog/product_list.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'catalog/product_detail.html', context)

def contacts(request):
    if request.method == 'Product':
        print(request.Product)
    return render(request, 'catalog/contacts.html')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('product_name', 'product_description', 'imagery', 'category', 'cost_product')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('product_name', 'product_description', 'imagery', 'category', 'cost_product')

    # success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.product_name)
            new_product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
