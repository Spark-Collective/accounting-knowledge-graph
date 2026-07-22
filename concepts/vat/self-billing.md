---
type: rule
title: Self-billing (self-facturatie)
description: The customer issues the invoice on the supplier's behalf; allowed for VAT under conditions, and must go via Peppol from 2026.
tags: [vat, peppol, bv, belgium, verify-live]
sources: [https://financien.belgium.be]
aliases: ["self-billing", "self-facturatie", "autofacturation", "selffacturatie"]
confidence: medium
created: 2026-06-29
updated: 2026-06-29
verify_live: true
review_after: 2027-01-31
relations:
  affects: [peppol-e-invoicing]
---

# Self-billing (self-facturatie)

**Self-billing** = the **customer issues the invoice on the supplier's behalf**. Common with large platforms and clients handling many freelancers (Deliveroo, Uber, Upwork, Creative Shelter, big consultancies).

## The rule (verify_live)

- **Allowed for VAT** under conditions: a **prior agreement** between the two parties and an **acceptance procedure** for each invoice. The **supplier remains liable for the VAT** on the supply. [search]
- **From 1 January 2026:** every B2B invoice, **including self-bills, must be sent and received via Peppol** ([[peppol-e-invoicing]]). [search]
- The self-bill still carries all the normal invoice mentions (VAT numbers, and the reverse-charge mention where relevant , see [[intracommunity-and-medecontractant]]).

> Confirm the current VAT conditions and the Peppol requirement with [FOD Financiën](https://financien.belgium.be).

## Why it matters

If a big client self-bills a one-person BV, the BV must still **check the invoice is correct** (VAT, amounts) and that it flows through Peppol , the client generated it, but the BV owns the VAT position. The agent books it like any sales invoice.

## See also

[[peppol-e-invoicing]] · [[booking-a-purchase-invoice]] · [[intracommunity-and-medecontractant]]

Source: distilled from FOD Financiën VAT self-billing rules. Verify live.
