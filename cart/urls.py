from django.conf.urls import url
from .views import user_cart, add_to_cart, remove_from_cart, add_to_cart_cart, remove_from_cart_cart

urlpatterns = [
    url(r'^$', user_cart, name='cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^addcart/(?P<id>\d+)', add_to_cart_cart, name='add_to_cart_cart'),
    url(r'^remove/(?P<id>\d+)', remove_from_cart, name='remove_from_cart'),
    url(r'^removecart/(?P<id>\d+)', remove_from_cart_cart, name='remove_from_cart_cart'),

]