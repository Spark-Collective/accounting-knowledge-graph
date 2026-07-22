---
type: rule
title: Withholding obligation on contractors (inhoudingsplicht)
description: Before paying a construction/cleaning/security contractor, check for tax + social debts and withhold to the authority if any (art. 30bis/30ter).
tags: [bookkeeping, bv, belgium, verify-live]
sources: [https://financien.belgium.be, https://www.rsz.fgov.be]
aliases: ["inhoudingsplicht", "obligation de retenue", "30bis", "30ter", "aannemer met schulden"]
confidence: medium
created: 2026-06-29
updated: 2026-06-29
verify_live: true
review_after: 2026-12-31
relations:
  affects: [booking-a-purchase-invoice]
---

# Withholding obligation on contractors (inhoudingsplicht)

When you receive an invoice from a contractor in **construction (art. 30bis), or cleaning / security (art. 30ter)**, you must , **before paying** , check whether they have debts. If so, you pay part of the invoice to the authority instead of to the contractor. An easily-missed joint-liability trap.

## The rule (verify_live)

- **Check before paying:** query the official database for the contractor's debts. **New since 1 May 2026, a third category was added** , debts for self-employed social contributions (RSVZ/INASTI) , on top of tax debts and RSZ (employee) social debts. Three categories to check. [search]
- **If debts exist, withhold and remit to the authority:** roughly **15%** (excl. VAT) for tax debts and **35%** for social-security debts , paid directly to FOD/RSZ, the remainder to the contractor. [search]
- **Scope:** works in immovable state (construction), plus the cleaning and security sectors. [search]
- **If you skip it:** you become **jointly liable** for the debt, plus a surcharge. [search]

> Percentages, the check procedure, and the sector scope change. **Run the official check and confirm with [FOD Financiën](https://financien.belgium.be) / RSZ before paying** such an invoice.

## Why it matters

A real, silent liability whenever a BV pays a construction / cleaning / security supplier. The agent must flag these invoices in [[booking-a-purchase-invoice]] and run the debt check before the payment goes out.

## See also

[[booking-a-purchase-invoice]] · [[coda-bank-reconciliation]] · [[social-contributions-self-employed]]

Source: distilled from FOD Financiën / RSZ rules (art. 30bis/30ter WIB92); topic surfaced via a secondary explainer. Verify all figures live.
