{{
    config(
        materialized='table',
        partition_by={"field": "order_customer_id", "data_type": "integer"}
    )
}}

WITH fraud_detection AS (
    SELECT
        order_customer_id,
        AVG(order_item_total) AS avg_order_total,
        COUNT(*) AS num_orders
    FROM {{ ref('dim_order') }}
    WHERE order_item_total > 0
      AND order_customer_id IS NOT NULL
    GROUP BY order_customer_id
)
SELECT *
FROM fraud_detection
ORDER BY avg_order_total DESC