---
type: reference
title: Supplier pattern library (transaction classification)
description: Common Belgian suppliers/transaction types and their default account + VAT + deductibility, to speed classification.
tags: [workflows, deductible-costs, vat, belgium]
relations:
  part_of: [booking-a-purchase-invoice]
  affects: [expense-categorization]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Supplier pattern library (transaction classification)

Default classifications for recurring Belgian suppliers/transaction types , a fast path for [[booking-a-purchase-invoice]] and [[expense-categorization]]. **Defaults, not rulings:** apply the linked rule page for the actual deductible % and VAT, follow the [[classification-protocol]] when a line doesn't match, and never auto-maximise.

| Supplier / type | Default account | VAT | Deductibility |
|---|---|---|---|
| Fuel stations (Total, Q8, Esso) | car costs (61) | partial (car cap); only on a **fuel-card invoice**, not a till receipt | CO2-based ([[car-and-mobility]]) |
| EV charging | car costs (61) | partial | [[ev-charging-reimbursement]] |
| Telecom (Proximus, Orange, Telenet) | services (61) | deductible (business share) | business use; VAA if private ([[benefits-in-kind-vaa]]) |
| Restaurants / Deliveroo / Uber Eats | restaurant cost (61) | **not deductible** | ~69% ([[restaurant-and-meals]]) |
| SaaS / cloud (Google, Microsoft, Adobe, AWS) | services (61) | **reverse charge** if EU non-BE ([[intracommunity-and-medecontractant]]) | deductible |
| Office supplies / ICT (Coolblue, Amazon, Bol) | supplies (61) / asset (2) | deductible; ICT VAT capped ~75% ([[ict-equipment]]) | 100% (ICT) |
| Rail / parking (NMBS, parkings) | travel (61) | usually **no recovery** (no valid invoice, [[vat-deduction-conditions]]) | cost deductible |
| Accountant / lawyer | fees (61) | deductible | deductible |
| Insurance | (61) | **exempt** (no VAT) | deductible |
| Bank charges (KBC, BNP, Belfius) | financial charges (65) | no VAT | deductible |
| Social secretariat / HR | fees (61) | deductible | deductible |

## See also

[[booking-a-purchase-invoice]] · [[expense-categorization]] · [[classification-protocol]]

Note: Spark's own classification list (clean-room), pointing at the rule pages for the numbers. Inspired by OpenAccountants' supplier patterns; no AGPL content copied.
