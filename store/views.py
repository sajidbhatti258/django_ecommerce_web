from django.shortcuts import render

from math import ceil

from django.views.generic import ListView, DetailView,CreateView,UpdateView

from.models import Product,Category

from django.urls import reverse_lazy
# Create your views here.


from django.views.generic import ListView
from .models import Category
from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from store.models import Category, Product

class CategoryProductListView(ListView):
    model = Product
    template_name = 'store/category_product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')  # Get category ID from URL
        category = get_object_or_404(Category, id=category_id)  # Fetch the category by ID
        return Product.objects.filter(category=category)  # Filter products by category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')  # Get category ID from URL
        category = get_object_or_404(Category, id=category_id)  # Fetch the category by ID
        context['category'] = category  # Add category to the context
        return context
class ProductListView(ListView):
    model = Category
    template_name = 'store/product_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # Prefetch products related to each category to minimize queries
        return Category.objects.prefetch_related('products').all()
     
    #  adding a more context data 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         
        # Add a list of all products, or featured products if needed
        context['featured_products'] = Product.objects.filter(is_featured=True)  # Adjust as necessary
        return context
 
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'prod'  # This makes the product available as 'prod' in the template

    def get_context_data(self, **kwargs):
        # Get the default context from the parent class
        context = super().get_context_data(**kwargs)
        
        # Calculate the available stock
        prod = context['prod']
        available_stock = prod.stock - prod.sold_quantity
        
        # Add the available stock to the context
        context['available_stock'] = available_stock
        
        return context
    
class ProductCreateView(CreateView):
    model = Product
    template_name = 'store/product_form.html'
    fields =[ 'name', 'description', 'price' , 'stock', 'category', 'image']
    success_url = reverse_lazy('product_list')
    
    
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'store/product_form.html'
    fields =['name','description','price','stock','category','image']
    success_url = reverse_lazy('product_list')
    
    
from django.db.models import Q

def product_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        query_words = query.split()  # Split the query into individual words
        search_conditions = Q()
        
        # Build a Q object with OR conditions for each word in the query
        for word in query_words:
            search_conditions |= Q(name__icontains=word)
        
        results = Product.objects.filter(search_conditions).distinct()  # Ensures unique results

    return render(request, 'store/product_search.html', {'query': query, 'results': results})
