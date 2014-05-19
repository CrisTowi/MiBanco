from django.contrib import admin

from Principal.models import Cliente, Cuenta, OperacionesCuenta


admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(OperacionesCuenta)