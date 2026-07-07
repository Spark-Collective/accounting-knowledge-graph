---
type: workflow
title: Booking a purchase invoice
description: The SOP for capturing, splitting VAT, classifying deductibility, and booking a supplier invoice.
tags: [workflows, bookkeeping, vat, deductible-costs, belgium]
sources: []
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
aliases: ["aankoopfactuur boeken", "aankoopfactuur inboeken", "factuur inboeken", "btw splitsing"]
---

# Workflow: booking a purchase invoice

The most frequent agent action. Each purchase invoice is captured, classified, and booked , with the VAT split and the deductibility flagged, never assumed.

## Steps

1. **Capture + validate.** Read supplier, date, invoice number, net/VAT/gross. Check the **supplier VAT number** and that the company's own details are correct. Reject duplicates.
2. **Determine the cost nature** and the right class-6 account ([[chart-of-accounts-mar]]).
3. **Classify deductibility** , apply the relevant rule page: [[restaurant-and-meals]] (~69%, VAT not deductible), [[car-and-mobility]], [[ict-equipment]] (VAT ~75%), [[sponsoring]], etc. Flag the non-deductible fraction for the year-end add-back; **do not** exclude it from the booking.
4. **Split VAT.** Book deductible input VAT to **411**; book non-deductible VAT as part of the cost. Watch caps (car, ICT) and restaurant (no VAT deduction).
5. **Reverse charge?** If the invoice is medecontractant/intracommunity ([[intracommunity-and-medecontractant]]), there is no supplier VAT , self-account in the VAT return instead.
6. **Book the counterpart** to the supplier account (44) and **match the payment** from the bank ([[month-end-close]] / CODA).
7. **Archive** the document per [[document-retention]] (10 years).

## Gate

- Debit = credit; VAT correctly split; deductibility category recorded; supplier VAT number valid.
- **Anything ambiguous (deductibility, reverse charge) is flagged for review, not guessed.**

## See also

[[month-end-close]] · [[chart-of-accounts-mar]] · [[intracommunity-and-medecontractant]]
