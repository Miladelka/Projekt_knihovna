-- nejde spustit

SELECT
    r.admin_serial,
    SUM(DATEDIFF(DAY, r.date_request, v.date_borrow)) AS DayDifference
FROM vypujcky v
JOIN rezervace_fixed r ON v.Id_No = r.Id_No
    AND v.admin_serial = r.admin_serial
    AND r.availability LIKE N'nedostupne'
    AND DATEDIFF(DAY, r.date_request, v.date_borrow) >= 0
WHERE v.Id_No IN (SELECT Id_No FROM rezervace_fixed)
    AND v.admin_serial IN (SELECT admin_serial FROM rezervace_fixed)
    AND v.date_borrow = (
        SELECT MIN(date_borrow)
        FROM vypujcky v2
        WHERE v2.Id_No = v.Id_No
        AND v2.admin_serial = v.admin_serial
        AND DATEDIFF(DAY, r.date_request, v2.date_borrow) >= 0
    )
GROUP BY
    r.admin_serial
ORDER BY
    DayDifference DESC

    -- AND v.Id_No = N'00824641707537'
    -- AND v.admin_serial = N'000178047000010'