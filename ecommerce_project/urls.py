
from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index_page, name='home_page'),
    
   path('', include(('store.urls', 'store'), namespace='store')),

    path('cart/', include('cart.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls', namespace='users')),
   
]
if settings.DEBUG:  # Only serve media files this way in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
