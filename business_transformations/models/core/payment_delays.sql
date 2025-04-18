{{
    config(
        materialized='table',
        partition_by={"field": "delivery_status", "data_type": "string"}
    )
}}
SELECT
    delivery_status,
    AVG(days_for_shipping_real - days_for_shipping_scheduled) AS avg_payment_delay,
    COUNT(1) AS count_of_orders
FROM {{ ref('dim_shipping') }}
GROUP BY delivery_status