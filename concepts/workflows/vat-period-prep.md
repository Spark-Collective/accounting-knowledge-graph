---
type: workflow
title: Prepare a periodic VAT return for review
description: The SOP the agent runs to compile a VAT return; prepare, never file.
tags: [workflows, vat, intervat, belgium]
relations:
  requires: [vat-rates-and-regimes, vat-return-grilles]
  affects: [periodic-vat-return-intervat]
sources: [https://financien.belgium.be/nl/E-services/Intervat]
confidence: high
created: 2026-06-26
updated: 2026-10-12
verify_live: false
review_after: 2027-06-26
aliases: ["btw aangifte voorbereiden", "periodieke btw voorbereiding", "kwartaalaangifte"]
---

# Workflow: prepare a periodic VAT return for review

The agent **prepares** the [[periodic-vat-return-intervat|periodic VAT return]] and presents it for approval. It files only on the operator's explicit, written approval for that exact period (since 2026-10-12: through the ledger's `filings_submit_vat`, which records who approved and refuses without a confirm flag). No approval, no submission.

## Steps

1. **Scope the period.** Determine the period (quarter/month) and its filing deadline , **verify the current deadline live** ([[periodic-vat-return-intervat]] is `verify_live`).
2. **Reconcile first.** Ensure all sales and purchase invoices for the period are booked and the bank is reconciled (the [[chart-of-accounts-mar|VAT accounts]] 411/451 must be complete). Flag anything unbooked.
3. **Compile the figures.** Sum output VAT (451) and input VAT (411) by rate; compute the net to pay or reclaim. Map to the Intervat return grid boxes.
4. **Sanity checks.** Compare to the prior period; flag big swings, missing-VAT-number invoices, reverse-charge (medecontractant) entries, and intra-community transactions (these also feed the EC sales list).
5. **Verify rates/rules** against [[vat-rates-and-regimes]] , and re-confirm any changeable figure with [FOD Financiën](https://financien.belgium.be).
6. **Present for approval.** Produce a short summary (period, boxes, net, flags) for the operator. Generate the Intervat XML only after approval.
7. **Record.** Log what was prepared; route the artifact to its store. Any recurring issue -> update the relevant KB page.

## Before a quarterly return

Run the [[quarter-close]] workflow first: the independent quarter check, the single correction batch, the quarter-end btw-verrekening. The return is only as good as the quarter behind it; Q3 2026 moved from 5.101,05 to 4.974,80 between the first grid computation and the filed figure.

## Guardrails

- **Never file on your own initiative.** Outbound to the tax authority needs the operator's explicit written approval for that period; the submission tool records it. Show the full return (every box, the declarant, the XML) before asking.
- If figures don't reconcile, **stop and escalate** , do not file an unbalanced return.

## See also

[[periodic-vat-return-intervat]] · [[vat-rates-and-regimes]] · [[chart-of-accounts-mar]] · [[quarter-close]]
