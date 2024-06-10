-- Inserting data into Dipping_Sauce table
INSERT IGNORE INTO Dipping_Sauce (Item_ID, IName, Price) VALUES 
('DP101', 'Pizza Sauce', 0.99),
('DP102', 'classic Garlic', 1.29),
('DP103', 'Ranch', 1.29),
('DP104', 'Cheese', 1.29),
('DP105', 'Barbecue', 1.29),
('DP106', 'Buffalo', 1.29),
('DP107', 'Honey Mustard', 1.29),
('DP108', 'Blue Cheese', 1.29),
('DP109', 'Spicy Garlic', 1.29),
('DP111', 'burger sauce', 1.29),
('DP112', 'seasoning Pck', 1.29),
('DP113', 'pepperoncinis', 0.99),
('DP110', 'Creamy Garlic', 1.39);

-- Inserting data into Dessert table
INSERT IGNORE INTO Dessert (Item_ID, IName, Price) VALUES 
('DS101', 'Double Chocolate Brownie', 9.99),
('DS102', 'Chocolate Chip Cookie', 9.99),
('DS103', 'Cinnamon Pull-Apart', 9.99),
('DS104', 'Cheesecake', 9.99);


-- Inserting data into Drink table
INSERT IGNORE INTO Drink (Item_ID, Drink_Name, DSize, Price) VALUES 
('DR101', 'Pepsi', '20OZ', 2.99),
('DR102', 'Diet Pepsi', '20OZ', 2.99),
('DR103', '7 Up', '20OZ', 2.99),
('DR104', 'Mountain Dew', '20OZ', 2.99),
('DR105', 'Mug Root Beer', '20OZ', 2.99),
('DR106', 'Brisk Iced Tea', '20OZ', 2.99),
('DR107', 'Aquafina', '20OZ', 1.99),
('DR108', 'Dr Pepper', '20OZ', 2.99),
('DR109', 'Schweppes Ginger Ale', '20OZ', 2.99),
('DR201', 'Pepsi', '2L', 5.49),
('DR202', 'Diet Pepsi', '2L', 5.49),
('DR203', '7 Up', '2L', 5.49),
('DR204', 'Mountain Dew', '2L', 5.49),
('DR205', 'Mug Root Beer', '2L', 5.49),
('DR206', 'Brisk Iced Tea', '2L', 5.49),
('DR207', 'Aquafina', '2L', 2.99),
('DR208', 'Dr Pepper', '2L', 5.49),
('DR209', 'Schweppes Ginger Ale', '2L', 5.49),
('DR301', 'Gatorade Cool Blue', '20OZ', 3.99),
('DR302', 'Gatorade Fruit Punch', '20OZ', 3.99),
('DR303', 'Gatorade Lemon-Lime', '20OZ', 3.99);


-- Inserting data into Wings table
INSERT IGNORE INTO Wings (Item_ID, IType, Sauce_Type, ICount, Price) VALUES 
('WB101', 'Boneless', 'Unsauced', 10, 8.99),
('WB102', 'Boneless', 'Unsauced', 15, 12.99),
('WB103', 'Boneless', 'Unsauced', 30, 22.99),
('WT101', 'Traditional', 'Unsauced', 8, 8.99),
('WT102', 'Traditional', 'Unsauced', 12, 14.99),
('WT103', 'Traditional', 'Unsauced', 24, 22.99),
('WB104', 'Boneless', 'BBQ', 10, 9.99),
('WB105', 'Boneless', 'BBQ', 15, 13.99),
('WB106', 'Boneless', 'BBQ', 30, 23.99),
('WT104', 'Traditional', 'BBQ', 8, 9.99),
('WT105', 'Traditional', 'BBQ', 12, 15.99),
('WT106', 'Traditional', 'BBQ', 24, 23.99),
('WB107', 'Boneless', 'Buffalo', 10, 10.99),
('WB108', 'Boneless', 'Buffalo', 15, 14.99),
('WB109', 'Boneless', 'Buffalo', 30, 24.99),
('WT107', 'Traditional', 'Buffalo', 8, 10.99),
('WT108', 'Traditional', 'Buffalo', 12, 16.99),
('WT109', 'Traditional', 'Buffalo', 24, 24.99),
('WB110', 'Boneless', 'Garlic Parmason', 10, 11.99),
('WB111', 'Boneless', 'Garlic Parmason', 15, 15.99),
('WB112', 'Boneless', 'Garlic Parmason', 30, 25.99),
('WT110', 'Traditional', 'Garlic Parmason', 8, 11.99),
('WT111', 'Traditional', 'Garlic Parmason', 12, 17.99),
('WT112', 'Traditional', 'Garlic Parmason', 24, 25.99),
('WB113', 'Boneless', 'Honey Chipotle', 10, 12.99),
('WB114', 'Boneless', 'Honey Chipotle', 15, 16.99),
('WB115', 'Boneless', 'Honey Chipotle', 30, 26.99),
('WT113', 'Traditional', 'Honey Chipotle', 8, 12.99),
('WT114', 'Traditional', 'Honey Chipotle', 12, 18.99),
('WT115', 'Traditional', 'Honey Chipotle', 24, 26.99);

-- Inserting values into the Address table
INSERT IGNORE INTO Address (Address_ID, Street_Number, Street_Name, City, Zip_Code, Address_Zone) 
VALUES 
('SC0000001', 33, 'Main Street', 'Saltcity', '12345', 'IN');
