# shop/views.py
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})


from .models import Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, 'Товар добавлен в корзину')
    return redirect('product_detail', id=product.id, slug=product.slug)

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart__user=request.user)
        cart_item.delete()
        messages.success(request, 'Товар удален из корзины')
    except CartItem.DoesNotExist:
        pass
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = request.user.cart.items.all()  # Доступ к объектам CartItem через отношение OneToOneField
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'shop/cart.html', context)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)

post_save.connect(create_user_cart, sender=User)