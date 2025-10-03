from faker import Faker

fake = Faker()

usuarios = {}
for codigo in range(1, 16):
    usuarios["codigo"] = codigo
    usuarios["nombre"] = fake.name()
    usuarios["direccion"] = fake.address()
    usuarios["correo"] = fake.email()
    usuarios["telefono"] = fake.phone_number()

