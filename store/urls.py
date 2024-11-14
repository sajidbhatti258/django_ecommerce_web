
from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
     path('search/', product_search, name='product_search'),
    path('', ProductListView.as_view(), name="product_list"),
    # path('products/<int:category_id>/', ProductListView.as_view(), name='product_list'),
    path('category/<int:category_id>/', CategoryProductListView.as_view(), name='category_product_list'),
    path('<int:category_id>/', ProductListView.as_view(), name='product_list_by_category'),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
   
]
