
-- Insert data into Delivery table
INSERT ignore INTO Delivery (Del_ID, Address_Zone, Charges)
VALUES
    (101, 'N1', 3.99),
    (102, 'N2', 5.49),
    (103, 'S1', 3.99),
    (104, 'S2', 5.49),
    (105, 'S3', 5.49),
    (106, 'E1', 3.99),
    (107, 'E2', 5.49),
    (108, 'W1', 3.99),
    (109, 'W2', 5.49),
    (110, 'W3', 5.49),
    (111, 'W4', 6.99),
    (112, 'NE1', 3.99),
    (113, 'NE2', 5.49),
    (114, 'NW1', 3.99),
    (115, 'NW2', 5.49),
    (116, 'NW3', 5.49),
    (117, 'NW4', 6.99),
    (118, 'NW5', 6.99),
    (119, 'NW6', 6.99),
    (120, 'SE1', 3.99),
    (121, 'SE2', 5.49),
    (122, 'SE3', 5.49),
    (123, 'SW1', 3.99),
    (124, 'SW2', 5.49),
    (125, 'SW3', 5.49),
    (126, 'SW4', 6.99),
    (127, 'SW5', 6.99);

-- Insert data into Discount table
INSERT ignore INTO Discount (Dis_ID, D_name, Percent)
VALUES
    (1, 'Student Special', 10.00),
    (2, 'Family Feast Discount', 15.00),
    (3, 'Midweek Madness', 20.00),
    (4, 'Pizza Party', 25.00),
    (5, 'Buy One Get One Free (BOGO)', 50.00),
    (6, 'Loyal Customer Discount', 20.00),
    (7, 'Flash Pizza Sale', 10.00);
    
    -- Inserting data into Topping table
INSERT INTO Topping (T_ID, T_Name) VALUES 
(1, 'Bacon'),
(2, 'Banana peppers'),
(3, 'Beef'),
(4, 'Black olives'),
(5, 'Canadian bacon'),
(6, 'Chicken'),
(7, 'Cuppy Roni'),
(8, 'Italian sausage'),
(9, 'Jalapenos'),
(10, 'Green olives'),
(11, 'Green peppers'),
(12, 'Pepperoni'),
(13, 'Pineapple'),
(14, 'Mushrooms'),
(15, 'Onions'),
(16, 'Spinach'),
(17, 'Feta cheese'),
(18, 'Extra cheese'),
(19, 'Salami'),
(20, 'Sausage'),
(21, 'Spinach'),
(22, 'Meatball'),
(23, 'Steak'),
(24, '2 Cheese'),
(25, '3 Cheese');


-- Inserting data into Breadstick table
INSERT INTO Breadstick (Item_ID, IName, Price) VALUES 
('BS101', 'Oreo Bites', 7.99),
('BS102', 'Chicken Bites', 7.99),
('BS103', 'Cuppy Roni Bites', 7.99),
('BS104', 'Jalapeno Bites', 7.99),
('BS105', 'Cheese Sticks (10 inch)', 8.99),
('BS106', 'Cheese Sticks (12 inch)', 9.99),
('BS107', 'Stuffed Cheese Sticks', 10.99),
('BS108', 'Tucson Cheese Sticks (10 inch)', 10.99),
('BS109', 'Tucson Cheese Sticks (12 inch)', 12.99),
('BS110', 'Stuffed Bacon Cheese Sticks', 12.99),
('BS112', 'Bacon Cheese Sticks (10 inch)', 11.99),
('BS111', 'Bacon Cheese Sticks (12 inch)', 13.99),
('BS114', 'Breadstick', 9.99),
('BS113', 'Parmesan Stick', 10.99),
('BS116', 'Garlic Knot', 7.99),
('BS115', 'Cheddar Garlic Knot', 9.99);

-- Inserting data into Employee table
INSERT IGNORE INTO Employee (Employee_ID, EName, EPosition, Hire_Date) VALUES 
(10001, 'John Doe', 'General Manager', '2022-01-01'),
(10002, 'Jane Smith', 'Supervisor', '2021-06-15'),
(10003, 'Alex Johnson', 'Supervisor', '2021-07-20'),
(10004, 'Emily Brown', 'Instore Member', '2019-08-05'),
(10005, 'Michael Davis', 'Instore Member', '2019-09-10'),
(10006, 'Jessica Wilson', 'Instore Member', '2019-10-15'),
(10007, 'David Martinez', 'Instore Member', '2019-11-20'),
(10008, 'Amanda Jones', 'Instore Member', '2020-02-25'),
(10009, 'Matthew Taylor', 'Instore Member', '2020-03-01'),
(10010, 'Sarah Garcia', 'Instore Member', '2020-03-05'),
(10011, 'Robert Rodriguez', 'Instore Member', '2020-03-10'),
(10012, 'Jennifer Hernandez', 'Instore Member', '2020-03-15'),
(10013, 'Daniel Martinez', 'Instore Member', '2020-03-20'),
(10014, 'Emma Lopez', 'Instore Member', '2020-03-25'),
(10015, 'Christopher Perez', 'Instore Member', '2020-04-01'),
(10016, 'Ashley Gonzalez', 'Delivery Driver', '2018-04-05'),
(10017, 'Joshua Wilson', 'Delivery Driver', '2018-05-10'),
(10018, 'Madison Scott', 'Delivery Driver', '2018-06-15'),
(10019, 'Ryan King', 'Delivery Driver', '2018-07-20'),
(10020, 'Olivia Martinez', 'Delivery Driver', '2018-08-25');