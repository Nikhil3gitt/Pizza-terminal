import csv
import random
import string

# Function to assign new unique Item IDs starting from "PZ"
def assign_new_item_ids(csv_file):
    # Read the CSV file and store data in a list
    data = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        data.append(header)
        for row in reader:
            data.append(row)

    # Remove duplicate rows based on specific columns (excluding Item_ID and Price)
    cleaned_data = [data[0]]  
    seen = set()
    for row in data[1:]:
        key = tuple(row[1:-1])  # Exclude Item_ID and Price columns
        if key not in seen:
            cleaned_data.append(row)
            seen.add(key)

    # Assign new unique Item IDs starting from "PZ"
    for i, row in enumerate(cleaned_data[1:], start=1):
        row[0] = 'PZ' + str(i).zfill(6)  # Generate new Item_ID

    # Write the cleaned and updated data back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_data)

    print("Duplicate rows removed and new Item IDs assigned.")

# Replace 'pizza_data.csv' with the name of your CSV file
assign_new_item_ids('pizza_data.csv')
