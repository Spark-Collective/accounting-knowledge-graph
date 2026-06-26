---
type: workflow
title: Year-end close
description: The SOP to close the year, compute the tax, and file the annual accounts + return.
tags: [workflows, year-end, corporate-tax, bv, belgium]
sources: []
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Workflow: year-end close

The annual routine that turns twelve [[month-end-close|monthly closes]] into the filed annual accounts and tax return. Prepare for review; the operator (and accountant) approve.

## Steps

1. **Final reconciliation** , all twelve months booked and reconciled ([[coda-bank-reconciliation]]); no open items unexplained.
2. **Closing entries** , post the year-end set ([[closing-entries]]): depreciation, impairments, provisions, cut-off, inventory, accruals.
3. **Draft the result** , produce the balance sheet + P&L; sanity-check vs prior year.
4. **Corporate-tax computation** , base = accounting profit + disallowed expenses (verworpen uitgaven) + dividends, minus deductions; apply the rate ([[corporate-tax-basics]]); reconcile against [[advance-payments|advance payments]]; book the tax provision.
5. **If distributing** , verify the [[distribution-test-advies|net-asset + liquidity tests]] pass **before** any dividend/[[vvpr-bis-dividends|VVPR-bis]].
6. **Assemble the annual accounts** , the micro/abridged model per [[company-size-criteria|size]]; file in XBRL at the NBB within the deadline ([[annual-accounts-nbb]]).
7. **File the corporate-tax return** (Biztax) and any related forms; archive everything ([[document-retention]]).

## Gate

- The balance sheet **balances**; the result ties to the P&L.
- For a payout, the **distribution test passes** , otherwise stop.
- The **NBB and tax deadlines** are met (verify the current dates).
- Figures going to the authority are **verified live and operator-approved**, never auto-filed.

## See also

[[closing-entries]] · [[annual-accounts-nbb]] · [[corporate-tax-basics]] · [[month-end-close]]
