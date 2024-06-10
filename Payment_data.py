import csv
import random

# Read Bill_IDs from Bill_data.csv
bill_ids = []
with open('Bill_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        bill_ids.append(row[0])

# Function to generate a unique 15-digit Payment_ID
def generate_payment_id(existing_ids):
    while True:
        payment_id = ''.join(random.choices('0123456789', k=15))
        if payment_id not in existing_ids:
            return payment_id

# Generate tip based on specified distribution
def generate_tip():
    rand = random.random()
    if rand < 0.62:
        return round(random.uniform(0, 10), 2)
    elif rand < 0.94:
        return round(random.uniform(10, 20), 2)
    elif rand < 0.995:
        return round(random.uniform(20, 50), 2)
    else:
        return round(random.uniform(50, 100), 2)

payment_modes = ['Debit', 'Credit', 'Cash', 'Online transfer']
existing_payment_ids = set()

payments = []
for bill_id in bill_ids:
    payment_id = generate_payment_id(existing_payment_ids)
    existing_payment_ids.add(payment_id)
    payment_mode = random.choice(payment_modes)
    tip = generate_tip()
    
    payments.append([payment_id, bill_id, payment_mode, tip, None])  # Total_Amount is set to None

# Write the generated payments to a CSV file
with open('payments.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Payment_ID', 'Bill_ID', 'Payment_Mode', 'Tip', 'Total_Amount'])
    writer.writerows(payments)

print(f"{len(payments)} payments generated and written to payments.csv")

