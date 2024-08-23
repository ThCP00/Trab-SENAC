from django.contrib import admin
from django.urls import path, include # Importe para URLS de produto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produto.urls')), # Vamos incluir este caminho para a urls do produto
    path('pedido/', include('pedido.urls')),
    path('cliente/', include('cliente.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)