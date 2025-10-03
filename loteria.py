from faker import Faker

fake = Faker()

usuarios = {}
for codigo in range(1, 16):
    usuarios[codigo] = {
        "nombre": fake.name(),
        "direccion": fake.address(),
        "correo": fake.email(),
        "telefono": fake.phone_number()
    }

print("----------Usuarios----------")
for codigo, datos in usuarios.items():
    print(f"Usuario {codigo}:")
    print(f"    Nombre: {datos['nombre']}")
    print(f"    Dirección: {datos['direccion']}")
    print(f"    Correo electrónico: {datos['correo']}")
    print(f"    Teléfono: {datos['telefono']}")
