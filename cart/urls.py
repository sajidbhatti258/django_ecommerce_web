
from django.contrib import admin
from django.urls import path,include
from .views import CartListView,CartItemCreateView,CartItemDeleteView,CartItemUpdateView,AddToCartView

app_name ='cart'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', CartListView.as_view(), name='cart_list'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('add/', CartItemCreateView.as_view(), name='cart_add'),
    path('update/<int:pk>', CartItemUpdateView.as_view(), name='cart_update'),
    path('delete/<int:pk>', CartItemDeleteView.as_view(), name='cart_delete')
]
