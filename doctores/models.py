from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    
    def __str__(self):
        return f"Dr. {self.apellido} - {self.especialidad}"