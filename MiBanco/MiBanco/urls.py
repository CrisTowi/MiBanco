from django.conf.urls import patterns, include, url
from rest_framework import routers

from django.contrib import admin

from Principal.views import ClienteViewSet, CuentaViewSet, OperacionesCuentaViewSet

router = routers.DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'cuentas', CuentaViewSet)
router.register(r'opcuentas', OperacionesCuentaViewSet)

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

	url(r'^nueva_cuenta/$', 'Principal.views.nueva_cuenta', name='nueva_cuenta'),
	url(r'^nuevo_cliente/$', 'Principal.views.nuevo_cliente', name='nuevo_cliente'),
	url(r'^nueva_opcu/$', 'Principal.views.nueva_operacion_cuenta', name='nueva_opcu'),

	url(r'^nuevo/cliente/', 'Principal.views.nuevo_cliente_web', name='nuevo_cliente_web'),
	url(r'^editar/cliente/(?P<id>\d+)$', 'Principal.views.editar_cliente', name='editar_cliente'),

	url(r'^nuevo/cuenta/', 'Principal.views.nuevo_cuenta_web', name='nuevo_cuenta_web'),


	url(r'^nuevo/op_cuenta/', 'Principal.views.nuevo_op_cuenta_web', name='nuevo_op_cuenta_web'),
	url(r'^editar/op_cuenta/(?P<id>\d+)$', 'Principal.views.editar_op_cuenta', name='editar_op_cuenta'),
	url(r'^lista/cliente/', 'Principal.views.lista_cliente', name='lista_cliente'),
	
	url(r'^lista/cuenta/', 'Principal.views.lista_cuenta', name='lista_cuenta'),
	url(r'^lista/op_cuenta/', 'Principal.views.lista_op_cuenta', name='lista_op_cuenta'),

	url(r'^editar/cuenta/(?P<id>\d+)$', 'Principal.views.editar_cuenta', name='editar_cuenta'),


	url(r'^editar/clientemovi/', 'Principal.views.EditaCliente', name='EditaCliente'),
	url(r'^editar/cuentamovil/', 'Principal.views.EditaCuenta', name='EditaCuenta'),
	url(r'^editar/op_cuentamovil/', 'Principal.views.EditaOpCuenta', name='EditaOpCuenta'),

	url(r'^admin/', include(admin.site.urls)),
)
