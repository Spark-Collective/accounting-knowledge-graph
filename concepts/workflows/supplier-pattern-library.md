---
type: reference
title: Supplier pattern library (transaction classification)
description: Supplier and document clues for routing a purchase to the right review workflow, without automatic tax conclusions.
tags: [workflows, deductible-costs, vat, belgium]
relations:
  part_of: [booking-a-purchase-invoice]
  affects: [expense-categorization]
sources: [https://finances.belgium.be/fr/node/1581, https://www.belgium.be/fr/impots/tva/deductions, https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/persons-liable-vat_en]
confidence: high
created: 2026-06-26
updated: 2026-09-17
verify_live: false
review_after: 2027-03-17
aliases: ["leveranciers", "leverancierspatronen", "terugkerende leveranciers"]
---

# Supplier pattern library (transaction classification)

This is a routing aid for [[expense-categorization]] and [[booking-a-purchase-invoice]]. A supplier name suggests what evidence to inspect; it does not establish an account, business purpose, VAT recovery or income-tax deduction. The table below is an operational checklist, not a set of tax rulings. Supporting documents must substantiate the entries in the VAT books. [Source: SPF Finances, accounting and invoicing](https://finances.belgium.be/fr/node/1581).

## Document clues to inspect

| Document or supplier clue | Check before proposing a category |
|---|---|
| Fuel or charging | Separate the actual purchase from shop goods or equipment; identify the vehicle, business use and supporting document. Route to [[car-and-mobility]] or [[ev-charging-reimbursement]]. |
| Telecom | Separate subscriptions, equipment and private use. Consult [[benefits-in-kind-vaa]] when relevant. |
| Restaurant or food delivery | Establish the nature and purpose of the meal; delivery-platform branding alone does not establish restaurant treatment. Consult [[restaurant-and-meals]]. |
| Software or cloud service | Identify the invoicing legal entity, its establishment, customer VAT status and service supplied. Check the current cross-border rule in [[intracommunity-and-medecontractant]]. |
| Office supplies or ICT | Read the purchased items; determine expense, inventory or fixed-asset treatment using the company's chart and valuation policy. Consult [[ict-equipment]] and [[depreciation]]. |
| Rail or parking | Inspect the actual travel evidence and business purpose; establish whether it supports the proposed VAT treatment. |
| Professional adviser | Identify the billed service and period, and inspect any separately charged disbursements. |
| Insurance | Distinguish the premium, taxes and any separately billed services from the document. |
| Bank | Distinguish service fees, interest, loan principal and transfers; do not classify every bank debit as an expense. |
| Payroll service provider | Separate provider fees from wages, social contributions and tax remittances. |

## Tax decisions remain separate

VAT recovery depends on the activity and professional use; a supplier match cannot establish it. Mixed private and professional use requires evidence of the professional share. This page deliberately stores no default recovery percentage. [Source: Belgium.be, input VAT deduction](https://www.belgium.be/fr/impots/tva/deductions).

For cross-border services, inspect the supplier's establishment, customer status and place of supply. The general customer-liability rule concerns a supplier not established in the customer's country; it is not restricted to EU suppliers. Check exceptions before applying it. [Source: European Commission, persons liable for VAT, Article 196](https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/persons-liable-vat_en).

## Review boundary

High confidence applies to this evidence-first routing method only. It does not certify linked tax pages or any invoice's treatment. Fetch authoritative current rules when applying a rate, deduction, exemption or reverse charge. Preserve existing human decisions; use [[classification-protocol]] for missing evidence and disclose the specific unresolved question. Do not post or file merely because this reference has been reviewed.

## See also

[[booking-a-purchase-invoice]] · [[expense-categorization]] · [[classification-protocol]]
