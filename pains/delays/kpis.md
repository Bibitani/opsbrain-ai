# Pain Module: Delivery Delays — KPIs

## Core KPIs

1. Delay Rate
Definition:
Delayed deliveries / Total deliveries

Purpose:
Primary health indicator of delivery performance.

---

2. SLA Breach Rate
Definition:
Deliveries where delivery_time_hours > expected_time_hours

Purpose:
Objective measure of failure (even if delayed flag is wrong).

---

3. Average Delay Severity
Definition:
AVG(delivery_time_hours - expected_time_hours)
(Only for breached deliveries)

Purpose:
Measures how bad delays are, not just how frequent.

---

4. Delay Concentration
Dimensions:
- Region
- Delivery Partner
- Weather Condition
- Vehicle Type

Purpose:
Identify where delays cluster.

---

5. Partner Reliability Score
Definition:
1 - (Partner Delay Rate)

Purpose:
Rank partners by operational reliability.
