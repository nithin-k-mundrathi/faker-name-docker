import faker

Faker = faker.Factory().create
fake = Faker()

print("Hello {} from {}".format(fake.name(),fake.state()))
