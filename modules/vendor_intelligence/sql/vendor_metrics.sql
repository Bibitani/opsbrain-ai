SELECT
    delivery_partner AS vendor,
    COUNT(*) AS total_deliveries,

    ROUND(
        100.0 * SUM(CASE WHEN delayed = FALSE THEN 1 ELSE 0 END) 
        / COUNT(*),
        2
    ) AS on_time_rate_percent,

    ROUND(AVG(delivery_cost), 2) AS avg_delivery_cost,

    ROUND(AVG(delivery_cost / NULLIF(distance_km, 0)), 2) AS avg_cost_per_km,

    ROUND(AVG(delivery_rating), 2) AS avg_rating

FROM deliveries
GROUP BY delivery_partner;

