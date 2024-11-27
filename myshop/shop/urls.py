# shop/urls.py
from django.urls import path
from .views import product_list, product_detail, add_to_cart, remove_from_cart, view_cart, register_view, login_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)