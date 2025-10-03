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