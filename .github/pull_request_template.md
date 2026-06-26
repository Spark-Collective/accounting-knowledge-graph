## What this PR does

<!-- one or two lines -->

## Type

- [ ] New concept page
- [ ] Update / correct an existing page
- [ ] New CBN advies (reference)
- [ ] Tooling / docs

## Checklist (see [CONTRIBUTING.md](../CONTRIBUTING.md))

- [ ] One concept per file, written in my own words (no pasted text from other sources)
- [ ] Facts cited to a **primary source** (FOD Financiën / CBN-CNC / NBB / RSVZ / WVV / Royal Decree)
- [ ] Changeable facts (rates, thresholds, deadlines) marked `verify_live: true` with a `review_after:` date
- [ ] Honest `confidence:` (`low`/`medium` for pending or single-source rules)
- [ ] At least 2 `[[wikilinks]]`; new tags added to `taxonomy.md` first; new `relations:` predicates added to `AGENTS.md` first
- [ ] Added the page to `index.md` and a line to `log.md`
- [ ] `python3 tools/graph.py --lint` and `python3 tools/graph.py --validate` pass locally

## Source(s) used

<!-- which authority / article, with a link -->
