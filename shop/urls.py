from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings


from products.views import (home_page, about_page, not_fount_page, search, product_page, add_product_to_cart, user_cart,
                            add_product_to_favorites, user_favorites)
from users.views import register_view, login_view, profile_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about', about_page),
    path('signup', register_view, name='signup'),
    path('login', login_view, name='login'),
    path('profile', profile_view, name='profile'),
    path('logout', logout_view, name='logout'),
    path('search', search),
    path('products/<int:id>', product_page),
    path('notfound', not_fount_page, name='notfound'),
    path('add_to_cart/<int:id>', add_product_to_cart),
    path('user_cart', user_cart, name='user_cart'),
    path('add_to_cart/<int:id>', add_product_to_favorites),
    path('user_favorites', user_favorites, name='user_favorites')
]
# /media/product.png,
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# /static/hello.js
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
