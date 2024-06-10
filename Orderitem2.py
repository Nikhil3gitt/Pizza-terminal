import pandas as pd
import random

# Read the CSV files
file1 = pd.read_csv('Pizza_data.csv')
file2 = pd.read_csv('order_item.csv')

# Extract the 'Item_ID' column
file1_order_ids = file1['Item_ID']
file2_order_ids = file2['Item_ID']

# Find missing Item IDs from file1 in file2
missing_item_ids = file1_order_ids[~file1_order_ids.isin(file2_order_ids)]

if not missing_item_ids.empty:
    # Generate random quantities for missing Item IDs
    quantities = [random.choices([1, 2, 3], weights=[0.85, 0.13, 0.02])[0] for _ in range(len(missing_item_ids))]
    
    # Randomly select Order IDs from existing order_item.csv file
    existing_order_ids = file2['Order_ID'].unique()
    order_ids = [random.choice(existing_order_ids) for _ in range(len(missing_item_ids))]
    
    # Create a DataFrame for missing Item IDs, quantities, and Order IDs
    missing_data = pd.DataFrame({
        'Order_ID': order_ids,
        'Item_ID': missing_item_ids,
        'Quantity': quantities
    })
    
    # Append missing data to order_item.csv
    missing_data.to_csv('order_item.csv', mode='a', header=False, index=False)
    
    print("Missing Item IDs appended to order_item.csv.")
else:
    print("All Order IDs from file1 are present in file2.")
