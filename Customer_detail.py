import csv
import random
from faker import Faker

# Function to generate random contact numbers in the format (XX)-xxx-xxx
def generate_contact_number():
    area_code = random.randint(10, 99)
    prefix = random.randint(100, 999)
    suffix = random.randint(100, 999)
    return f'({area_code})-{prefix}-{suffix}'

# Initialize Faker to generate random names
fake = Faker()

# Open the ordersmain.csv file to read the unique Customer_IDs
unique_customer_ids = set()
with open('ordersmain.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        unique_customer_ids.add(row['Customer_ID'])

# Open CSV file for writing
with open('customer_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(['Customer_ID', 'CFName', 'CSName', 'Contact'])

    # Generate and write data rows for each unique Customer_ID
    for customer_id in unique_customer_ids:
        # Generate customer data for each unique Customer_ID
        first_name = fake.first_name()
        last_name = fake.last_name()
        contact = generate_contact_number()
        writer.writerow([customer_id, first_name, last_name, contact])

print("CSV data generation complete.")
