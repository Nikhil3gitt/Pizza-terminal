UPDATE IGNORE Payment p
JOIN (
    SELECT om.Order_ID,
           (((om.Subtotal_price * (100 - d.Percent) / 100) + dv.Charges) * 1.08) + p.Tip AS Total_Amount
    FROM Ordermain om
    JOIN Bill B ON B.Bill_ID = om.Order_ID
    JOIN Discount d ON B.Dis_ID = d.Dis_ID
    JOIN Delivery dv ON B.Del_ID = dv.Del_ID
    JOIN Payment P ON P.Bill_ID = om.Order_ID
    
) AS calculated_cost ON p.Bill_ID = calculated_cost.Order_ID
SET p.Total_Amount = calculated_cost.Total_Amount;
