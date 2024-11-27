from django.contrib import admin
from django.urls import path, include
from shop.views import product_list, product_detail, add_to_cart, remove_from_cart, view_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view-cart/', view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    
    path('', include('shop.urls')),
    
]