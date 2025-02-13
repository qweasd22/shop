# shop/urls.py
from django.urls import path, include
from .views import product_list, product_detail, add_to_cart, remove_from_cart, view_cart, register_view, login_view
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter 
from .views import ProductViewSet , UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter() 
router.register(r'products', ProductViewSet, basename='product') 
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('api/', include(router.urls)), # Добавляем URL-адреса для API-маршрутизатора router.urls   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = format_suffix_patterns(urlpatterns)