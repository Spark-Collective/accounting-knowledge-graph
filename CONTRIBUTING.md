# Contributing to spark-accounting-kb

Thanks for helping build an open, agent-readable knowledge base of Belgian accounting **practice**. This guide is the human on-ramp; the full machine protocol is in [`AGENTS.md`](AGENTS.md) (read it once , agent-assisted contributions are welcome, point your agent at it).

## What this project is (and isn't)

- It captures **distilled practice** , how to book, decide, and file , for **single-person BVs (management companies) and freelancers** in Belgium.
- It is **not** the law, and **not** a place to store precise live numbers. Rates, thresholds, and deadlines change, so we mark them `verify_live: true` and fetch the current value from the authority at use time. See the "core rule" in [`AGENTS.md`](AGENTS.md).
- It is **not** a copy of anyone's content. Write in your own words and cite the primary source.

## The five rules

1. **One concept per file** (20-40 lines). Split when it grows.
2. **Distil, never paste.** Re-author in your own words; cite the source in `sources:` and mark synthesized paragraphs `[source]`. Do not copy text from other projects (e.g. astro.tax, OpenAccountants) , facts aren't copyrightable, their phrasing is.
3. **Primary-source the facts.** Cite the authority (FOD Financiën, CBN/CNC, NBB, RSVZ, the WVV / Royal Decrees) , see [`sources.md`](sources.md).
4. **Mark changeable facts `verify_live: true`** with a `review_after:` date. Be honest with `confidence:` (`low`/`medium` for pending or single-source rules).
5. **Link.** At least 2 `[[wikilinks]]` per page; for relational concepts add typed [`relations:`](AGENTS.md) edges.

## How to add or change a page

1. Fork and branch.
2. Add/edit the markdown file under `concepts/<topic>/` (or `references/cbn-adviezen/` for a distilled advies, named `<slug>-advies.md`).
3. Use the frontmatter template in [`AGENTS.md`](AGENTS.md). New tag? Add it to [`taxonomy.md`](taxonomy.md) first. New `relations:` predicate? Add it to the vocabulary in `AGENTS.md` first.
4. Add the page to [`index.md`](index.md) and append a line to [`log.md`](log.md).
5. **Validate locally** (no dependencies, just Python 3):
   ```bash
   python3 tools/graph.py --lint       # required frontmatter + >=2 wikilinks on every page
   python3 tools/graph.py --validate   # typed edges resolve + predicates in vocab
   ```
   CI runs both on every PR; they must pass.
6. Open a small, focused PR. Describe the source you used and flag anything you're unsure about.

## What we will not merge

- Verbatim content copied from another source.
- A rate/threshold asserted as final without `verify_live` + a citation.
- The raw legal codes dumped wholesale (wrong granularity; goes stale; see the guardrail in `AGENTS.md`).

## Disclaimer

This is a general reference for preparing working papers, **not** tax, legal, or accounting advice. Everything produced from it must be reviewed and signed off by a qualified professional (comptable / accountant / belastingadviseur) before filing or acting on it.

## License

The project is licensed under the [Apache License 2.0](LICENSE). By contributing, you agree that your contributions are licensed under the same Apache-2.0 terms (inbound = outbound).
