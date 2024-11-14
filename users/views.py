
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# users/views.py
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView,UpdateView
from .models import UserProfile
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse


class UserRegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')  # Redirect to login after successful registration
    def get_initial(self):
        initial_data = {
        'password1': '',
        'username': '',
        'password2': ''
        }

       
        return initial_data
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib import messages

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    
    def form_valid(self, form):
        # Add a success message when login is successful
        messages.success(self.request, "You have logged in successfully!")
        
        # Call the super method to proceed with the default behavior
        return super().form_valid(form)

    def get_redirect_url(self):
        # Replace with logic to retrieve the actual product ID you want
        product_pk = 1  # Example pk; replace with dynamic retrieval, e.g., from session or request data
        return reverse('store:product_detail', kwargs={'pk': product_pk})


class UserProfileDetailView(LoginRequiredMixin,DetailView):
    model = UserProfile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        if not self.request.user.is_authenticated:
           return redirect(reverse('users:login'))  # Redirects unauthenticated users
        try:
            return self.request.user.userprofile
        except UserProfile.DoesNotExist:
            raise Http404("Profile not found.")
    
    
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['address', 'phone_number', 'profile_picture']
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile_detail')

    def get_object(self):
        return self.request.user.userprofile