# (B) Read-only gate query over recorded results: RESULT EMPTY (SNOW; Lars-approved; Astra's strict criteria, v2)

**Scope.**
- READ-ONLY over already-recorded results (`snow_results.jsonl` plus the recorded evidence files). No native runs, no
  solver, no new tables, no reduced-clause solve.
- Script `snow_b8_gate_query.py` v2 (sha256 `3143d6de…`); output `snow_b8_gate_query.json` (`fb931871…`), which lists every
  join key, every row, contradictions and anomalies.
- v1 (script `5d567177…` / json `11f55210…`) is superseded. Its numbers agree, but it used the oracle status instead of an
  explicit multiset comparison, had no reference-sha / effective-flag join, and its group rule could resolve conflicts
  toward a pass.

**Join key.** Exact table + candidate binary sha + reference binary sha + effective `HVM_*` flags (from the recorded
candidate environment; `HVM_MOVR` is checked equal to the table) + exact gate program hashes
(`suite.t0..t4.published_main`, `bounty.published`, current pct / C1 sha256).

**Per-gate classification.**
| class | condition |
|---|---|
| PASS | exact program, candidate AND reference complete, full multisets equal; for bounty also < 50,000 interactions |
| FAIL_OUTPUT | exact program, both complete, multisets differ |
| FAIL_OBJECTIVE | bounty only: exact program, both complete, multisets equal, ≥ 50,000 interactions |
| UNKNOWN / UNRECORDED | missing, capped, incomplete, inconclusive, or a different program. NOT a failure |

- A key qualifies iff all six gates are PASS, with no FAIL record.
- Mixed PASS and FAIL records under one key are flagged CONTRADICTORY, never resolved toward a pass.

## Result: **EMPTY**. 0 qualifying join keys
- 349 recorded rows. **41 join keys** have any gate record. All 41 are completely classified on all six gates.
- Pattern in **all 41**: `suite.t0..t4.published_main` **PASS** and `bounty.published` **FAIL_OBJECTIVE**.
  - The bounty runs have equal full multisets on the exact program, at 97,890, 97,896 or 122,340 interactions.
  - The keys cover the default-configuration sweep (`f9111a87` / `f9c251a4`, no flags; single-cell variants of the all-K
    table) and 3 backend-8 keys (`041404f1`, `HVM_MOVR_INHERIT=1`).
- **0 CONTRADICTORY** keys and **0 anomalies** (recorded `HVM_MOVR` = table everywhere).
- **Coverage UNKNOWN, not failure:** 8 rows selected all six gates but stopped at an earlier case, so their gates are
  UNRECORDED:
  - `labels.percent.dynamic_auto` mismatch: 3 rows;
  - `falsifier.issue18.minimal` mismatch: 2;
  - `suite.t0.n1.*` mismatch: 2;
  - `suite.t0.n4.mixed` inconclusive: 1.

  All other rows recorded no gate.

## Meaning
- **No qualifying complete recorded evidence.** No join key has complete PASS records for all six exact gates including
  the <50k bounty record. In every completely gated key, the binding result is the objective, not output agreement.
- **EMPTY excludes NOTHING that is unrecorded or only partially recorded:** not the 8 early-stopped tables, not unrecorded
  tables, configurations or action languages, and not other rules.
- Not an impossibility result; not E evidence.
- Per Lars's decision, (A) is NOT started. Stopped pending Lars.
