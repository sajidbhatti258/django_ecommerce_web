from django.shortcuts import render , redirect , get_list_or_404

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from cart.models import Cart, CartItem
from django.views.generic import ListView, CreateView , UpdateView, DeleteView

from store.models import Product

from django.contrib import messages
from users.middlewares import auth,gust
from django.utils.decorators import method_decorator

# Create your views here.

class CartListView(LoginRequiredMixin,ListView):
    model = CartItem
    template_name = 'cart/cart_detail.html'  # Customize the template path
    context_object_name = 'cart_items'

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart.items.all()
    
class CartItemCreateView(LoginRequiredMixin,CreateView):
    model = CartItem
    fields = ['product', 'quantity']
    
    def form_valid(self, form):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        form.instance.cart = cart
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('cart:cart_list')
    
    
class CartItemUpdateView(LoginRequiredMixin,UpdateView):
    model = CartItem
    fields = ['quantity']
    template_name ='cart/cartitem_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_name'] = self.object.product.name
        context['product_price'] = self.object.product.price
        context['product_quantity'] = self.object.quantity
        return context

    def get_success_url(self):
        return reverse_lazy('cart:cart_list')
    
class CartItemDeleteView(LoginRequiredMixin,DeleteView):
    model = CartItem
    template_name = 'cart/cartitem_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('cart:cart_list')

    def delete(self, request, *args, **kwargs):
        # Get the CartItem object
        cart_item = self.get_object()

        # Get the associated product
        product = cart_item.product

        # Update the product stock
        product.stock += cart_item.quantity  # Increase stock by the quantity in the cart item
        product.save()

        # Now call the parent class's delete method to delete the CartItem
        return super().delete(request, *args, **kwargs)



class AddToCartView(View):
    @method_decorator(auth)  # Apply the auth decorator
    
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        # Check stock availability
        if quantity > product.stock - product.sold_quantity:
            messages.error(request, "Not enough stock available!")
            return redirect('store:product_detail', pk=product_id)

        # Get or create a cart for the user
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Check if the product is already in the cart
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        # Update quantity if the item already exists
        if not item_created:
            new_quantity = cart_item.quantity + quantity
            if new_quantity > product.stock - product.sold_quantity:
                messages.error(request, "Not enough stock available for the added quantity!")
                return redirect('store:product_detail', pk=product_id)

            cart_item.quantity = new_quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        # Deduct stock from available quantity
        product.sold_quantity += quantity
        product.save()

        messages.success(request, "Product added to cart!")
        return redirect('store:product_detail', pk=product_id)  # Redirect to the cart list view

    def get_success_url(self):
        return reverse_lazy('cart:cart_list')
