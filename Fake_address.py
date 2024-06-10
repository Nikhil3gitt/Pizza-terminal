import csv
import random
import string
from faker import Faker

fake = Faker()

# Function to generate unique address IDs
def generate_address_id():
    return 'SC' + ''.join(random.sample(string.digits, 7))

# Function to generate address zone based on zip code
def generate_address_zone(zip_code):
    if zip_code == 'KAZ72':
        return random.choice(['W1', 'W2', 'W3', 'W4'])
    elif zip_code == 'KAZ73':
        return random.choice(['N1', 'N2'])
    elif zip_code == 'KAZ74':
        return random.choice(['NE1', 'NE2'])
    elif zip_code == 'KAZ75':
        return random.choice(['E1', 'E2'])
    elif zip_code == 'KAZ76':
        return random.choice(['SE1', 'SE2', 'SE3'])
    elif zip_code == 'KAZ77':
        return random.choice(['S1', 'S2', 'S3'])
    elif zip_code == 'KAZ78':
        return random.choice(['SW1', 'SW2', 'SW3', 'SW4', 'SW5'])
    elif zip_code == 'KAZ79':
        return random.choice(['NW1', 'NW2', 'NW3', 'NW4', 'NW5', 'NW6'])
    else:
        return 'Unknown'

# Generate fake addresses
def generate_fake_address():
    address_id = generate_address_id()
    street_number = random.randint(1, 1000)
    street_name = random.choice(street_names)
    city = 'Saltcity'
    zip_code = 'KAZ7' + str(random.randint(2, 9))
    address_zone = generate_address_zone(zip_code)

    return {
        'Address_ID': address_id,
        'Street_Number': street_number,
        'Street_Name': street_name,
        'City': city,
        'Zip_Code': zip_code,
        'Address_Zone': address_zone
    }

# Generate fake addresses
street_names = [fake.street_name() for _ in range(80)]

# Write fake addresses to CSV file
with open('fake_addresses.csv', 'w', newline='') as csvfile:
    fieldnames = ['Address_ID', 'Street_Number', 'Street_Name', 'City', 'Zip_Code', 'Address_Zone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(7860):  # Generate 7860 fake addresses
        address = generate_fake_address()
        writer.writerow(address)

print("Fake addresses generated and saved to fake_addresses.csv")
