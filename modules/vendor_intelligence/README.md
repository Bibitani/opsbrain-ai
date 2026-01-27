# Pain Module 2 — Vendor Performance & Cost Leakage

This module identifies underperforming and overpriced delivery partners by analyzing
cost, reliability, and service quality. It enables OpsBrain to recommend
vendor-level operational actions such as reallocation, escalation, or replacement.

## Scope

This module answers questions like:
- Which delivery partners are the least reliable?
- Which vendors are the most expensive per km?
- Are we overpaying low-performing partners?
- Which partner gives the best cost-to-performance ratio?
- Which vendor should we reduce dependency on?

It does NOT handle:
- City-level delay root cause analysis  
- Route-level delay diagnostics  
(Handled by the Delivery Delay module)

## Core KPIs

- Average Cost per KM  
- On-Time Delivery Rate (%)  
- Average Delay Days per Vendor  
- Average Customer Rating per Vendor  
- Cost per Successful Delivery  
- Vendor Risk Score (composite: high cost + high delay + low rating)
Add Vendor Intelligence pain module skeleton
