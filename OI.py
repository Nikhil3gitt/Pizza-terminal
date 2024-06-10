import pandas as pd
import pymysql

# Connect to MySQL database
conn = pymysql.connect(host='localhost', user='root', password='Niks@1254', database='Pizza_terminal')
cursor = conn.cursor()

# Disable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

# Load CSV file into DataFrame
csv_file_path = '/Users/nikhilnakum/Local Disk(E)/Learning/SQl_Project/order_item.csv'
data = pd.read_csv(csv_file_path)

# Insert data row by row
for index, row in data.iterrows():
    sql = "INSERT IGNORE INTO order_item (Order_ID, Item_ID, Quantity) VALUES (%s, %s, %s)"
    cursor.execute(sql, (row['Order_ID'], row['Item_ID'], row['Quantity']))


# Commit changes and re-enable foreign key checks
conn.commit()
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

# Close connection
conn.close()
