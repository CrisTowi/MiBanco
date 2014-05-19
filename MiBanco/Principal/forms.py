#encoding:utf-8
from django.forms import ModelForm

from Principal.models import Cliente, Cuenta, OperacionesCuenta

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente

class CuentaForm(ModelForm):
	class Meta:
		model = Cuenta

class OperacionesCuentaForm(ModelForm):
	class Meta:
		model = OperacionesCuenta
