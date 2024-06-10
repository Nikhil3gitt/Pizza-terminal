import csv
import random
import string

# Function to generate random pizza attributes
def generate_pizza():
    pizza_name_options = [
        'Make Your Own Pizza', 'Cheese Pizza', 'Hawaiian', 'Super Hawaiian',
        'Canadian Classic', 'Garden Fresh', 'Works', 'Mean', 'Ultimate Meats',
        'Pepperoni', 'Six Cheese', 'Chicken BBQ', 'Fiery Buffalo', 'Meatball Pepperoni',
        'Spinach', 'Cuppy Roni', 'Philly Cheese Steak', 'Cheesy Alfredo', 'Tandoori Chicken',
        'BBQ Meats'
    ]
    size_options = ['Small', 'Medium', 'Large', 'Extra large']
    base_options = {
        'Small': ['Regular', 'Gluten free'],
        'Medium': ['Regular'],
        'Large': ['Regular', 'Thin crust', 'Stuffed crust', 'Garlic parmesan', 'Garlic parmesan Stuffed crust'],
        'Extra large': ['Regular', 'Neon style']
    }
    sauce_options = ['Pizza sauce', 'Creamy tomato', 'BBQ', 'Buffalo', 'Ranch', 'Alfredo', 'Tandoori chicken']
    sauce_size_options = ['No Sauce', 'Normal Sauce', 'Light Sauce', 'Extra Sauce']
    cooking_instruction_options = ['Normal cook', 'Well-done']
    cutting_instruction_options = ['Normal cut', 'Square cut']
    cheese_options = ['Regular cheese', 'No cheese']

    # Generate Item_ID
    item_id = 'PZ' + ''.join(random.choices(string.digits, k=6))

    # Generate pizza attributes
    pizza_name = random.choice(pizza_name_options)
    size = random.choices(size_options, weights=[13, 30, 44, 13])[0]
    base = random.choice(base_options[size])
    sauce = random.choices(sauce_options, weights=[80, 5, 5, 5, 5, 5, 5])[0]
    sauce_size = random.choices(sauce_size_options, weights=[70, 10, 10, 10])[0]
    cooking_instruction = random.choices(cooking_instruction_options, weights=[80, 20])[0]
    cutting_instruction = random.choices(cutting_instruction_options, weights=[85, 15])[0]
    cheese = random.choices(cheese_options, weights=[95, 5])[0]

    # Generate random price based on size
    if size == 'Small':
        price = round(random.uniform(11.99, 19.99), 2)
    elif size == 'Medium':
        price = round(random.uniform(16.99, 24.99), 2)
    elif size == 'Large':
        price = round(random.uniform(20.99, 47.99), 2)
    else:
        price = round(random.uniform(21.99, 47.99), 2)

    return [item_id, pizza_name, size, base, sauce, sauce_size, cooking_instruction, cutting_instruction, cheese, price]

# Generate pizza data
data = [['Item_ID', 'Pizza Name', 'Size', 'Base', 'Sauce', 'Sauce Size', 'Cooking Instruction', 'Cutting Instruction', 'Cheese', 'Price']]
for i in range(67000):
    data.append(generate_pizza())

# Write data to CSV file
with open('pizza_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file generated successfully.")
