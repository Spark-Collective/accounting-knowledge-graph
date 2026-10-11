---
type: workflow
title: Quarter close and VAT return, start to filing
description: The quarterly SOP distilled from closing Q3 2026 in the native ledger. Independent check first, correction batch second, settlement and return last.
tags: [workflows, bookkeeping, vat, intervat, belgium]
relations:
  requires: [month-end-close, vat-period-prep, closing-entries]
  affects: [periodic-vat-return-intervat]
sources: [https://www.cbn-cnc.be/nl/adviezen/erkenning-van-opbrengsten-en-kosten, https://financien.belgium.be/nl/ondernemingen/btw/btw-plicht/gedeeltelijke-btw-aftrek/gemengde-belastingplichtigen]
confidence: high
created: 2026-10-11
updated: 2026-10-11
verify_live: false
review_after: 2027-04-11
aliases: ["kwartaalafsluiting", "kwartaal afsluiten", "quarter-end close"]
---

# Workflow: quarter close and VAT return

Three months of [[month-end-close]] never add up to a closed quarter. The Q3 2026 close found eleven items the monthly routine had missed, two of them with filing impact. This page is the order of work that caught them. It runs on top of [[vat-period-prep]], which stays the rule for the return itself.

## 1. Independent check before anyone books

Run the ledger's quarter check (`packages/ledger/scripts/quarter-check.ts` in the Midday fork) against the quarter and the previous quarter. Read it as an auditor, not as the bookkeeper who made the entries. The things that bit in Q3 2026, in the order they were found:

- **Costs per month.** A month far below the others is a missing booking, not a quiet month (September showed 1.570 against 8.179 and 5.837: payroll, insurance release and three accruals were missing).
- **Prepaid costs (490000).** Every debit needs a release schedule. A 2025 insurance premium sat untouched for nine months because no release was ever planned. Register annual services as `deferral` amortizations the day they are booked; the engine then releases them monthly.
- **Payroll.** One payroll entry per month (gross, withholding 453000, net 455000, benefits in kind against 749). The tell when one is missing: 453000 in debit, 455000 at zero instead of the usual one month payable.
- **Same supplier, same treatment.** Compare account and VAT treatment per counterparty with the previous quarter. Car lease went from 610300 at 50% VAT to finance costs at 100%; Tesla connectivity moved across three accounts in three months.
- **Non-EU and EU services.** Every foreign B2B service carries reverse charge, per transaction, with the right code (`P21-ICS` EU, `P21-NON-EU` non-EU). A supplier that still charged 21% under the OSS consumer regime (TradingView, 1Password) gets the reverse charge anyway and its VAT is cost, not deduction, until a corrected invoice arrives.
- **Assets.** Every 2xx debit from the bank needs an `amortizations` row, or it never depreciates (a desk bought in September had none).
- **Bank.** Feed total versus ledger per account must be zero, and the app balance versus feed total is a separate question (a constant gap is an opening or feed issue, not a booking).
- **Inbox evidence.** Before asking for a document, search the inbox and vault; the September payslip and three invoices were already there.

## 2. One approval, one batch

Put every proposed entry in one working paper with the money effect per item and the decisions the operator must take (deduction percentages, business use, cut-off splits). The operator answers once. Then one idempotent script posts the batch: it reverses whatever is currently posted for a transaction and re-books it, it never trusts the entry number from the plan (the hourly auto-post can book a row between the review and the run), and it verifies each entry's lines before moving to the next. Dry run first, live second, record the entry numbers.

## 3. Quarter-end entries, in order

1. Reverse-charge corrections and cut-off releases (journal 800, last day of the quarter).
2. Accruals for invoices dated after quarter end for services inside it (444000), to reverse on day one of the next quarter.
3. Depreciation catch-up when a base changed.
4. Regularisations in the company's favour on 411000 with the grid-62 code; corrections of earlier settlements against 451900.
5. Recompute the grids. Grid 71 must equal 451000 less 411000 at quarter end.
6. **Btw-verrekening** in journal 890: Dr 451000 (its balance), Cr 411000 (its balance), Cr 451900 (grid 71). After it, 411000 and 451000 are zero and 451900 carries the amount to pay.

## 4. The return

Prepare per [[vat-period-prep]]. Generate the XML from the ledger, with the company itself as declarant when it files itself. Submission is a human click (in the app's Filings page when the FPS production access works, otherwise upload on Intervat). Record the receipt reference on the filing row, pay with the structured communication, lock the three months.

## Guardrails

- Nothing is posted without the operator's written answers to the decision list.
- A correction script is read-only until its dry run prints exactly the plan the operator approved.
- No quarter closes with an unbooked bank row, a 490000 line without a schedule, or a month without payroll.

## See also

[[month-end-close]] · [[vat-period-prep]] · [[closing-entries]] · [[intracommunity-and-medecontractant]] · [[chart-of-accounts-mar]]
