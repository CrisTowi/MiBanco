from django.shortcuts import render
from Principal.models import Cliente, Cuenta, OperacionesCuenta
from Principal.serializers import ClienteSerializer, CuentaSerializer, OpCuentaSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from Principal.forms import ClienteForm, CuentaForm, OperacionesCuentaForm
from django.http import HttpResponseRedirect


class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

class CuentaViewSet(viewsets.ModelViewSet):
	queryset = Cuenta.objects.all()
	serializer_class = CuentaSerializer

class OperacionesCuentaViewSet(viewsets.ModelViewSet):
	queryset = OperacionesCuenta.objects.all()
	serializer_class = OpCuentaSerializer

@csrf_exempt
def nuevo_cliente(request):

	if request.method == 'POST':
		nombre = request.POST['nombre']
		ap_paterno = request.POST['ap_paterno']
		ap_materno = request.POST['ap_materno']
		tel = request.POST['num_tel']
		calle = request.POST['calle']
		colonia = request.POST['colonia']
		numero = request.POST['numero']

		cliente = Cliente()
		cliente.nombre = nombre
		cliente.ap_paternos = ap_paterno
		cliente.ap_materno = ap_materno
		cliente.num_telefonico = tel
		cliente.calle = calle
		cliente.colonia = colonia
		cliente.numero = numero

		cliente.save()

	return

@csrf_exempt
def nueva_cuenta(request):

	if request.method == 'POST':
		balance = float(request.POST['balance'])
		id_cliente = request.POST['cliente']

		cliente = Cliente.objects.get(id = id_cliente)

		cuenta = Cuenta()
		cuenta.balance = balance
		cuenta.cliente = cliente

		cuenta.save()

	return

@csrf_exempt
def nueva_operacion_cuenta(request):

	if request.method == 'POST':
		id_cuenta = request.POST['cuenta']
		tipo_movimiento = request.POST['tipo_mov']
		cantidad = float(request.POST['cantidad'])

		cuenta = Cuenta.objects.get(id = id_cuenta)

		operacion_cuenta = OperacionesCuenta()
		
		operacion_cuenta.cuenta = cuenta
		operacion_cuenta.tipo_movimiento = tipo_movimiento
		operacion_cuenta.cantidad = cantidad

		operacion_cuenta.save()

	return

def nuevo_cliente_web(request):

	if request.method == 'POST':
		formulario = ClienteForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/api/')
	else:
		formulario = ClienteForm()

	ctx = {'formulario': formulario}
	return render(request, 'formulario.html', ctx)

def editar_cliente(request, id):

	cliente = Cliente.objects.get(id = id)

	if request.method == 'POST':
		formulario = ClienteForm(request.POST, instance=cliente)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/api/')
	else:
		formulario = ClienteForm(instance=cliente)

	ctx = {'formulario': formulario}
	return render(request, 'formulario.html', ctx)


def nuevo_cuenta_web(request):

	if request.method == 'POST':
		formulario = CuentaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/api/')
	else:
		formulario = CuentaForm()

	ctx = {'formulario': formulario}
	return render(request, 'formulario.html', ctx)

def editar_cuenta(request, id):

	cuenta = Cuenta.objects.get(id = id)

	if request.method == 'POST':
		formulario = CuentaForm(request.POST, instance=cuenta)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/api/')
	else:
		formulario = CuentaForm(instance=cuenta)

	ctx = {'formulario': formulario}
	return render(request, 'formulario.html', ctx)


def nuevo_op_cuenta_web(request):

	if request.method == 'POST':
		formulario = OperacionesCuentaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/api/')
	else:
		formulario = OperacionesCuentaForm()

	ctx = {'formulario': formulario}
	return render(request, 'formulario.html', ctx)

def editar_op_cuenta(request, id):

	op_cuenta = OperacionesCuenta.objects.get(id = id)

	if request.method == 'POST':
		formulario = OperacionesCuentaForm(request.POST, instance=op_cuenta)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/api/')
	else:
		formulario = OperacionesCuentaForm(instance=op_cuenta)

	ctx = {'formulario': formulario}
	return render(request, 'formulario.html', ctx)

def lista_op_cuenta(request):

	op_cuentas = OperacionesCuenta.objects.all()

	ctx = {'op_cuentas': op_cuentas}

	return render(request, 'lista_op_cuenta.html', ctx)


def lista_cuenta(request):

	cuentas = Cuenta.objects.all()

	ctx = {'cuentas': cuentas}

	return render(request, 'lista_cuenta.html', ctx)


def lista_cliente(request):

	clientes = Cliente.objects.all()

	ctx = {'clientes': clientes}

	return render(request, 'lista_cliente.html', ctx)


