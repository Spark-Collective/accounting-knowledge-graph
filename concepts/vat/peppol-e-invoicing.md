---
type: rule
title: Peppol e-invoicing (mandatory B2B from 2026)
description: Structured e-invoices via Peppol are mandatory for Belgian B2B from 1 January 2026.
tags: [vat, peppol, bv, eenmanszaak, belgium, verify-live]
sources: [https://financien.belgium.be]
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2026-09-30
---

# Peppol e-invoicing (mandatory B2B from 2026)

From **1 January 2026**, structured electronic invoicing via the **Peppol** network is mandatory for **B2B invoices between Belgian VAT payers**. The Royal Decree of 18 June 2025 made it definitive.

## The rule (verify_live)

- **Scope:** all Belgian VAT payers, **regardless of size or sector** , including small/exempt businesses under the EUR 25,000 franchise. [search]
- **Format:** structured **Peppol BIS 3.0** (UBL-based), sent and received over the Peppol network. **PDF and paper are no longer valid B2B invoices.** Credit notes follow the same rules. [search]
- **Out of scope:** B2C invoices. **B2G** has been mandatory since March 2024. [search]
- **Penalties:** non-compliance can be fined (reported up to ~EUR 5,000). [search]

> Confirm the current rules, any phase-in, and penalty amounts with [FOD Financiën](https://financien.belgium.be).

## Practice

The business needs a Peppol-capable channel (an access point) to send and receive. Spark routes invoices through a Peppol access point and maps the accounting system's invoice data to the structured format , so the agent's job is to produce clean, complete invoice data (parties, VAT treatment, lines) and confirm delivery, not to hand-build UBL.

Reverse-charge and intracommunity invoices ([[intracommunity-and-medecontractant]]) still need their legal mentions inside the structured invoice.

## See also

[[intracommunity-and-medecontractant]] · [[periodic-vat-return-intervat]] · [[vat-rates-and-regimes]]

Source: linkup search synthesis; verify against FOD Financiën.
