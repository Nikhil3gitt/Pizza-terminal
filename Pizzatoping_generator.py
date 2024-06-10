import csv
import random

# Load pizza data from CSV file
pizza_data = []
with open('pizza_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    pizza_data = list(reader)

# Define toppings and their IDs
toppings = {
    1: 'Bacon', 2: 'Banana peppers', 3: 'Beef', 4: 'Black olives', 5: 'Canadian bacon',
    6: 'Chicken', 7: 'Cuppy Roni', 8: 'Italian sausage', 9: 'Jalapenos', 10: 'Green olives',
    11: 'Green peppers', 12: 'Pepperoni', 13: 'Pineapple', 14: 'Mushrooms', 15: 'Onions',
    16: 'Spinach', 17: 'Feta cheese', 18: 'Extra cheese', 19: 'Salami', 20: 'Sausage',
    21: 'Spinach', 22: 'Meatball', 23: 'Steak', 24: '2 Cheese', 25: '3 Cheese'
}

# Define coverage options
coverage_options = ['LeftHalf', 'RightHalf', 'Entire']

# Define relevant toppings for each pizza name
relevant_toppings = {
    'Cheese Pizza': [18, 24, 25],
    'Hawaiian': [5, 12, 13],
    'Super Hawaiian': [5, 12, 13, 20],
    'Canadian Classic': [5, 8, 14],
    'Garden Fresh': [2, 4, 9, 11, 13, 14, 16],
    'Works': [1, 8, 9, 11, 12, 14, 20],
    'Mean': [1, 8, 12, 20, 22],
    'Ultimate Meats': [1, 3, 5, 8, 12, 20],
    'Pepperoni': [7, 12],
    'Six Cheese': [18, 24, 25],
    'Chicken BBQ': [6, 8, 14],
    'Fiery Buffalo': [6, 9, 12, 14],
    'Meatball Pepperoni': [12, 22],
    'Spinach': [16, 17, 18],
    'Cuppy Roni': [7],
    'Philly Cheese Steak': [8, 14, 23],
    'Cheesy Alfredo': [18, 24, 25],
    'Tandoori Chicken': [6, 9],
    'BBQ Meats': [3, 5, 6, 12, 20],
    'Make Your Own Pizza': list(toppings.keys())
}

# Function to generate random pizza toppings for each pizza
def generate_pizza_toppings(item_id, pizza_name):
    # Ensure num_toppings does not exceed the number of relevant toppings
    max_toppings = len(relevant_toppings.get(pizza_name, toppings.keys()))
    num_toppings = min(random.randint(1, 5), max_toppings)
    
    if pizza_name in relevant_toppings:
        selected_toppings = random.sample(relevant_toppings[pizza_name], num_toppings)
    else:
        selected_toppings = random.sample(list(toppings.keys()), num_toppings)
    
    pizza_toppings = []
    for topping_id in selected_toppings:
        coverage = 'Entire' if random.random() < 0.75 else random.choice(coverage_options[:2])
        pizza_toppings.append([item_id, topping_id, coverage])
    
    return pizza_toppings

# Generate PizzaTopping data
pizza_topping_data = [['Item_ID', 'T_ID', 'Coverage']]
for pizza in pizza_data:
    item_id = pizza[0]
    pizza_name = pizza[1]
    pizza_toppings = generate_pizza_toppings(item_id, pizza_name)
    pizza_topping_data.extend(pizza_toppings)

# Write PizzaTopping data to CSV file
with open('pizza_topping_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(pizza_topping_data)

print("PizzaTopping CSV file generated successfully.")
