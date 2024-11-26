# shop/urls.py
from django.urls import path
from .views import product_list, product_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)