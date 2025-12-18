# Exploring Sakila database

## Movies longer than 180 minutes

```sql long_film
SELECT
    title,
    length
FROM sakila.film
WHERE length > 180;
```


## Movies with the word 'LOVE'

```sql love_film
 SELECT
        title,
        rating,
        length,
        description
    FROM
        sakila.film
    WHERE
        title LIKE '%LOVE%';
```

## Statistics: Film lengths

```sql film_lengths
SELECT
    MIN(length) AS shortest_length,
    MAX(length) AS longest_length,
    ROUND(AVG(length)) AS average_length,
    ROUND(MEDIAN(length)) AS median_length
    FROM
        sakila.film
```


## Rental cost: Top 10 most expensive movies (price per day)

```sql rental_cost
SELECT
    title,
    ROUND(rental_rate / rental_duration) AS daily_rental_cost
    FROM
        sakila.film
    ORDER BY daily_rental_cost DESC
    LIMIT 10
```

## Top actors

```sql top_actors
SELECT 
            a.first_name,
            a.last_name,
            COUNT(fa.film_id) AS nr_films
        
FROM sakila.actor a
LEFT JOIN sakila.film_actor fa ON a.actor_id = fa.actor_id
        GROUP BY a.actor_id, a.first_name, a.last_name
        ORDER BY nr_films DESC
        LIMIT 10 
```

## Top customers
```sql top_customers
SELECT
            c.first_name || ' ' || c.last_name AS customer,
            ROUND(SUM(p.amount)) AS spend
        FROM
            sakila.customers c
        JOIN sakila.payments p ON p.customer_id = c.customer_id
        GROUP BY customer
        ORDER BY spend DESC
        LIMIT 5  
```
<BarChart
    data={top_customers}
    title="Top customers"
    x=customer
    y=spend    
    swapXY=true
    labels=true
/>

## Revenue per film category

```sql revenue_film_category
SELECT 
            name AS category,
            ROUND(SUM(p.amount)) AS revenue
        FROM sakila.category c
        JOIN sakila.film_category fc ON c.category_id = fc.category_id
        JOIN sakila.film f ON fc.film_id = f.film_id
        JOIN sakila.inventory i ON f.film_id = i.film_id      
        JOIN sakila.rental r ON i.inventory_id = r.inventory_id  
        JOIN sakila.payments p ON r.rental_id = p.rental_id
        GROUP BY category
        ORDER BY revenue DESC 
```


<BarChart
    data={revenue_film_category}
    title="Revenue per category"
    x=category
    y=revenue    
    swapXY=true
    labels=true
/>