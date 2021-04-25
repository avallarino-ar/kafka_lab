from faker import Faker

fake = Faker()

def get_user():
    return {
        "fname": fake.first_name(),
        "lname": fake.last_name(),
        "address": fake.address(),
        "edad": fake.random_int(0, 100),
        # "date_of_birth": fake.date(end_datetime='-1y'),
        "email": fake.email()
    }


if __name__ == "__main__":
    print(get_user())
