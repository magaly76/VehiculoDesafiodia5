from .models import Vehiculo, Chofer, RegistroContabilidad
from datetime import date

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo(
        patente = patente,
        marca = marca,
        modelo = modelo,
        year = year
    )
    vehiculo.save()

def crear_chofer(rut, nombre, apellido, patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    chofer = Chofer(
        rut = rut,
        nombre = nombre,
        apellido = apellido,
        activo = False,
        creacion_registro = date.today(),
        patente = vehiculo
    )

    chofer.save()

def crear_registro_contable(precio, patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    registro = RegistroContabilidad (
        fecha_compra = date.today(),
        precio = precio,
        patente = vehiculo
    )

    registro.save()

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()

def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()

def deshabilitar_vehiculo():
    return "funcion no implementada"

def habilitar_vehiculo():
    return "Funcion no implementada"

def obtener_vehiculo(patente):
    return Vehiculo.objects.get(patente=patente)

def obtener_chofer(rut):
    return Chofer.objects.get(rut=rut)

def asignar_chofer_vehiculo(rut, patente):
    chofer = Chofer.objects.get(rut=rut)
    vehiculo = Vehiculo.objects.get(patente=patente)
    chofer.patente = vehiculo
    chofer.save()

def imprimir_datos_vehiculo():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f'Patente:{vehiculo.patente} Marca:{vehiculo.marca} Modelo:{vehiculo.modelo} Año:{vehiculo.year}' )