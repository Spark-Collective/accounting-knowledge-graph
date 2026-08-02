---
type: rule
title: Filing the personal income tax return (Tax-on-web)
description: How a director's return is filed, what can be automated, and what cannot.
tags: [personal-tax, workflows, belgium, verify-live]
relations:
  requires: [personal-income-tax-computation]
  affects: [year-end-close]
sources: [https://financien.belgium.be, https://www.myminfin.be]
confidence: medium
created: 2026-08-02
updated: 2026-08-02
verify_live: true
review_after: 2027-01-31
aliases: ["aangifte personenbelasting", "Tax-on-web", "belastingaangifte indienen"]
---

# Filing the personal income tax return (Tax-on-web)

## The channel reality

Belgium exposes real APIs for **VAT** (Intervat) and **document retrieval** (MyMinfin
FineAPI), but **not** for the personal income tax return. Tax-on-web is a human web
application; mandate holders use Tax-on-web mandataris.

So a system can prepare everything and verify everything, but **a human submits**.
That is not a limitation to hide: filing your own return is entirely ordinary in
Belgium, and the useful promise is that by the time the form is open, every number is
computed, sourced and ready to enter.

## What can be automated

| Step | Automatable |
|---|---|
| Collect remuneration, benefits, withholding | Yes, from the company ledger |
| Retrieve the fiche 281.20 and prior assessments | Yes, MyMinfin FineAPI (`documents-read-api`) |
| Capture personal items (VAPZ, advance payments, deductions) | Guided entry |
| Cross-check ledger figures against the official fiche | Yes |
| Compute the return | Yes, see [[personal-income-tax-computation]] |
| **Submit** | **No API. Human, in Tax-on-web** |
| Collect the assessment afterwards | Yes, MyMinfin FineAPI |

## Deadlines (verify_live)

Announced yearly and different per channel (paper vs Tax-on-web vs mandate holder).
Roughly end June for paper and mid-July online. **Confirm the current year's dates**;
they move.

## Validate before you trust

Any computation engine should first **reproduce an assessment the authority already
issued** for the same taxpayer, matching every intermediate the assessment prints, not
just the final amount. Prior assessments are retrievable through the MyMinfin API, so
this check can run against real history at any time of year.

An engine that has not reproduced a real assessment should present its output as an
estimate, and say so.

## See also

[[personal-income-tax-computation]] · [[director-remuneration]] ·
[[periodic-vat-return-intervat]] (the API-backed counterpart)
