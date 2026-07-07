---
type: rule
title: Advance payments (voorafbetalingen)
description: Prepay corporate tax quarterly or face a surcharge; rates set yearly.
tags: [corporate-tax, bv, belgium, verify-live]
sources: [https://financien.belgium.be]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
aliases: ["voorafbetalingen", "vermeerdering vermijden", "voorafbetaling vennootschapsbelasting"]
---

# Advance payments (voorafbetalingen)

A company is expected to **prepay** its corporate tax during the year in quarterly instalments (VA1-VA4). Prepaying too little triggers a **surcharge** (*belastingvermeerdering*) on the tax due , effectively a penalty for under-prepayment.

## The rule (verify_live)

- **Four quarterly due dates** for a calendar-year company , roughly **10 April, 10 July, 10 October, and 20 December**. A non-calendar financial year shifts these. [fod]
- **Under-prepayment -> surcharge.** Earlier payments earn a higher credit (bonification logic), so VA1 counts more than VA4. [fod]
- **The surcharge percentage and the per-quarter credit rates are set each year** by the government , do not assume last year's figures. [fod]
- **Start-up exemption:** small companies are generally **exempt from the surcharge for their first three financial years**. [fod]

> Confirm the current surcharge rate, the exact due dates, and the start-up exemption with [FOD Financiën](https://financien.belgium.be) before planning payments.

## Why it matters

For a profitable one-person BV past its first three years, planning advance payments is a concrete, recurring agent task: estimate the year's [[corporate-tax-basics|corporate tax]], schedule the instalments to avoid the surcharge, and reconcile against the assessment.

## See also

[[corporate-tax-basics]] · [[company-size-criteria]]

Source: distilled from the standard mechanism; verify all figures against FOD Financiën.
