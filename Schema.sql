
-- Create a new database
CREATE DATABASE IF NOT EXISTS Pizza_terminal;

-- Switch to the newly created database
USE Pizza_terminal;

-- Create Dessert table
CREATE TABLE IF NOT EXISTS Dessert (
    Item_ID VARCHAR(10) PRIMARY KEY,
    IName VARCHAR(30),
    Price DECIMAL(10, 2)
);

-- Create Dipping Sauce table
CREATE TABLE IF NOT EXISTS Dipping_Sauce (
    Item_ID VARCHAR(10) PRIMARY KEY,
    IName VARCHAR(30),
    Price DECIMAL(10, 2)
);

-- Create Wings table
CREATE TABLE IF NOT EXISTS Wings (
    Item_ID VARCHAR(10) PRIMARY KEY,
    IType VARCHAR(30),
    Sauce_Type VARCHAR(30),
    ICount INT,
    Price DECIMAL(10, 2)
);

-- Create Pizza table
CREATE TABLE IF NOT EXISTS Pizza (
    Item_ID VARCHAR(10) PRIMARY KEY,
    Pizza_name VARCHAR(60),
    Size VARCHAR(50),
    Base VARCHAR(30),
    Sauce VARCHAR(30),
    Sauce_Size VARCHAR(50),
    Cooking_instruction VARCHAR(30),
    Cutting_instruction VARCHAR(30),
    Cheese VARCHAR(30),
    Price DECIMAL(10, 2)
);

-- Create Topping table
CREATE TABLE IF NOT EXISTS Topping (
    T_ID INT PRIMARY KEY,
    T_Name VARCHAR(30)
);

-- Create Breadstick table
CREATE TABLE IF NOT EXISTS Breadstick (
    Item_ID VARCHAR(10) PRIMARY KEY,
    IName VARCHAR(30),
    Price DECIMAL(10, 2)
);

-- Create Drink table
CREATE TABLE IF NOT EXISTS Drink (
    Item_ID VARCHAR(10) PRIMARY KEY,
    Drink_name VARCHAR(30),
    DSize VARCHAR(50),
    Price DECIMAL(10, 2)
);

-- Create Employee table
CREATE TABLE IF NOT EXISTS Employee (
    Employee_ID INT PRIMARY KEY,
    EName VARCHAR(255),
    EPosition VARCHAR(50),
    Hire_Date DATE
);

-- Create Address table
CREATE TABLE IF NOT EXISTS Address (
    Address_ID VARCHAR(10) PRIMARY KEY,
    Street_Number INT,
    Street_Name VARCHAR(50),
    City VARCHAR(20),
    Zip_Code VARCHAR(10),
    Address_Zone VARCHAR(5)
);

-- Create Customer table
CREATE TABLE IF NOT EXISTS Customer (
    Customer_ID VARCHAR(10) PRIMARY KEY,
    CFName VARCHAR(20),
	CSName VARCHAR(20),
    Contact VARCHAR(12)
);

-- Create Order table
CREATE TABLE IF NOT EXISTS Ordermain (
    Order_ID Varchar(10) PRIMARY KEY,
    Employee_ID INT,
    ODate DATE,
    OTime TIME,
    Order_Source VARCHAR(30),
    Order_Type VARCHAR(30),
    Subtotal_Price DECIMAL(10, 2),
	Address_id VARCHAR(10),
    Customer_ID VARCHAR(10),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID),
	FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Address_id) REFERENCES Address(address_ID)
);


-- Create Order_Item table
CREATE TABLE IF NOT EXISTS Order_Item (
    
    Item_ID VARCHAR(10),
    Order_ID VARCHAR(10),
    Quantity INT,
    PRIMARY KEY (Item_ID, Order_ID),
    FOREIGN KEY (Item_ID) REFERENCES Pizza(Item_ID),
	FOREIGN KEY (Item_ID) REFERENCES Drink(Item_ID),
	FOREIGN KEY (Item_ID) REFERENCES Breadstick(Item_ID),
    FOREIGN KEY (Item_ID) REFERENCES Wings(Item_ID),
    FOREIGN KEY (Item_ID) REFERENCES dessert(Item_ID),
    FOREIGN KEY (Item_ID) REFERENCES Dipping_Sauce(Item_ID),
    
    FOREIGN KEY (Order_ID) REFERENCES Ordermain(Order_ID)
 	
);
    


-- Create PizzaTopping table
CREATE TABLE if not exists PizzaTopping (
    Item_ID VARCHAR(10), 
    T_ID INT,
    Coverage VARCHAR(30),
    FOREIGN KEY (T_ID) REFERENCES Topping(T_ID),
  
   	FOREIGN KEY (Item_ID) REFERENCES Pizza(Item_ID),
  	PRIMARY KEY (Item_ID, T_ID)
);


-- Create Delivery table
CREATE TABLE If not EXISTS Delivery (
    Del_ID INT PRIMARY KEY,
    Address_Zone VARCHAR(5),
    Charges DECIMAL(10, 2)
);

-- Create Discount table
CREATE TABLE If not EXISTS Discount (
    Dis_ID INT PRIMARY KEY,
    D_name VARCHAR(30),
    Percent DECIMAL(5, 2)
);


-- Create Bill table
CREATE TABLE If not Exists Bill (
    Bill_ID Varchar(10) PRIMARY KEY,
    
    Del_ID INT,
    Dis_ID INT,
    FOREIGN KEY (Bill_ID) REFERENCES Ordermain(Order_ID),
  
  	FOREIGN KEY (Del_ID) REFERENCES Delivery(Del_ID),
  
  	FOREIGN KEY (Dis_ID) REFERENCES Discount(Dis_ID)
);


-- Create Payment table
CREATE TABLE If not Exists Payment (
    Payment_ID INT PRIMARY KEY,
    Bill_ID Varchar(10),
    Payment_Mode VARCHAR(30),
    Tip DECIMAL(10, 2),
    Total_Amount DECIMAL(10, 2),
    FOREIGN KEY (Bill_ID) REFERENCES Bill(Bill_ID)
);
