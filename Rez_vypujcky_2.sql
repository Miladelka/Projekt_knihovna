-- Rezervace versus uskutečněné výpůjčky, včetně duplikovaných řádků, 74.745 řad, jiný příkaz

SELECT 
    *, 
    DATEDIFF(DAY, r.date_request, v.date_borrow) AS DayDifference
FROM vypujcky v
JOIN Rezervace_komplet AS r ON v.Id_No = r.Id_No 
    AND v.admin_serial = r.admin_serial 
WHERE v.Id_No IN (SELECT Id_No FROM Rezervace_komplet)
    AND v.admin_serial IN (SELECT admin_serial FROM Rezervace_komplet)
    AND v.date_borrow = (
        SELECT TOP 1 date_borrow
        FROM Vypujcky_komplet v2 
        WHERE v2.Id_No = v.Id_No
        AND v2.admin_serial = v.admin_serial
        AND DATEDIFF(DAY, r.date_request, v2.date_borrow) >= 0
        ORDER BY DATEDIFF(DAY, r.date_request, v2.date_borrow) ASC
    )