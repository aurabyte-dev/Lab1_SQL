# Exploring Sakila database

## Movis lengths

```sql films
 SELECT
    title,
    rating,
    length,
    description

FROM sakila.film;

```


## Top customers

```sql rental_customers
 SELECT
    customer,
    sum(amount) as total_spend
    length,
    description

FROM sakila.film;

```

<BarChart
    data={orders_by_category}
    title="Sales by Month, {inputs.category.label}"
    x=month
    y=sales_usd
    series=category
/>