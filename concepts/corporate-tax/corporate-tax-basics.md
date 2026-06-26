---
type: rule
title: Corporate tax basics (vennootschapsbelasting)
description: Standard 25% rate, the 20% reduced rate on the first EUR 100k, and how the base is built.
tags: [corporate-tax, bv, belgium, verify-live]
relations:
  requires: [company-size-criteria]
  affects: [advance-payments]
sources: [https://financien.belgium.be, https://nl.wikipedia.org/wiki/Belgische_vennootschapsbelasting]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Corporate tax basics (vennootschapsbelasting)

A BV pays corporate tax on its taxable profit. The taxable base starts from the **accounting profit** and is adjusted (the *fiscale bewerkingen*): increase in reserves + **disallowed expenses** (*verworpen uitgaven*, e.g. the non-deductible fraction of [[restaurant-and-meals|meals]] or [[car-and-mobility|car costs]]) + distributed dividends, then minus the deductions.

## Rates (verify_live)

- **Standard rate: 25%.** [search]
- **Reduced rate: 20% on the first EUR 100,000** of taxable profit, **for a small company** ([[company-size-criteria]]) meeting conditions. [search]

### Conditions for the 20% rate (verify_live)

- The company is a **small company** (size criteria).
- **At least one director draws a minimum remuneration of EUR 45,000** (or, if profit is lower, a remuneration at least equal to the profit). The planned rise to EUR 50,000 is **not yet in force for 2026** , confirm before relying on it. [search]
- Not a **financial company**, and the **majority of shares are held by natural persons** (not a holding-heavy structure). [search]

> Rates, the EUR 100,000 band, and the EUR 45,000 remuneration threshold change. **Confirm the current figures with [FOD Financiën](https://financien.belgium.be)** before computing a real assessment.

## Why it matters

The EUR 45,000 director-remuneration condition ties corporate tax directly to [[social-contributions-self-employed|director pay]] , a core optimization lever for a one-person BV (enough salary to keep the 20% rate, the rest via dividends). Modelling this is a primary job of the SparkOS accounting agent.

## See also

[[company-size-criteria]] · [[social-contributions-self-employed]] · [[advance-payments]]

Source: linkup search synthesis; verify against FOD Financiën.
