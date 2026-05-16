from doctores.models import Doctor

Doctor.objects.create(nombre="Juan", apellido="Pérez", especialidad="Cardiología", telefono="8112345678")
Doctor.objects.create(nombre="María", apellido="López", especialidad="Dermatología", telefono="8123456789")
Doctor.objects.create(nombre="Carlos", apellido="Ramírez", especialidad="Pediatría", telefono="8134567890")
Doctor.objects.create(nombre="Ana", apellido="González", especialidad="Neurología", telefono="8145678901")
Doctor.objects.create(nombre="José", apellido="Martínez", especialidad="Ortopedia", telefono="8156789012")
Doctor.objects.create(nombre="Laura", apellido="Hernández", especialidad="Ginecología", telefono="8167890123")
Doctor.objects.create(nombre="Miguel", apellido="Torres", especialidad="Oftalmología", telefono="8178901234")
Doctor.objects.create(nombre="Sofía", apellido="Vargas", especialidad="Oncología", telefono="8189012345")
Doctor.objects.create(nombre="Ricardo", apellido="Castillo", especialidad="Psiquiatría", telefono="8190123456")
Doctor.objects.create(nombre="Patricia", apellido="Flores", especialidad="Medicina Interna", telefono="8201234567")


from empleados.models import Empleado

Empleado.objects.create(nombre="Luis García", puesto="Recepcionista", fecha_contratacion="2024-01-15")
Empleado.objects.create(nombre="Ana Torres", puesto="Veterinaria", fecha_contratacion="2023-11-20")
Empleado.objects.create(nombre="Carlos López", puesto="Asistente", fecha_contratacion="2024-03-05")
Empleado.objects.create(nombre="María Hernández", puesto="Contadora", fecha_contratacion="2022-09-10")
Empleado.objects.create(nombre="José Martínez", puesto="Entrenador", fecha_contratacion="2023-07-01")
Empleado.objects.create(nombre="Laura Ramírez", puesto="Recepcionista", fecha_contratacion="2024-02-18")
Empleado.objects.create(nombre="Miguel Castillo", puesto="Veterinario", fecha_contratacion="2023-12-12")
Empleado.objects.create(nombre="Patricia Flores", puesto="Asistente", fecha_contratacion="2022-08-25")
Empleado.objects.create(nombre="Ricardo Vargas", puesto="Administrador", fecha_contratacion="2023-05-30")
Empleado.objects.create(nombre="Sofía González", puesto="Auxiliar", fecha_contratacion="2024-04-10")


from productos.models import Producto

Producto.objects.create(nombre="Collar Antipulgas", descripcion="Protección contra pulgas y garrapatas", precio=199.99, stock=50)
Producto.objects.create(nombre="Alimento Premium", descripcion="Croquetas para perro adulto", precio=899.50, stock=120)
Producto.objects.create(nombre="Juguete de Pelota", descripcion="Pelota resistente para morder", precio=75.00, stock=200)
Producto.objects.create(nombre="Arena para Gato", descripcion="Arena absorbente y sin olor", precio=150.00, stock=80)
Producto.objects.create(nombre="Shampoo Medicado", descripcion="Shampoo para piel sensible", precio=220.00, stock=40)
Producto.objects.create(nombre="Transportadora", descripcion="Caja transportadora tamaño mediano", precio=650.00, stock=25)
Producto.objects.create(nombre="Vitaminas Caninas", descripcion="Suplemento multivitamínico para perros", precio=300.00, stock=60)
Producto.objects.create(nombre="Rascador para Gato", descripcion="Rascador de cartón reciclado", precio=180.00, stock=35)
Producto.objects.create(nombre="Cepillo de Cerdas", descripcion="Cepillo para pelaje largo", precio=95.00, stock=100)
Producto.objects.create(nombre="Alimento para Cachorros", descripcion="Croquetas especiales para cachorros", precio=750.00, stock=90)


from servicios.models import Servicio

Servicio.objects.create(nombre="Consulta General", costo=350.00)
Servicio.objects.create(nombre="Vacunación", costo=250.00)
Servicio.objects.create(nombre="Desparasitación", costo=200.00)
Servicio.objects.create(nombre="Cirugía Menor", costo=1500.00)
Servicio.objects.create(nombre="Cirugía Mayor", costo=5000.00)
Servicio.objects.create(nombre="Estética Canina", costo=400.00)
Servicio.objects.create(nombre="Estética Felina", costo=450.00)
Servicio.objects.create(nombre="Radiografía", costo=800.00)
Servicio.objects.create(nombre="Ultrasonido", costo=1200.00)
Servicio.objects.create(nombre="Hospitalización", costo=1000.00)


from sucursales.models import Sucursal

Sucursal.objects.create(nombre="Sucursal Centro", direccion="Av. Juárez #123", ciudad="Monterrey")
Sucursal.objects.create(nombre="Sucursal Norte", direccion="Calle Hidalgo #456", ciudad="San Nicolás")
Sucursal.objects.create(nombre="Sucursal Sur", direccion="Blvd. Acapulco #789", ciudad="Guadalupe")
Sucursal.objects.create(nombre="Sucursal Oriente", direccion="Av. Miguel Alemán #321", ciudad="Apodaca")
Sucursal.objects.create(nombre="Sucursal Poniente", direccion="Calle Morelos #654", ciudad="Santa Catarina")
Sucursal.objects.create(nombre="Sucursal San Pedro", direccion="Av. Vasconcelos #987", ciudad="San Pedro Garza García")
Sucursal.objects.create(nombre="Sucursal Escobedo", direccion="Carretera a Laredo #111", ciudad="Escobedo")
Sucursal.objects.create(nombre="Sucursal García", direccion="Av. Lincoln #222", ciudad="García")
Sucursal.objects.create(nombre="Sucursal Cadereyta", direccion="Calle Zaragoza #333", ciudad="Cadereyta")
Sucursal.objects.create(nombre="Sucursal Santiago", direccion="Av. Las Huertas #444", ciudad="Santiago")