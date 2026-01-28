SELECT
  COUNT(*) AS total_deliveries,
  SUM(CASE WHEN delayed THEN 1 ELSE 0 END) AS delayed_deliveries,
  ROUND(
    SUM(CASE WHEN delayed THEN 1 ELSE 0 END)::NUMERIC / COUNT(*) * 100,
    2
  ) AS delay_rate_percent
FROM deliveries;



SELECT
  COUNT(*) AS total_deliveries,
  SUM(CASE WHEN delivery_time_hours > expected_time_hours THEN 1 ELSE 0 END)
    AS sla_breaches,
  ROUND(
    SUM(CASE WHEN delivery_time_hours > expected_time_hours THEN 1 ELSE 0 END)::NUMERIC
    / COUNT(*) * 100,
    2
  ) AS sla_breach_rate_percent
FROM deliveries;


SELECT
  ROUND(
    AVG(delivery_time_hours - expected_time_hours),
    2
  ) AS avg_delay_severity_hours
FROM deliveries
WHERE delivery_time_hours > expected_time_hours;




SELECT
  region,
  COUNT(*) AS total,
  SUM(CASE WHEN delayed THEN 1 ELSE 0 END) AS delayed,
  ROUND(
    SUM(CASE WHEN delayed THEN 1 ELSE 0 END)::NUMERIC / COUNT(*) * 100,
    2
  ) AS delay_rate_percent
FROM deliveries
GROUP BY region
ORDER BY delay_rate_percent DESC;



SELECT
  delivery_partner,
  COUNT(*) AS total,
  SUM(CASE WHEN delayed THEN 1 ELSE 0 END) AS delayed,
  ROUND(
    1 - (
      SUM(CASE WHEN delayed THEN 1 ELSE 0 END)::NUMERIC / COUNT(*)
    ),
    2
  ) AS reliability_score
FROM deliveries
GROUP BY delivery_partner
ORDER BY reliability_score ASC;


