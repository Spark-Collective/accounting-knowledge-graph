---
type: rule
title: Director loan and current account (rekening-courant)
description: Borrowing from your company via the current account; debit balances carry a yearly-set interest.
tags: [corporate-tax, payroll-director, bv, belgium, verify-live]
sources: [https://help.astro.tax/nl/articles/10053338-geld-lenen-van-je-vennootschap-hoe-werkt-dat-precies, https://financien.belgium.be]
confidence: medium
created: 2026-06-26
updated: 2026-09-03
verify_live: true
review_after: 2027-01-31
aliases: ["rekening-courant", "RC zaakvoerder", "lening van vennootschap", "debetstand"]
---

# Director loan and current account (rekening-courant)

A director can take money out of the company as a loan, either through the **current account (rekening-courant, R/C)** or a **fixed-term loan**. The R/C tracks the running balance of what the director and the company owe each other.

## The rule (verify_live)

- **Positive R/C:** the company owes the director (the director put money in). [astro]
- **Negative / debit R/C:** the director owes the company , this is treated as a loan and **carries interest**. [astro]
- **The interest rate on a debit R/C is set yearly** by the tax authority. Recent reference rates: income year 2022 ~**7.14%**, income year 2023 ~**5.43%** , high and volatile. [astro]
- If the company charges **too little** interest, the shortfall becomes a taxable **benefit in kind** ([[benefits-in-kind-vaa]]) for the director.

> The debit-R/C interest rate changes every year. **Confirm the current rate with [FOD Financiën](https://financien.belgium.be)** before booking interest.

## Credit R/C: the director lends TO the company (verify_live)

The mirror case matters for a one-person BV that bridges cash with the director's
own money. The company may pay interest on that loan, but two ceilings apply
before the excess is **requalified as a dividend** (non-deductible for the company):

- **Rate ceiling (art. 55 WIB92 / art. 18, 4° WIB92):** the interest may not exceed
  the market rate, defined since 2020 as the **MFI rate for loans up to EUR 1M with a
  variable rate and initial fixation up to one year, of NOVEMBER of the previous
  calendar year, plus 2.5 percentage points**. Calendar 2026: MFI Nov 2025 = 3.50%,
  so **6.00%** (2025: 7.08%, 2024: 8.02%). Changes every January. [practicali] [bakertilly]
- **Principal ceiling (art. 18, 4° WIB92):** interest is requalified on the part of the
  loan that exceeds **taxed reserves at the start of the taxable period + paid-up
  capital at the end of it**.
- **Withholding:** the company withholds **30% roerende voorheffing** on the interest it
  pays the director, and the director declares it as movable income.

Midday's Owner surface shows the open loan, the yearly cap (tax parameter
`rc_creditor_max_interest_rate`, seeded per year with its source), the day-weighted
interest allowed so far, and the principal ceiling from the ledger's class-1 balances.

> Re-verify the MFI figure each January at the NBB (MIR statistics) or FOD Financiën
> before invoicing interest.

## Why it matters

A debit R/C is a common, easily-overlooked exposure for a one-person BV: drawing cash without booking the (now high) interest creates a VAA and a tax cost. The agent should track the R/C balance and apply the current rate , part of [[director-remuneration|payout planning]].

## See also

[[benefits-in-kind-vaa]] · [[director-remuneration]] · [[corporate-tax-basics]]

Source: Astro Tax help (collaboration source, distilled), FOD Financiën; credit-R/C rate: [Practicali, calendar 2026](https://www.practicali.be/blog/marktrente-voor-creditinteresten-op-uw-rekening-courant-voor-kalenderjaar-2026), [Baker Tilly](https://bakertilly.be/nl/news/maximale-rente-credit-r-c-voor-boekjaar-2025-bekend/).
