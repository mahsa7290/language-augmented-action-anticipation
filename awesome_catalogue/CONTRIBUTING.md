# Contributing

Thank you for helping maintain the catalogue.

## Required fields

1. Canonical paper title and URL.
2. Venue or preprint identifier and year.
3. Task regime and benchmark/dataset.
4. Primary C1--C4 role and any secondary roles.
5. Code/checkpoint URL when publicly available.
6. Publication maturity and reproduction status.
7. Source table/figure/section for quantitative claims.

## Coding rule

Use C1 for context representation, C2 for goal/intention conditioning, C3 for future objective or decoding, and C4 only for feasibility beyond ordinary label prediction. Multi-component methods should retain secondary labels rather than forcing all roles into the primary count.

## Pull-request checklist

- [ ] Paper URL resolves to the canonical source.
- [ ] Code link is official or clearly labelled third-party.
- [ ] Dataset and protocol version are stated.
- [ ] No cross-paper number is presented as directly comparable without protocol evidence.
- [ ] New claim has a row-level source locator.
