from django.shortcuts import render

from django.views.generic import ListView, DetailView,CreateView,UpdateView

from django.urls import reverse_lazy

from orders.models import Order ,OrderItem
from cart.models import Cart, CartItem
from django.shortcuts import get_object_or_404
from users.middlewares import auth,gust
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class OrderListView(ListView):
    
    model = Order
    
    template_name = 'order_list.html'
    
    context_object_name = 'orders'
    
    def get_queryset(self):
        
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(DetailView):
    
    model = Order
    
    template_name = 'order_detail.html'
    
    context_object_name = 'order'
    
    def get_queryset(self):
        
        return Order.objects.filter(user=self.request.user)
    
    

@method_decorator(auth, name='dispatch')
class OrderCreateView(CreateView):
    
    model = Order
    template_name = 'order_form.html'
    fields = ['status', 'total']
    success_url = reverse_lazy('order_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        order = form.save()

        # Transfer items from the cart to order items
        cart = get_object_or_404(Cart, user=self.request.user)
        total = 0  # Initialize total price variable
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price  # Capture current price
            )
            total += item.product.price * item.quantity  # Add item total to overall total

        # Save the total to the order
        order.total = total
        order.save()

        # Optionally clear the user's cart
        cart.items.all().delete()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the user's cart and total to the template
        cart = get_object_or_404(Cart, user=self.request.user)
        context['cart'] = cart

        # Calculate the total price for cart items and pass it to the template
        total = sum(item.product.price * item.quantity for item in cart.items.all())
        context['total'] = total
        return context
  
class OrderUpdateView(UpdateView):
    model = Order
    fields = ['status']  # Only allow updating status
    template_name = 'orders/order_update.html'
    success_url = reverse_lazy('order_list')

    def get_queryset(self):
        # Allow only specific users or roles to update orders
        return Order.objects.filter(user=self.request.user)