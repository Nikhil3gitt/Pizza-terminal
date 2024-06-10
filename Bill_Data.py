import csv
import random

# Function to determine Dis_ID based on frequency
def determine_discount_id():
    # Create a list with the appropriate number of each Dis_ID based on the specified percentages
    dis_ids = [10] * 10 + [11] * 5 + [17] * 20 + [16] * 12 + [15] * 11 + [14] * 23 + [12] * 9 + [13] * 10
    random.shuffle(dis_ids)
    return dis_ids

# Read Order_IDs from ordersmain.csv
with open('ordersmain.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    order_ids = [row[0] for row in reader]  # Assuming the first column contains Order_IDs

# Generate the discount IDs based on the percentage
dis_ids = determine_discount_id()
# Extend dis_ids list to match the number of order_ids
while len(dis_ids) < len(order_ids):
    dis_ids.extend(determine_discount_id())
dis_ids = dis_ids[:len(order_ids)]  # Trim to the exact length of order_ids

# Open CSV file for writing
with open('bill_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(['Bill_ID', 'Del_ID', 'Dis_ID'])

    # Generate and write data rows
    for bill_id, dis_id in zip(order_ids, dis_ids):
        del_id = None  # Del_ID is null
        writer.writerow([bill_id, del_id, dis_id])

print("CSV data generation complete.")
