---
type: rule
title: Personal income tax computation (director)
description: The order of operations that turns a director's remuneration into the amount on the aanslagbiljet.
tags: [personal-tax, payroll-director, bv, belgium, verify-live]
relations:
  requires: [director-remuneration, social-contributions-self-employed]
  affects: [salary-vs-dividend]
  unlocks: [personal-tax-return-filing]
sources: [https://financien.belgium.be]
confidence: high
created: 2026-08-02
updated: 2026-08-02
verify_live: true
review_after: 2027-01-31
aliases: ["personenbelasting", "aanslagbiljet", "berekening personenbelasting", "gemiddelde aanslagvoet"]
---

# Personal income tax computation (director)

How a director's remuneration becomes the amount on the assessment. The **order** below
matters as much as the rates: several steps are commonly assumed to work differently
than they do, and each of those assumptions produces a wrong number.

Confidence is `high` because this chain was verified end to end against a real
Belgian assessment: every intermediate the assessment prints reproduces to the cent.
The **rates** remain `verify_live` (they change yearly); the **structure** does not.

## The chain

1. **Bezoldigingen** (code 1400) = gross remuneration **+ benefits in kind**, net of any
   amount the director repaid to the company for those benefits.
2. **− Persoonlijke sociale bijdragen** (code 1405). Deductible professional expense.
3. **− Beroepskosten**: either the lump sum or substantiated actual expenses.
   The director lump sum is a **percentage of income AFTER the social contributions**
   (not of gross), and it is capped.
4. = **Gezamenlijk belastbaar inkomen**.
5. **Basisbelasting**: the progressive brackets applied to that amount.
6. **− Belastingvermindering op de belastingvrije som**.
7. = **Om te slane belasting**.
8. **+ Afzonderlijk belaste inkomsten** at their own rate (e.g. deeleconomie).
9. = **Totale hoofdsom** ("Belasting Staat").
10. **Federal**: hoofdsom × (100 − autonomiefactor)%.
11. **Regional**: federal × opcentiemen% (the region's surcharge on the *federal* tax).
12. **Municipal**: **hoofdsom** × gemeentebelasting%.
13. **− Terugbetaalbare bestanddelen**: bedrijfsvoorheffing, roerende voorheffing,
    voorafbetalingen, tax credits.
14. **Saldo** = (federal − credits) + regional + municipal.

## Four things that are easy to get wrong

> **The tax-free sum is a CREDIT, not a deduction.** It does not reduce taxable income;
> it produces a reduction computed at its own rate. Subtracting it from income instead
> overstates the relief for anyone above the first bracket.

> **The municipal surcharge is computed on the TOTAL principal, not on the reduced
> federal tax.** Applying it to the federal figure understates it by roughly a quarter.

> **The lump-sum expense base excludes the social contributions.** It is a percentage
> of income after step 2, not of gross remuneration.

> **The regional surcharge stacks on the already-reduced federal tax**, not on the
> principal. Steps 10 and 11 are sequential, not parallel.

## Gemiddelde aanslagvoet

The average rate the assessment prints divides the **total principal** by **total net
income including separately-taxed income** — not by the jointly-taxed base — and is
shown to one decimal.

## Why it matters

This is the second half of [[director-remuneration|salary vs dividend]]: the corporate
side is only half the optimization, and a director cannot see the real cost of a salary
euro without this chain. It is also the calculation a freelancer leaves an accounting
office to get, so an agent that runs it must be able to show every step.

## See also

[[director-remuneration]] · [[social-contributions-self-employed]] ·
[[withholding-on-director-pay]] · [[benefits-in-kind-vaa]]

> Verify the brackets, tax-free sum, lump-sum percentage and cap, autonomiefactor,
> regional opcentiemen and the municipal rate against
> [FOD Financiën](https://financien.belgium.be) for the income year before filing.
> The best available check is reproducing a prior assessment for the same taxpayer.
