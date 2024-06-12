import pandas as pd
from faker import Faker
import random
import csv
import json

# config:
FILENAME_OUT = 'fake_citizen_data'
NUM_USERS = 20000           # database size (rows)
MISSING_SCALE = 1           # make db more realistic; 0: all fields are filled up; >5 - a lot data is missing
OUTPUT_FORMAT = 'mysql'     # options: 'csv', 'json', 'mysql'
EMAIL_DOMAINS = [ 
    "gmail.com",
    "gmail.com",
    "gmail.com",
    "yahoo.com",
    "yahoo.com",
    "outlook.com",
    "aol.com",
    "comcast.net",
    "icloud.com",
    "msn.com",
    "msn.com",
    "live.com",
    "verizon.net",
    "att.net",
    "bellsouth.net",
    "mail.com",
    "mail.com",
    "me.com",
    "cox.net",
    "sbcglobal.net",
    "earthlink.net",
    "charter.net",
    "hotmail.co.uk",
    "ymail.com",
    "mac.com",
    "aim.com",
    "rocketmail.com",
    "zoho.com",
    "roadrunner.com"]

def generate_user_data(num_users, domain_parts, missing_scale):
    fake = Faker()
    fake.seed_instance(4321)
    users = []

    for i in range(num_users):
        name = fake.name()
        first_name = name.split()[0].lower()
        last_name = name.split()[-1].lower()

        local_part_options = [
            f"{first_name[0]}{last_name[0]}", 
            first_name,
            f"{first_name}{last_name[0]}",  
            f"{first_name}_{last_name}", 
            f"{first_name}{random.randint(10, 400)}",
            fake.email().split('@')[0]]

        local_part = random.choice(local_part_options)
        domain_part = random.choice(domain_parts)
        email = f"{local_part}@{domain_part}"
        birthdate = fake.date_of_birth(minimum_age=22, maximum_age=70).isoformat()

        user_data = {
            "Name": name,
            "Address": fake.address(),
            "Email": email,
            "Phone Number": fake.phone_number(),
            "Birthdate": birthdate,
            "Social Security Number": fake.ssn(),
            "Employment Status": fake.job(),
            "Income": fake.random_number(digits=5),
            "License Plate": fake.license_plate(),
            "Government Status": "Yes" if i % random.randint(150, 300) == 0 else "No",
            "Military Service": "Yes" if i % random.randint(70, 150) == 0 else "No"}

        if missing_scale > 0:
            fields_to_remove = random.sample(list(user_data.keys() - {'Name'}), min(len(user_data.keys()) - 1, missing_scale))
            for field in fields_to_remove:
                user_data[field] = None

        users.append(user_data)
    return users

def save_data(users, format):
    if format == 'csv':
        df = pd.DataFrame(users)
        df.to_csv(f'{FILENAME_OUT}.csv', index=False, quoting=csv.QUOTE_ALL)
    elif format == 'json':
        with open(f'{FILENAME_OUT}.json', 'w') as f:
            json.dump(users, f, indent=4)
    elif format == 'mysql':
        with open(f'{FILENAME_OUT}.dump', 'w') as f:
            for user in users:
                columns = ', '.join(user.keys())
                values_list = []
                for value in user.values():
                    if value is not None:
                        value = str(value).replace("'", "''")
                        values_list.append(f"'{value}'")
                    else:
                        values_list.append("NULL")
                values = ', '.join(values_list)
                f.write(f"INSERT INTO users ({columns}) VALUES ({values});\n")

if __name__ == '__main__':
    users = generate_user_data(NUM_USERS, EMAIL_DOMAINS, MISSING_SCALE)
    save_data(users, OUTPUT_FORMAT)
