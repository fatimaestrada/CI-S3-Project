from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from accounts import urls as accounts_urls
from products import urls as products_urls
from settings import MEDIA_ROOT
from django.views import static
from rest_framework import routers
from payments import urls as payments_urls
from cart import urls as cart_urls

from products import views as product_views
from cart import views as cart_views


router = routers.DefaultRouter()
router.register(r'products', product_views.ProductViewSet)
router.register(r'cart', cart_views.CartItemViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include(products_urls)),
    url(r'^payments/', include(payments_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^$', index, name='index'),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'accounts/', include(accounts_urls)),
    url(r'user/', include(accounts_urls)),
]
