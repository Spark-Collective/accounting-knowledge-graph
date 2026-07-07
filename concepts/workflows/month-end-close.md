---
type: workflow
title: Month-end close
description: The monthly SOP to get the books complete, reconciled, and review-ready.
tags: [workflows, bookkeeping, vat, belgium]
sources: []
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
aliases: ["maandafsluiting", "maandelijkse afsluiting"]
---

# Workflow: month-end close

The recurring routine that keeps the books current, so the [[vat-period-prep|VAT return]] and year-end are low-effort. Run it monthly.

## Steps

1. **Collect** all documents for the month: purchase invoices, sales invoices, bank statements, receipts.
2. **Book purchases** ([[booking-a-purchase-invoice]]) and **sales** (with the correct VAT treatment, incl. [[intracommunity-and-medecontractant|reverse charge]]).
3. **Reconcile the bank** , import the statement (CODA) and match every line to an invoice or entry; investigate unmatched items. (See planned `coda-bank-reconciliation`.)
4. **Check the VAT accounts** (411 input / 451 output, see [[chart-of-accounts-mar]]) , do they reflect the month's invoices?
5. **Review open items** , aged debtors (40) and creditors (44); flag overdue.
6. **Sanity pass** , unusual amounts, missing supplier VAT numbers, costs with uncertain [[restaurant-and-meals|deductibility]].
7. **Summarise** , a short month report (revenue, costs, cash, flags) for the operator.

## Gate

- **The bank reconciles** and there are **no unbooked documents** for the month.
- VAT accounts tie to the booked invoices.
- Any anomaly is surfaced in the summary, not silently closed.

## See also

[[booking-a-purchase-invoice]] · [[vat-period-prep]] · [[chart-of-accounts-mar]]
