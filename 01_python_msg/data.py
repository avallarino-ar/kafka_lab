from faker import Faker

fake = Faker()

def get_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }


if __name__ == "__main__":
    print(get_user())
