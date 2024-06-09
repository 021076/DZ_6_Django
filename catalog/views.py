from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm
from catalog.models import Product, Version


# def product_list(request):
#     catalog = Product.objects.all()
#     context = {"catalog": catalog}
#     return render(request, 'catalog/product_list.html', context)

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'catalog/product_detail.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'catalog'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        catalog = Product.objects.all()
        for product in catalog:
            actual_version = Version.objects.filter(product=product, actual_version=True)
            if actual_version:
                product.version_title = actual_version.last().version_title
                product.version_number = actual_version.last().version_number
            else:
                product.version_title = 'Текущая версия отсутствует'
                product.version_number = '-'
        context['catalog'] = catalog
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        actual_version = Version.objects.filter(product=product, actual_version=True)
        if actual_version:
            product.version_title = actual_version.last().version_title
            product.version_number = actual_version.last().version_number
        else:
            product.version_title = 'Текущая версия отсутствует'
            product.version_number = '-'
        context['product'] = product
        return context


def contacts(request):
    if request.method == 'Product':
        print(request.Product)
    return render(request, 'catalog/contacts.html')


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.product_name)
            new_product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
