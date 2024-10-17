from django.db import models

class Empleados(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    num_emergencia = models.CharField(max_length=20)
    identificacion = models.CharField(max_length=2)
    acta_nacimiento = models.CharField(max_length=2)
    rfc = models.CharField(max_length=2)
    antidoping = models.CharField(max_length=2)
    carta = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre
    
class Proveedores(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    correo = models.EmailField()
    fecha_registro = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Categorias(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    

class Productos(models.Model):
    nombre = models.CharField(max_length=20)
    existencia = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_registro = models.DateField(auto_now=True)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    





