UPDATE Ordermain om
JOIN (
    SELECT oi.Order_ID, 
           SUM((CASE WHEN oi.Item_ID IN (SELECT Item_ID FROM Pizza) THEN p.Price
                     WHEN oi.Item_ID IN (SELECT Item_ID FROM Breadstick) THEN b.Price
                     WHEN oi.Item_ID IN (SELECT Item_ID FROM Drink) THEN d.Price
                     WHEN oi.Item_ID IN (SELECT Item_ID FROM Dipping_Sauce) THEN ds.Price
                     WHEN oi.Item_ID IN (SELECT Item_ID FROM Dessert) THEN de.Price
                     WHEN oi.Item_ID IN (SELECT Item_ID FROM Wings) THEN w.Price
                END) * oi.Quantity) AS Subtotal
    FROM order_item oi
    LEFT JOIN Pizza p ON oi.Item_ID = p.Item_ID
    LEFT JOIN Breadstick b ON oi.Item_ID = b.Item_ID
    LEFT JOIN Drink d ON oi.Item_ID = d.Item_ID
    LEFT JOIN Dipping_Sauce ds ON oi.Item_ID = ds.Item_ID
    LEFT JOIN Dessert de ON oi.Item_ID = de.Item_ID
    LEFT JOIN Wings w ON oi.Item_ID = w.Item_ID
    GROUP BY oi.Order_ID
) AS Subtotals ON om.Order_ID = Subtotals.Order_ID
SET om.Subtotal_price = Subtotals.Subtotal;
