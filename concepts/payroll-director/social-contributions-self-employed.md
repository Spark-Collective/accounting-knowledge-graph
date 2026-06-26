---
type: rule
title: Social contributions for the self-employed / director
description: How self-employed social security works (RSVZ/INASTI); rates to verify live.
tags: [payroll-director, eenmanszaak, bv, belgium, verify-live]
relations:
  affects: [director-remuneration]
sources: [https://www.rsvz-inasti.fgov.be/, https://www.nisse.be/en]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Social contributions for the self-employed / director

A self-employed person and a **company director** (usually self-employed status) pay social contributions to a **social insurance fund** affiliated with **RSVZ/INASTI**. These directly affect net income and the tax base.

## How it works (verify_live)

- **Base:** net taxable professional income. Contributions are **provisional** (computed on income from ~3 years prior) and later **regularised** to the final year's income. [grok/rsvz]
- **Rate:** roughly **~20.5%** on the lower income bracket, with a lower rate above a ceiling, plus **minimum** contributions and an income **cap**. [grok/rsvz]
- **Main vs secondary activity** (hoofdberoep / bijberoep) changes the minima and rights.
- **Director of a BV:** typically self-employed; the choice of **salary vs management fee** affects both the social-contribution base and the corporate-tax picture (see [[director-remuneration]], planned).

> Rates, minima, and caps change yearly. **Confirm current figures with [RSVZ/INASTI](https://www.rsvz-inasti.fgov.be/)** before computing.

## Why it matters

Social contributions are deductible and materially change the director's net , the agent must account for them when modelling salary vs dividend, and when reconciling the director's current account.

## See also

[[eenmanszaak-vs-vennootschap]] · [[company-size-criteria]]

Source: Grok research synthesis; verify against RSVZ/INASTI.
