from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre 					= models.CharField(max_length=45)
	ap_paterno 			= models.CharField(max_length=45)
	ap_materno 			= models.CharField(max_length=45)
	num_telefonico	= models.CharField(max_length=45)
	calle						= models.CharField(max_length=45)
	colonia 				= models.CharField(max_length=45)
	numero 					= models.IntegerField()

	def __unicode__(self):
		return self.nombre + ' ' + self.ap_paterno

class Cuenta(models.Model):
	balance = models.FloatField()
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.id

class OperacionesCuenta(models.Model):
	cuenta 					= models.ForeignKey(Cuenta)
	fecha_operacion = models.DateField(auto_now_add=True)
	tipo_movimiento = models.CharField(max_length=1)
	cantidad 				= models.FloatField()

	def __unicode__(self):
		return str(self.cuenta.id) + ' ' + str(self.fecha_operacion) 