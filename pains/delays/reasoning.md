# Delay Reasoning Logic (OpsBrain)

## Ground Truth Rules
- SLA breach overrides delayed flag
- SQL results are authoritative
- LLM only explains, never invents

## Reasoning Flow
1. Check overall delay & SLA breach rate
2. Identify top regions contributing to delays
3. Identify partners with low reliability
4. Cross-check weather and vehicle patterns
5. Explain causes with evidence (numbers)

## Output Style
- State the problem clearly
- Cite metrics
- Explain why it happened
- Avoid speculation


# OpsBrain Delay Reasoning — Delivery Delays

## 1. Problem Statement
The overall delivery delay rate is approximately 26–27%, indicating a persistent, system-level operational issue rather than isolated or random failures.

---

## 2. Key Observations

### 2.1 Vehicle Type
- Delay rates across all vehicle types range narrowly between 26.1% and 27.0%.
- No vehicle category stands out as a significant contributor to delays.

Inference:
Vehicle selection is not a meaningful driver of delivery delays.

---

### 2.2 Regions
- Regional delay rates show limited variation (≈1.5% spread).
- Central region exhibits marginally higher delays, while the East performs slightly better.

Inference:
Geographic factors contribute minimally; higher delays are likely due to demand concentration rather than regional infrastructure failure.

---

### 2.3 Delivery Partners
- Delay rates vary noticeably across partners (≈3.5% spread).
- Certain partners (e.g., Xpressbees, Ekart) consistently underperform, while others (e.g., Delhivery, FedEx) show stronger reliability.

Inference:
Partner execution quality is a key internal driver of delays and represents a controllable operational lever.

---

### 2.4 Weather Conditions
- Weather shows the highest variance in delay rates.
- Stormy (41.45%) and rainy (37.35%) conditions drastically increase delays.
- Clear, cold, and hot conditions perform significantly better (<18%).

Inference:
Weather is the strongest external amplifier of delivery delays but is not directly controllable.

---

## 3. Root Cause Ranking (by impact)

1. Weather conditions (external, high impact)
2. Delivery partner performance (internal, controllable)
3. Regional load imbalance (internal, partially controllable)
4. Vehicle type (minimal impact)

---

## 4. OpsBrain Conclusion
Delivery delays are primarily driven by adverse weather conditions, with delivery partner execution quality acting as the most significant controllable internal factor. Vehicle type has negligible influence, and regional effects are secondary.

Operational improvements should prioritize partner performance management and proactive planning around adverse weather conditions rather than changes to vehicle allocation.

---

## 5. Suggested Actions (Non-Automated)
- Monitor and manage underperforming delivery partners through SLA reviews and incentives.
- Introduce weather-aware operational buffers and contingency planning.
- Rebalance load in regions with marginally higher delay concentration during peak periods.

