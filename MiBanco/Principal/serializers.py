from rest_framework import serializers

from Principal.models import Cliente, Cuenta, OperacionesCuenta

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = ('id', 'nombre', 'ap_paterno', 'ap_materno', 'num_telefonico', 'calle', 'colonia', 'numero',)


class CuentaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cuenta
		fields = ('id', 'balance', 'cliente',)

class OpCuentaSerializer(serializers.ModelSerializer):
	class Meta:
		model = OperacionesCuenta
		fields = ('id', 'cuenta', 'fecha_operacion', 'tipo_movimiento', 'cantidad',)