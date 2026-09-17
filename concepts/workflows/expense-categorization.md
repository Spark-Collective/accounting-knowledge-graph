---
type: workflow
title: Expense categorization
description: Route each cost to the right account, deductibility rule, and VAT treatment.
tags: [workflows, deductible-costs, vat, belgium]
relations:
  part_of: [booking-a-purchase-invoice]
  requires: [vat-deduction-conditions]
sources: [https://finances.belgium.be/fr/node/1581, https://www.belgium.be/fr/impots/tva/deductions, https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/persons-liable-vat_en]
confidence: high
created: 2026-06-26
updated: 2026-09-17
verify_live: false
review_after: 2027-03-17
aliases: ["kosten categoriseren", "kostenrubriek", "kost boeken", "welke rekening voor kost"]
---

# Workflow: expense categorization

The judgment step inside [[booking-a-purchase-invoice]]. Keep three decisions separate: the accounting category, income-tax treatment and VAT treatment. This page defines a working method; it contains no default deduction percentages or tax rates.

## Steps

1. **Read the evidence.** Identify the invoicing entity, purchased items, business purpose and period. Use [[supplier-pattern-library]] as a checklist. A brand name or bank description alone is insufficient. Entries must be supported by documents. [Source: SPF Finances, accounting and invoicing](https://finances.belgium.be/fr/node/1581).
2. **Propose the accounting category.** Use the company's actual chart and valuation policy, consulting [[chart-of-accounts-mar]] and [[depreciation]]. Check whether the item is an expense, asset, prepayment or settlement before selecting an account. Never force every invoice into an expense account.
3. **Review income-tax treatment separately.** Route to the relevant rule page, such as [[restaurant-and-meals]], [[car-and-mobility]], [[ict-equipment]] or [[sponsoring]]. Check the current authoritative rule and its conditions before assigning a deduction percentage. Record missing evidence rather than inferring a percentage from the supplier.
4. **Review VAT separately.** Establish taxable activity, professional use and the supporting invoice, then consult [[vat-deduction-conditions]] and any applicable restrictions. Private and professional use must be distinguished. [Source: Belgium.be, input VAT deduction](https://www.belgium.be/fr/impots/tva/deductions).
5. **Check cross-border treatment where relevant.** Read the legal supplier and customer details and identify the service's place of supply before proposing reverse charge. [Source: European Commission, persons liable for VAT](https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/persons-liable-vat_en). Follow [[intracommunity-and-medecontractant]] and verify current conditions.
6. **Record uncertainty and preserve decisions.** Identify possible private use for review under [[benefits-in-kind-vaa]]. Follow [[classification-protocol]]: cite evidence, disclose assumptions and name the fact still needed. Do not overwrite an existing human decision.

## Completion gate

A booking proposal records the account, VAT treatment, income-tax treatment and their evidence, or explicitly marks each unresolved field. A knowledge-reference review does not approve the proposal. Rates and deductions require current sources; posting and filing require the applicable authorization.

## See also

[[booking-a-purchase-invoice]] · [[vat-deduction-conditions]] · [[supplier-pattern-library]] · [[classification-protocol]]
