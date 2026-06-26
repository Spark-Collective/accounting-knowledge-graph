---
type: rule
title: Withholding tax on director pay (bedrijfsvoorheffing)
description: The company withholds advance income tax on the director's salary and remits it to the authority.
tags: [payroll-director, bv, belgium, verify-live]
relations:
  requires: [director-remuneration]
sources: [https://help.astro.tax/nl/articles/10053108-hoe-werkt-de-bedrijfsvoorheffing-voor-bestuurders-van-een-vennootschap, https://financien.belgium.be]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Withholding tax on director pay (bedrijfsvoorheffing)

When a BV pays its director a salary, it must **withhold bedrijfsvoorheffing** on the monthly gross and **remit it to the tax authority** , an advance on the director's personal income tax, so part of the bill is already paid by the annual return.

## The rule (verify_live)

- Withheld on the **monthly gross** director remuneration and any taxable benefits. [astro]
- Computed via the **government's official formula/scales**, based on income and benefits. [astro]
- Typically run through a **sociaal secretariaat** (social secretariat), which calculates and files it. [astro]

> The scales and formula are updated (at least yearly). **Use the current official calculation** ([FOD Financiën](https://financien.belgium.be)); do not reuse last year's figures.

## Why it matters

It is the payroll-side counterpart of the company's own [[advance-payments|corporate-tax prepayment]]: getting the withholding right avoids a surprise at the director's personal assessment. It sits on top of the gross set in [[director-remuneration]] and the [[social-contributions-self-employed|social contributions]].

## See also

[[director-remuneration]] · [[social-contributions-self-employed]] · [[benefits-in-kind-vaa]]

Source: Astro Tax help (collaboration source, distilled), FOD Financiën.
