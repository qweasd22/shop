from django.contrib import admin
from django.urls import path, include
from shop.views import product_list, product_detail, add_to_cart, remove_from_cart, view_cart, register_view, login_view, profile_view, edit_profile, logout

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view-cart/', view_cart, name='view_cart'),
    path('profile/', profile_view, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(next_page='product_list'), name='logout'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('', include('shop.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
    
    
]