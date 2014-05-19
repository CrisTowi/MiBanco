from rest_framework import serializers

from Principal.models import Cliente, Cuenta, OperacionesCuenta

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cliente
		fields = ('id', 'nombre', 'ap_paterno', 'ap_materno', 'num_telefonico', 'calle', 'colonia', 'numero',)


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cuenta
		fields = ('id', 'balance', 'cliente',)

class OpCuentaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = OperacionesCuenta
		fields = ('id', 'cuenta', 'fecha_operacion', 'tipo_movimiento', 'cantidad',)