import csv
import random
import string
from datetime import datetime, timedelta

# Helper functions
def random_order_id():
    return 'O' + ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.digits, k=6))

def random_date(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

def random_time(morning_ratio, afternoon_ratio):
    random_value = random.random()
    if random_value < morning_ratio:
        return (datetime.min + timedelta(hours=random.randint(11, 14), minutes=random.randint(0, 59))).time()
    elif random_value < morning_ratio + afternoon_ratio:
        return (datetime.min + timedelta(hours=random.randint(14, 17), minutes=random.randint(0, 59))).time()
    else:
        return (datetime.min + timedelta(hours=random.randint(17, 23), minutes=random.randint(0, 59))).time()

def get_order_type(order_source):
    if order_source == 'Web':
        return random.choices(['Pick Up', 'Delivery'], weights=[0.83, 0.17], k=1)[0]
    elif order_source == 'Call':
        return random.choices(['Pick Up', 'Delivery'], weights=[0.83, 0.17], k=1)[0]
    elif order_source == 'Inperson':
        return random.choices(['Dine In', 'Pick Up', 'Delivery'], weights=[0.2, 0.7, 0.1], k=1)[0]
    elif order_source == 'Third Party':
        return random.choices(['Uber', 'Skip', 'Door Dash'], weights=[0.53, 0.2, 0.27], k=1)[0]
    else:
        return 'Invalid Order Source'

# Configuration
num_orders = 30000
morning_ratio = 0.15
afternoon_ratio = 0.30
years = [2022, 2023]
order_sources = ['Web', 'Call', 'Inperson', 'Third Party']
employees = list(range(10002, 10014))
customer_ids = list(range(1001, 7000))

# Load address IDs from fake_addresses.csv
fake_address_ids = []
with open('fake_addresses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        fake_address_ids.append(row['Address_ID'])

# Generate data
orders = []
order_ids = set()
customer_address_mapping = {}  # Dictionary to store address ID for each customer ID

while len(orders) < num_orders:
    order_id = random_order_id()
    if order_id in order_ids:
        continue  # Ensure unique order ID
    order_ids.add(order_id)

    employee_id = random.choice(employees)
    order_date = random_date(random.choice(years))
    order_time = random_time(morning_ratio, afternoon_ratio)
    order_source = random.choice(order_sources)
    
    order_type = get_order_type(order_source)
    if order_type == 'Invalid Order Source':
        continue  # Skip invalid order source

    customer_id = 'C' + str(random.choice(customer_ids)).zfill(4)
    subtotal_price = None

    if order_type == 'Delivery':
        # For delivery orders, select address ID from fake_addresses.csv
        address_id = random.choice(fake_address_ids)
        # Randomly vary address ID in 5% of cases for the same customer ID
        if random.random() < 0.05:
            address_id = random.choice(fake_address_ids)
            customer_address_mapping[customer_id] = address_id
        else:
            if customer_id in customer_address_mapping:
                address_id = customer_address_mapping[customer_id]
            else:
                address_id = random.choice(fake_address_ids)
                customer_address_mapping[customer_id] = address_id
    else:
        # For non-delivery orders, use default address ID 'SC0000001'
        address_id = 'SC0000001'

    orders.append([order_id, employee_id, order_date, order_time, order_source, order_type, subtotal_price, customer_id, address_id])

# Write to CSV
with open('ordersmain.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Order_ID', 'Employee_ID', 'ODate', 'OTime', 'Order_Source', 'Order_Type', 'Subtotal_Price', 'Customer_ID', 'Address_ID'])
    writer.writerows(orders)

print(f"{len(orders)} orders generated and written to ordersmain.csv")
