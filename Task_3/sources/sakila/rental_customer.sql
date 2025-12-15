SELECT
    c.first_name || ' ' || c.last_name AS customer,
    COUNT(p.amount) AS spend
FROM
    staging.customer c
    JOIN staging.payment p ON p.customer_id = c.customer_id