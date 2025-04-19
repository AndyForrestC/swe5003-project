{{
    config(
        materialized='table',
        partition_by={"field": "department_id", "data_type": "integer"},
        cluster_by='department_name'
    )
}}
WITH order_aggregates AS (
    SELECT
        o.department_id,
        o.product_card_id,
        SUM(o.order_item_total) AS total_committed_funds,
        SUM(CASE WHEN o.order_status = 'COMPLETE' THEN 1 ELSE 0 END) AS completed_orders,
        COUNT(1) AS total_orders
    FROM {{ ref('dim_order') }} o
    GROUP BY o.department_id, o.product_card_id
),
distinct_departments AS (
    SELECT DISTINCT department_id, department_name, market
    FROM {{ ref('dim_department') }}
),
distinct_products AS (
    SELECT DISTINCT product_card_id, category_name
    FROM {{ ref('dim_product') }}
),
department_market_category AS (
    SELECT
        d.department_name,
        d.market,
        p.category_name,
        oa.total_committed_funds,
        oa.completed_orders,
        oa.total_orders
    FROM order_aggregates oa
    JOIN distinct_departments d ON oa.department_id = d.department_id
    JOIN distinct_products p ON oa.product_card_id = p.product_card_id
)
SELECT
    department_name,
    market,
    category_name,
    MAX(total_committed_funds) AS total_committed_funds,
    CASE 
        WHEN SUM(total_orders) = 0 THEN 0
        ELSE CAST(SUM(completed_orders) AS FLOAT64) / SUM(total_orders)
    END AS commitment_fulfillment_rate
FROM department_market_category
GROUP BY department_name, market, category_name
