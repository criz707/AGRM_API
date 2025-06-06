from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True, verbose_name='Id del tipo de rol')
    rol = models.CharField(max_length=45, verbose_name='Nombre del rol')
    
    def __str__(self):
        return self.rol


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, verbose_name='Id del usuario')
    nombre = models.CharField(max_length=45, verbose_name='Nombre del usuario')
    correo = models.CharField(max_length=45, verbose_name='Correo del usuario')
    foto = models.TextField(max_length=150, null=True, blank=True, verbose_name='URL del perfil del usuario')
    contrasena = models.CharField(max_length=45, verbose_name='Contraseña del usuario')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol del usuario')

    def __str__(self):
        return self.nombre


class EstadoReserva(models.Model):
    id_estado = models.IntegerField(primary_key=True, verbose_name='Id del estado de la reserva')
    estado = models.CharField(max_length=45, verbose_name='Estado de la reserva')  # corregí el typo ESATDO  estado

    def __str__(self):
        return self.estado


class Mesa(models.Model):
    id_mesa = models.IntegerField(primary_key=True, verbose_name='Id de la mesa')
    numero = models.CharField(max_length=45, verbose_name='Número de la mesa')
    piso = models.IntegerField(null=True, blank=True, verbose_name='Piso de la mesa')

    def __str__(self):
        return f"Mesa {self.numero} - Piso {self.piso}"


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True, verbose_name='Id de la reserva')
    fecha_inicio = models.DateTimeField(verbose_name='Fecha de inicio')
    fecha_final = models.DateTimeField(verbose_name='Fecha final')
    fecha = models.DateTimeField(verbose_name='Fecha de la reserva')
    
    estado = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE, verbose_name='Estado de la reserva')
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, verbose_name='Mesa reservada')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario que reserva')

    def __str__(self):
        return f"Reserva {self.id_reserva} - {self.fecha.date()}"
