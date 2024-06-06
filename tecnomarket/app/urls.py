from django.urls import path
from .views import home, galeria, contacto, agregar_producto, listar_productos, \
    modificar_productos, eliminar_productos,registro

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('contacto/', contacto, name='contacto'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-productos/<id>/', modificar_productos, name='modificar_productos'),
    path('eliminar-productos/<id>/', eliminar_productos, name='eliminar_productos'),
    path('registro/', registro, name='registro'),
]
