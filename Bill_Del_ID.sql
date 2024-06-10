UPDATE Bill b
JOIN Ordermain om ON b.Bill_ID = om.Order_ID
JOIN Address a ON om.Address_ID = a.Address_ID
JOIN Delivery d ON a.Address_Zone = d.Address_Zone
SET b.Del_ID = d.Del_ID;
