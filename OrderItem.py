import csv
import random

# Define item IDs for other tables

pizza_item_ids = [f'PZ0{i:05d}' for i in range(1, 11154)]
dessert_item_ids = ['DS101', 'DS102', 'DS103', 'DS104']
dipping_sauce_item_ids = [f'DP{i:03d}' for i in range(101, 114)]
wings_item_ids = [f'WB{i:03d}' for i in range(101, 116)] + [f'WT{i:03d}' for i in range(101, 116)]
drink_item_ids = [f'DR{i:03d}' for i in range(101, 110)] + [f'DR{i:03d}' for i in range(201, 210)] + [f'DR{i:03d}' for i in range(301, 304)]
breadstick_item_ids = [f'BS{i:03d}' for i in range(101, 117)]

# Open the file in write mode initially to write the header
with open('order_item.csv', 'w', newline='') as csvfile:
    fieldnames = ['Order_ID', 'Item_ID', 'Quantity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row

# Store all Order_IDs from ordersmain.csv
order_ids = []

# Read all Order_IDs from ordersmain.csv
with open('ordersmain.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header rows

    for row in reader:
        order_id = row[0]
        order_ids.append(order_id)

# Generate random data for Order_Item
for order_id in order_ids:
    # Generate random number of items for the order
    num_items = random.choices(range(1,16), weights=[0.04, 0.28, 0.24, 0.12, 0.1, 0.04, 0.04, 0.03, 0.03, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01])[0]

    with open('order_item.csv', 'a', newline='') as csvfile:  # Open in append mode to add data rows
        fieldnames = ['Order_ID', 'Item_ID', 'Quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for _ in range(num_items):
            item_type = random.choices(['Pizza', 'Dessert', 'Dipping Sauce', 'Wings', 'Drink', 'Breadstick'],
                                       weights=[0.4, 0.1, 0.25, 0.05, 0.1, 0.1])[0]
            
            if item_type == 'Pizza':
                item_id = random.choice(pizza_item_ids)
                quantity = random.choices([1, 2, 3], weights=[0.85, 0.13, 0.02])[0]
            elif item_type == 'Dessert':
                item_id = random.choice(dessert_item_ids)
                quantity = random.choices([1, 2, 3], weights=[0.85, 0.13, 0.02])[0]
            elif item_type == 'Dipping Sauce':
                item_id = random.choice(dipping_sauce_item_ids)
                quantity = random.choices([1, 2, 3, 4, 5, 6, 7, 8], weights=[0.21, 0.27, 0.24, 0.16, 0.08, 0.025, 0.01, 0.005])[0]
            elif item_type == 'Wings':
                item_id = random.choice(wings_item_ids)
                quantity = random.choices([1, 2, 3], weights=[0.85, 0.13, 0.02])[0]
            elif item_type == 'Drink':
                item_id = random.choice(drink_item_ids)
                quantity = random.choices([1, 2, 3], weights=[0.85, 0.13, 0.02])[0]
            elif item_type == 'Breadstick':
                item_id = random.choice(breadstick_item_ids)
                quantity = random.choices([1, 2, 3], weights=[0.85, 0.13, 0.02])[0]

            writer.writerow({'Order_ID': order_id, 'Item_ID': item_id, 'Quantity': quantity})

print('Done')
