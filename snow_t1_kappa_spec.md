# T1 C1-vs-kappa experiment — CANCELLED by Lars

**Current status, superseding every preparation/build/run gate below.**
- Lars dropped T1 after VMOV withdrawal. No differential, calibration run,
  candidate execution, further build, or execution-gate review is authorized.
- Before that cancellation, the one compiler-only build authorized by Astra
  review 33AC completed. Its record is retained unchanged:
  `snow_t1_kappa/build_record.json`; binary `8e0ab73c...`, never executed.
- The runner v2 return below was not approved for execution. Its review stopped
  on receipt of the cancellation. Historical source, build and proposal
  artifacts are retained for provenance, not as outstanding work.
- The replacement deliverables are the scoped negatives report and a new
  paper-only positive-route proposal. No VMOV, solver or Words work is allowed.

The remainder records the cancelled experiment's historical design and gates.

**Purpose after Astra 5365.**
- Universal O2 is already refuted on paper (public label `&(8388608)`), and a bounded agreement could never prove O2.
- T1 therefore only:
  - (a) locates, on the fixed listed corpus, where per-activation `%` freshening changes the full collapse output or
    termination;
  - (b) counts mismatches on proved-E-invalid programs toward O2b.
- Interpretation follows Lars's condition (3): only a mismatch on an E-CERTIFIED row is evidence against O2 on the
  corpus. Agreement on uncertified rows is weak / uncertified support.
- The 5365 paper witness is NOT a corpus case and is NOT added.

## 1. Mode-6 audit: NOT usable as C1^κ

Working-tree `HVM4/src/hvm.c` (words-modified, sha `a54eb1de…`; using it would also be words-tree reuse):
- **Wrong identification.** Mode 6 acts only when `MOV_ON && term_ext(next) == EXC_LAB && !MOVR_ON` (lines 6861–6862).
  That selects copiers by the `&EXC` label. Parsed `%` bindings get an AUTO label (`% f = v` parses as `! & f = v`,
  line 283 comment), so they would not be selected.
- **Extra semantics.** `EXC6-WIRE` (6869–6873) wires the door to the value when the other door is dead. That is a
  dead-side wire, not freshening, and it removes a copier firing (the binder-SUP / multiplicity hazard).
- **Unstable refresh.** `exc_instance_label` (326–333) falls back to `return MOV_FRESH++` when its 2^22-entry table is
  full. Each door entry then gets a NEW label, so the two doors of one copier would disagree.
- **Namespace overflow.** `MOV_FRESH` starts at `0x400000` and increments without bound. After 4,194,304 allocations it
  enters the parser's auto-label range (≥ `0x800000`, upstream H:226), colliding with static labels. There is no
  exhaustion check.
- **Relabelling at door entry.** It rewrites the entering door term per entry (6875–6879), not at copier birth.
  Stability then depends on the table.
- **Non-termination.** Lars reports that the earlier runtime fresh-label rule did not terminate somewhere. I did not
  locate the cause from source; candidates are the WIRE rule and the refresh fallback.
- **Conclusion:** mode 6 is excluded. C1^κ is built as a minimal patch on the pinned upstream instead.

## 2. Construction of C1^κ (patch P_κ on the pinned upstream)

**Base:** `astra_evidence/reference_repro_6defdfc_gcc_o2/src/hvm.c`, upstream `6defdfc`, sha256 `3d2724d0…` ("H").

**Build** (same as the reference): GCC 13.3.0, `gcc -O2 -o <out> hvm.c`.

**Pre-step B0 (toolchain check):** build unpatched H and require byte equality with `astra-repr/hvm_base` (sha
`ea6cb779…`). If it differs, stop.

**Patch points.** Line numbers are H's. The patched source and diff are hashed and given to Astra before building.
- **P1 parser.**
  - Accept `%` as EXACTLY the established lexical replacement `! &`, i.e. a cloned let through the same path as
    `! & f = v` (H:2644–2650, `parse_auto_dup(body, depth+1, depth+1, BJV, 0, uses)`), with the same label-allocation
    order.
  - During that one `parse_auto_dup` call, record each book DUP location it allocates (H:2083 `loc`) in a static set
    `PCT_BOOK`.
  - `uses ≤ 1` returns before any allocation (H:2044–2046), so **single-use `%` creates no copier and nothing is
    marked**.
- **P2 copier birth.** In `wnf_alo_dup` (H:4033–4040): if `KAPPA_ON` and `book_loc ∈ PCT_BOOK`, then
  `KMAP[bind_ent] := kappa_alloc()`.
  - `bind_ent` is this activation's binding entry for this tree position. Each book DUP in an auto-dup chain is its own
    position with its own static `lab+i` (H:2082–2086), so **each activation × position gets exactly one κ**.
  - Copiers act only on WHNF values (the DP0/DP1 frame dispatch has no ALO case, H:5082ff). `%` code is therefore
    instantiated once, in its shared cell, before any enclosing copier acts on it. One birth per activation.
- **P3 door resolution.** In the ALO-DP0/DP1 resolution (H:3996–4011, `term_new(0, rtag, lab, it)`): if
  `KMAP[it]` exists, use κ instead of the book `lab`.
  - Both doors of the copier resolve to the same `it`, so they get the same κ: **stable, with no per-entry refresh**.
- **P4 inheritance (no code change).** The dup frame uses `lab = term_ext(frame)` (H:5084–5086). Derived body / field
  copiers (`term_clone_at(.., lab)`, H:3899–3902, 3932–3935) and the binder / commute SUPs it creates carry that same
  label.
  - **Descendants inherit κ, and nothing ever re-freshens:** κ is assigned only in P2.
  - Ordinary and source labels are untouched, because only `PCT_BOOK` births are relabelled.
- **P5 namespace and collisions.**
  - At the end of parsing, set `κ_lo := PARSE_FRESH_LAB` (all static auto labels lie below it) and scan the book for
    any static (named or numeric) SUP / DUP / door label ≥ `κ_lo`. If one exists: abort `KAPPA-STATIC-COLLISION`.
  - `kappa_alloc` returns `κ_next++`. If it reaches `PARSE_DYN_LAB = 0xFFFFFF` (reserved, H:228): abort
    `KAPPA-EXHAUSTED`. Capacity ≈ 8,388,607 − (static auto labels).
  - Every dynamic label installation (`wnf_dsu_num`, H:4152–4155, and the DDU-NUM counterpart) checks
    `(lab & EXT_MASK) ≥ κ_lo`. If so: abort `KAPPA-DYN-COLLISION`. This is conservative: it also covers κ's not yet
    allocated, so **globally fresh = disjoint from every static and dynamic label of the run**.
- **P6 KMAP.** An open-addressing u64→u32 table with a fixed capacity of 2^24. When full: abort `KAPPA-MAP-FULL`.
  **There is never a fallback label.**
- **P7 switch.** `KAPPA_ON := (getenv("HVM_KAPPA") equals "1")`. With it off, P2, P3 and P5 are inert and P1's marking
  has no effect.
- **Accounting.** κ assignment is not an interaction: interaction counts are unchanged in meaning. One stderr line
  `KAPPA_ALLOC=<n> KAPPA_LO=<x>` is emitted at exit, as a parsed diagnostic.
- **Abort exits** use a distinct exit code (e.g. 77) and are classified UNKNOWN.

**Verification obligations (review + control).**
- **K1:** P1 yields a book identical to parsing the C1 source (`! &` rewrite). Checked by the κ-off control.
- **K2:** every DUP birth path goes through `wnf_alo_dup`, including REF expansion and `@main`. To be checked in H
  during review: any non-ALO runtime DUP birth must be listed and patched or excluded.
- **K3:** every door creation path for an instantiated `%` DUP goes through P3.
- **K4:** no heap location reuse (H:317 bump allocator), so `KMAP` keys are unique.

## 3. Effective flags and harness (identical to the recorded gate evidence except the stated differences)
- Harness: `astra_contract.py` (sha `869aafcf…`), `astra_oracle.py`, `astra-repr/region_frontend.py`, guard
  `/home/lars/hoc/guard.sh` (sha `8c3ab7ed…`). Hashes are re-recorded at run time.
- **Reference C1:** `astra-repr/hvm_base` (`ea6cb779…`) on each case's `c1_source`, env with no `HVM_*`, args `-s -C64`.
- **Candidate C1^κ:** `hvm_kappa` (sha recorded at build) on the case's `pct_source`, env `{HVM_KAPPA=1}` only, args
  `-s -C64`.
- **κ-off control:** `hvm_kappa` on `pct_source`, env without `HVM_*`, args `-s -C64`. It must equal the reference
  EXACTLY on every row, in full multiset AND interactions. Any difference makes the construction invalid: stop and
  report, with no differential verdicts.

## 4. Caps and classification
- Per attempt: 1500 MB, 30 s, deadline 38 s. Collapse cap starts at 64 and escalates to a maximum of 4096, per harness
  (as recorded).
- **UNKNOWN, never agreement:** any timeout, cap limit, collapse cap reached, missing or unparsed output, nonzero exit,
  guard kill, or `KAPPA-*` abort, on either side.
- **Termination is reported explicitly per row:** exit code, timeout flag, complete flag, final cap, wall time, both
  sides.
- **Verdicts:**
  - EQUAL: both complete, full collapse multisets identical (residual / free-variable worlds included, not filtered);
  - MISMATCH: both complete, multisets differ;
  - UNKNOWN: otherwise.

## 5. Fixed row inventory (48 rows; nothing else)
| # | Rows | Manifest | E status label | Certificate / gate identity |
|---|---|---|---|---|
| 2 | `falsifier.issue18.minimal`, `falsifier.issue18.applied_branches` (make_B) | `astra_manifest.json` | **E-certified (source-bridged)** | `astra_pct_fixed_certificate_results.json` (restricted affine-beta, criteria (e) source bridge). NOTE: a term certificate, not an HVM-program-hash certificate. **Astra to confirm that this label is admissible**; otherwise relabel these rows UNKNOWN. |
| 2 | `contract.transport.erasing_capture`, `contract.transport.forced_capture` | `astra_pct_transport_manifest.json` | **E-certified** | `astra_pct_transport_certificate.py` results, per-copy VALID; identity = manifest pct / C1 sha |
| 2 | `contract.transport.uncopied_capture`, `contract.transport.data_copy` | same | **proved E-invalid** | same certificate, INVALID (counts toward O2b) |
| 3 | `contract.transport.unforced_substitution`, `forced_substitution`, `percent_forced_substitution` | `astra_pct_substitution_manifest.json` | UNKNOWN (no E certificate). **κ-inert**: at most one `%` use, so no `%` copier | control: C1^κ must equal C1 exactly, including interactions |
| 2 | `contract.transport.dup_lam_retained_binder`, `dup_lam_replacement` | `astra_pct_dup_effect_manifest.json` | UNKNOWN; **κ-inert** (single-use `%`) | control, as above |
| 6 | `suite.t0..t4.published_main`, `bounty.published` | `astra_manifest.json` | **mandatory gate** (E-UNKNOWN) | exact pct / C1 sha per manifest |
| 31 | the 31 `door.*` programs, exactly the backend-8 witness set (`snow_b8_witness_ledger.json`) | `astra_door_manifest.json` | UNKNOWN | manifest pct / C1 sha |

**Excluded:**
- Jan-4: there is no corpus fixture, and creating one is not approved.
- The 5365 paper witness: not a corpus case.
- The `labels.percent.*` cases: relevant, but not in the approved list. Adding them needs Lars's approval.

## 6. Per-row report (to Lars before any further step)
Each row reports:
- E-status label;
- C1: status, multiset sha256 + printed multiset, interactions, wall, exit, complete, final cap;
- C1^κ: the same fields plus `KAPPA_ALLOC`;
- κ-off: exact-equal Y/N;
- verdict (EQUAL / MISMATCH / UNKNOWN);
- interpretation class:
  - evidence against O2 (MISMATCH on an E-certified row);
  - O2b support (MISMATCH on a proved-E-invalid row);
  - uncertified (any verdict on an UNKNOWN / gate row; agreement reported as weak, uncertified support);
  - construction-control failure (any κ-inert row ≠ EQUAL).

## 7. Order of steps (each gated)
1. Astra reviews this spec; the OK and any required changes are recorded here.
2. Write P_κ. Astra reviews the diff (its sha recorded).
3. B0 toolchain check. Build `hvm_kappa`; record its sha.
4. κ-off control on all 48 rows. It must be exact, or stop.
5. The differential. Raw evidence is saved before any summary.
6. Report to Lars. Nothing further without his decision.

## 8. Astra review record
### Astra: design direction accepted for preparing the minimal patch and runner ONLY

Static review of F95D, following the proposal review in `astra_copy_aware_pct_rule_review.md` (D81C). This is NOT build/run authorization. Return the exact patched source, diff, runner and hashes for the next review gate. No VMOV/O1 implementation, new fixture, solver, words reuse or widened corpus is approved.

**Operational meaning accepted:** one fresh label per instantiated, marked SOURCE auto-dup node, keyed by its fresh ALO binding entry. This is an operational experiment, not a claim that the physical entry is already the complete semantic resource `(activation, enclosing-copy history)`. Each tree position has a different source node; ordinary body/field/commute descendants inherit the assigned label rather than getting another one.

Required clarifications/changes before the diff gate:

1. **K1 is not proved by output equality.** Kappa-off output+interaction equality is a mandatory calibration, not proof of identical books. The diff must preserve the cloned-let elaboration and label-allocation order by construction, with percent marking outside semantic heap storage. Record the marked book nodes and their original labels/site tree positions. Bound marking storage; overflow is UNKNOWN, never silently missed markings. Nested percent parsing and the numeric remainder operator must remain distinct.
2. **Correct K2's quantifier.** Source DUP bindings enter via REF/ALO and `wnf_alo_dup`; runtime `term_clone[_at]` also creates copiers and must NOT allocate kappa. The experiment needs coverage of marked source-DUP instantiations, not the false statement that every copier birth uses ALO-DUP. H:3975-4059 and 4785-4832 give the source/environment path. P3 must use the binding entry reached by the existing ALO environment lookup and preserve missing/unbound lookup behavior. Store/check the original static label with the mapped entry, so an unexpected door/entry association fails diagnostically rather than silently relabelling an unrelated handle.
3. **Do not infer ownership from the bump allocator.** Binding entries are newly allocated, but cells can be repurposed in place. The patch must leave reference role/lookup behavior unchanged and perform no raw-location re-freshening. No general native affinity or E proof is claimed.
4. **Namespace policy:** retain the conservative UNKNOWN guards. Scan all relevant parsed book SUP/DUP/DP/BJ-half label fields, not only percent nodes. The two numeric dynamic-label installation routes are DSU-NUM (H:4152-4155) and DDU-NUM (H:4199-4205); guard the exact masked label used by native construction before the semantic installation. Other inspected runtime propagation sites inherit an existing SUP/frame label. An unreachable static high label may therefore make a case UNKNOWN; report this, do not drop the row or rename public labels. Check exhaustion before allocation, never wrap. Do not alpha-rename visible labels in the output comparison.
5. **Diagnostic parsing:** the normal oracle rejects stderr. A wrapper must recognize exactly the specified complete KAPPA diagnostic, retain raw stderr, and separately record its parsed fields; any extra/unrecognized stderr remains UNKNOWN. Require the diagnostic and active-mode indication on successful kappa runs. Off/inert controls must report zero assignments. A missing diagnostic cannot be treated as zero.
6. **Controls:** compare full multisets including residual/free-variable structure and interactions on kappa-off runs. A complete disagreement is a construction failure and stops the batch. Incomplete controls are UNKNOWN, not evidence of a broken construction or successful calibration, and cannot support the associated kappa verdict. The five single-use/no-percent controls must also have zero assignments and identical interaction counts when kappa is on.
7. **Finite budget:** sequential execution, the stated 30 s / 1500 MB per-attempt guard and 38 s harness deadline, plus a 15-minute batch deadline. Escalate only a completed collapse-cap attempt, up to the stated 4096 maximum; do not retry a guard/namespace/map abort as though it were a collapse-cap event. At most seven cap attempts per row/mode (64 through 4096); unfinished rows are UNRECORDED/UNKNOWN. Never raise caps to obtain a pass. A timeout is not a proof of mathematical nontermination.
8. **Identity and scope:** freeze an explicit 48-row name/hash list, reference pin, parser/harness/guard hashes, effective environments and source include dependencies if present. The five targets plus bounty are exact mandatory gates, still E-UNKNOWN. Preserve separate E and mandatory-gate fields. Jan-4 has no separate executed row; the paper freshening witness and labels.percent cases remain excluded absent Lars's approval.
9. **Costs and interpretation:** rule interactions retain their native meaning; kappa allocation/lookups are experiment metadata, not evidence for a bounty count or speedup. Report assignment count, wall time, exits/abort reason, complete status and final cap. A mismatch on an E-invalid row is non-E sensitivity/O2b evidence, not proof that E licenses the transformation. Finite agreement never establishes O2 or its universal negation.

**Issue18 source-bridge admission for this T1 only.** The two exact sources were read and their hashes checked against the manifest. They are the fixed minimal/make_B programs of criteria (e), including the fixed observers. Use `E-certified (restricted source-bridged certificate)` with these pins, not a name-only join:

- Minimal pct `771f5cf9534f5e1c2d9d0e03fee519a4d6962a709ecb5911a4e3ffdf4c553f10`; C1 `7acd805d64d40b34c22233849ac684f3156924453a9241198353c42f5672cfba`.
- make_B pct `b434b47c2279ace2bbfcc58e8a0db5b65842a73dcb9e79d912ad919c9658ec20`; C1 `c8593e8c380c61ea5d3a723b1d9125fb5f9e82a91e19165b677e1518fd8a0236`.
- Fixed certificate script `5b302a81821691463f4b951dbc4f697391ada67f581c227f9422227958c60ebc`; retained results `8e892842252f705fe64b8e5aebc103d7b17a3e1b8c6ead8e2291b972a7c17345`.
- Transport certificate script `d9e44f7ac8b63b8fd820100defbabbef86e50bdc730c90fa13fd429bfe0d56b7`; retained results `0df58b3f3ec038336612401427840f1ac52c943ee1198c028cb479d866e0800d`. Keep its exact transport-manifest pct/C1 pins and the distinct valid/invalid per-copy classifications.

This is a present source-to-existing-certificate admission, not a retroactive edit of the backend-8 ledger or the old certificates. No certificate was rerun and no new general transport theorem is asserted.

**Next gate:** source/diff and runner review; then exact build pins and bounded execution authorization. Lars receives results before any follow-up. The previous unmodified GCC reproduction record may be reused if the toolchain/recipe is unchanged; an unexplained byte mismatch on a requested reproduction is a stop, not permission to substitute another reference.

## 9. Prepared artifacts for the source / diff / runner gate (SNOW). NOT built, NOT run

**Artifacts.**
| Artifact | Path | sha256 |
|---|---|---|
| Base (pinned upstream 6defdfc) | `astra_evidence/reference_repro_6defdfc_gcc_o2/src/hvm.c` | `3d2724d0716b5d6b1c07a3b0b3c5cb89f848487a43d364ea689658f9aeb75fe7` |
| Patched source P_κ | `snow_t1_kappa/hvm_kappa.c` | `d2253321172ea154f266fbf6234a2cb9c408ab28ae852bb90437b008bb362b65` |
| Diff (12 hunks, 383 lines) | `snow_t1_kappa/p_kappa.diff` | `f6880a42046ce35e4f6c70cc4df80309e8a743241de84edb76a1549ed10c4207` |
| Runner | `snow_t1_kappa_runner.py` | `14dfdfabfd4027e8ce02c9f55198964bd04e23577b122ae31568ee480a1df4c5` |
| Row freeze script (read-only) | `snow_t1_kappa_freeze.py` | `9f453f97b620f236164b492dfff7da52df712d57001b4831331a0e3ea1fab037` |
| Frozen 48-row inventory | `snow_t1_kappa/rows.json` | `89988610f1f821749ea4508399a1d3732193c42826e2891b7bc0032d51d757a8` |

**What has and has not been executed.**
- Executed: the freeze script, and the runner's default PLAN mode. Both are read-only. PLAN verified the guard
  `8c3ab7ed…`, `hvm_base` `ea6cb779…`, oracle `ba82c5e3…` and contract `869aafcf…` pins, and loaded all 48 rows
  through `astra_oracle._case_sources` (manifest provenance plus the exact lexical-C1 check).
- NOT executed: no compiler (not even a syntax check) and no native process.

**Diff hunks** (base line → purpose).
- **227** — the P_κ state, all outside the semantic heap:
  - marks `PCT_MARKS` (cap 65,536) with a hash index;
  - KMAP (2^24 slots), allocated only in on-mode, holding `bind_ent` → (κ, original static label);
  - `kappa_abort` (one `KAPPA-ABORT reason=R alloc=n` line, exit 77);
  - `kappa_alloc` (exhaustion checked before allocation at `PARSE_DYN_LAB`; never wraps);
  - `kappa_birth` (mark lookup, original-label check `KAPPA-MARK-LABEL`, `KAPPA-REBIRTH` instead of re-freshening a
    location, map-load abort);
  - `kappa_door` (unmapped means reference behaviour; mapped means an original-label check `KAPPA-DOOR-LABEL`, then κ);
  - `kappa_dyn_check`.
- **2081** — in `parse_auto_dup`'s chain loop: record `(loc, lab+i, i, site)` only while this binding's marking is
  active. `uses ≤ 1` returns earlier, so no copier and no mark.
- **2579** — `pct_pattern_form` plus the head of `parse_term_dup`. `%` follows exactly the `! & R` path: not strict,
  `parse_term_dup_pat` skipped, `cloned = 1` in place of consuming `&`. Pattern forms of R, and non-`=` forms, abort
  (`PCT-PATTERN-FORM` / `PCT-FORM`), so a row using them is UNKNOWN.
- **2647** — the cloned-let `parse_auto_dup` call: marking is active only for a `%` binding (saved and restored around
  the call, so nested `%` and `!` sites in the value or body cannot leak). This is the only hooked call: the `λ&x`
  call (base H:2434) is untouched.
- **3502** — atom-position `%` sets `PCT_PARSE_NEXT` and enters `parse_term_dup`. The binary remainder operator is
  parsed in the operator loop (H:3373 / 3415), so it is unaffected.
- **4008** — `wnf_alo_cop`: only for the binding entry `it` reached by the EXISTING environment lookup, and only when
  `it != 0`. Missing or unbound lookups are unchanged.
- **4034** — `wnf_alo_dup`: κ birth for marked source nodes, keyed by the fresh `bind_ent`. Runtime `term_clone[_at]`
  copiers are not touched, so they inherit labels as in the reference.
- **4152 / 4199** — DSU-NUM / DDU-NUM: `kappa_dyn_check(lab & EXT_MASK)` before the native construction.
- **6367** — `kappa_init` and `kappa_report`:
  - `HVM_KAPPA` unset means off; `"1"` means on; anything else is an abort;
  - in on-mode, κ_lo := final `PARSE_FRESH_LAB`, and a scan of ALL parsed book SUP / DUP / DP / BJ labels (except the
    `PARSE_DYN_LAB` sentinel) aborts `KAPPA-STATIC-COLLISION` if any is ≥ κ_lo;
  - the report prints exactly one line after a normal evaluation return:
    `KAPPA mode=<on|off> alloc=<n> marked=<m> lo=0x<6hex> next=0x<6hex>` (off-mode prints `lo=next=0x000000` and
    `alloc=0`).
- **6417 / 6426** — `main`: `kappa_init()` after a successful `runtime_prepare`; `kappa_report()` after
  `runtime_eval_main`. Any internal `exit` means no diagnostic, which the runner treats as UNKNOWN.

**Mapping to the required changes in section 8.**
1. **K1:** cloned-let elaboration and label-allocation order are kept by construction. The same calls are made in the
   same order, and `parse_term_dup_pat` on `& name =` allocates nothing in the base. Marks live outside the heap, with
   original labels, site and tree position. Overflow or duplicate marks abort. Nested `%` / remainder are distinct.
   κ-off equality is used as calibration only.
2. **K2 quantifier:** only marked source-DUP instantiations via `wnf_alo_dup` get κ. P3 uses the existing lookup's
   entry with an original-label check.
3. **No ownership inferred from allocation:** κ is assigned only at birth. An existing key aborts (no re-freshening);
   reference roles and lookups are unchanged.
4. **Namespace guards** are as listed above. Unreachable high static labels make a row UNKNOWN; it is reported, not
   dropped, and labels are not renamed.
5. **Strict diagnostic:** the runner accepts stderr only as exactly one full KAPPA line (stripped before
   `oracle.parse_output`; raw kept and hashed) or one KAPPA-ABORT line with exit 77 (UNKNOWN). On-runs need
   `mode=on`. Off-runs need `mode=off` and `alloc=0`. A missing or unrecognised diagnostic is UNKNOWN.
6. **Controls:** κ-off must be EXACT (multiset and interactions) or the batch stops, and an incomplete calibration makes
   the row's verdict UNKNOWN. The 5 κ-inert rows must have on-mode `alloc=0`, `marked=0` and identical multiset and
   interactions, or the batch stops.
7. **Budget:** sequential execution; 1500 MB / 30 s per attempt; 38 s deadline; caps 64…4096 (≤ 7 attempts), escalated
   only on a sole `collapse-cap`; aborts, guard kills and timeouts are never retried; a 15-minute batch deadline; rows
   not reached are UNRECORDED.
8. **Identity:** the frozen 48 rows (`rows.json`) with manifest / pct / C1 sha, issue18 pins as admitted, certificate
   pins verified, separate `e_status` / `mandatory_gate` / `kappa_inert_control` fields. Jan-4, the 5365 witness and
   `labels.percent.*` are excluded.
   - Environments: REF / OFF use the inherited environment with every `HVM_*` removed; ON adds only `HVM_KAPPA=1`.
   - Include dependencies: none. Checked: no `import` or `#include` text occurs in any of the 96 row source files
     (48 × pct / C1).
9. **Costs:** κ allocations and lookups are metadata (reported `alloc` / `marked`), not interactions and not speed
   evidence.

**Next gate (requested):**
- (a) Astra reviews the diff, runner and rows;
- (b) if OK, exact build authorization: B0 toolchain reproduction of `hvm_base` (or reuse of the recorded
  reproduction), then `gcc -O2 -o snow_t1_kappa/hvm_kappa snow_t1_kappa/hvm_kappa.c` with the binary sha recorded;
- (c) bounded execution authorization from Lars.

Results go to Lars before any follow-up.

## 10. Astra source/diff/runner gate

Review: `astra_t1_kappa_source_review.md` (33AC).

The exact C source d2253321 / diff f6880a42 is accepted for ONE build with
the recorded GCC `-O2` recipe and a unique candidate path. Preserve build
command, compiler identity/output/exit and resulting binary hash. Reuse the
existing successful upstream reproduction when the toolchain is unchanged.
This is build-only permission, NOT permission to execute the binary.

Execution remains BLOCKED by the runner/freeze requirements H1-H7 in that
review: all-48 REF/OFF calibration before any ON process; immediate stop on a
complete calibration mismatch; a running attempt clamped to remaining batch
time; approved rows/source/frontend identities enforced; full per-attempt and
incremental row records with effective environments; verification of the
transport RESULTS artifact; complete frozen metadata on unrecorded rows.
Incomplete calibration is UNKNOWN and cannot pass the differential's gate.

Return revised runner/freeze/row pins plus the candidate build record/hash for
the final bounded-execution gate. No VMOV, widened corpus, certificate rerun,
solver, native/model run or Words work is authorized by this review.

## 11. SNOW return for the bounded-execution gate (H1–H7 addressed; candidate built, NOT executed)

**Build (the one approved build).**
- Recorded by `snow_t1_kappa_build.py` (`b6e54d26…`) into `snow_t1_kappa/build_record.json` (`5f2c08f1…`, written
  with exclusive creation).
- Source `d2253321…` and diff `f6880a42…` verified before compiling.
- Compiler identity is byte-equal to the recorded upstream reproduction:
  `gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0`.
- Command `gcc -O2 -o snow_t1_kappa/hvm_kappa snow_t1_kappa/hvm_kappa.c` (cwd `search/`), exit 0, empty stdout.
- stderr has 3 warnings, identical to the upstream reproduction's 3. There are no new warnings.
- **Binary `snow_t1_kappa/hvm_kappa` sha256 `8e0ab73cd43c4aadab3f43807f4f19818e50dc200d2fabe59356858b31a81762`.**
  Recorded `binary_executed: false`, and it has not been executed.
- The upstream reproduction record (`reference_repro_6defdfc_gcc_o2/record.json`) is reused, not rerun.
- The builder refuses to rebuild if a binary or record already exists.

**Revised pins.**
| Artifact | sha256 | Change |
|---|---|---|
| `snow_t1_kappa_runner.py` v2 | `ecdd6d4fd438ae307de56206504fab08b1a895ac9e19ffa6377750646692d839` | H1–H5, H7. Diff vs reviewed v1 (`14dfdfab…`, preserved as `snow_t1_kappa/runner_v1_reviewed.py`): `snow_t1_kappa/runner_v1_to_v2.diff` (`fb16acb3…`) |
| `snow_t1_kappa_freeze.py` v2 | `7cb4886562916fc8103c542b737948a2aa6fd0238c7f0523c8a8a7ff04e09ae2` | H6. Diff vs v1 (`9f453f97…`): `snow_t1_kappa/freeze_v1_to_v2.diff` (`8ebceaf2…`) |
| `snow_t1_kappa/rows.json` (re-frozen) | `e0cb8f328cb4231f3e908473279a1e43b4e1bcb4dc316038576e801a04f0cc92` | The ONLY field change vs v1 (`89988610…`, preserved as `rows_v1_reviewed.json`) is `certificate` on the 4 transport rows, which now name the verified results artifact. Names, order, hashes, E / gate / inert classes are unchanged. This needs a new explicit pin from Astra |

**Mapping of H1–H7.**
- **H1:** phase 1 runs REF / OFF for all 48 rows. A complete disagreement stops immediately and no ON process ever
  starts. Phase 2 (ON) starts only if all 48 calibrations are complete and EXACT; otherwise
  `stop = 'differential NOT started…'` and every ON is UNRECORDED. Incomplete calibration is UNKNOWN.
- **H2:** each attempt's process-group deadline is `min(38 s, remaining batch)`. There is no launch with no remaining
  time. `ended_by` is `harness-38s-deadline` or `batch-15min-deadline`. Only the attempt's own group is killed. Raw
  bytes are kept, and an interrupted attempt is UNKNOWN.
- **H3:** `PINS` enforces guard, `hvm_base`, `region_frontend.py` (`361f3989…`), oracle, contract, patched source,
  diff, binary and the rows hash. The build record must match the binary and say not executed. The 48 names are
  unique, and each row is unique in its manifest. Sources are loaded through `oracle._case_sources`. The exact source
  bytes are snapshotted per attempt (`program.hvm`, with path and sha in the record).
- **H4:** each attempt writes an exclusive `record.json` immediately after capture. It holds the full parser result
  (multiset, interactions, reasons, KAPPA diagnostic / abort), exit / timeout / exception, effective deadline and
  limits, command and cwd, environment, binary / guard / source identities, stdout / stderr paths and hashes. Each
  mode writes `<mode>.json` linking its attempt records with their hashes. Each row writes `calibration_row.json` /
  `differential_row.json` before proceeding. Launch or capture exceptions produce an UNKNOWN attempt record. A
  `finally` block always writes `results.json` with the prior evidence. Escalation happens only on a sole
  `collapse-cap`. `final_cap` is the last ATTEMPTED cap, and `escalation_cut_by_deadline` is recorded.
- **H5:** `identity.json` (local only) stores the full effective REF / OFF / ON environments, and every attempt
  record stores its environment. Chat summaries will not include them.
- **H6:** the freeze verifies script AND results for both certificates. Transport results:
  `astra_pct_transport_certificate_results.json` `0df58b3f…`.
- **H7:** every row in `results.json` carries all frozen fields (mandatory gate, inert-control flag, manifest and
  source hashes, certificate). Unrun modes are `{status: UNRECORDED}`, with verdict and interpretation
  `no comparison (UNRECORDED)`, distinct from completed comparisons.

**Executed in preparing this:** the build (approved), the freeze (read-only) and the runner PLAN mode (read-only pin
checks, no native process). **Not executed:** `hvm_kappa`, and the runner `--execute` path.

**Requested:**
- (1) Astra's review of the runner v2 / freeze v2 diffs and an explicit pin of rows `e0cb8f32…` and binary
  `8e0ab73c…`;
- (2) Lars's explicit bounded-execution authorization (48 rows, 3 modes, sequential, 30 s / 1500 MB, ≤ 7 caps up to
  4096, 15 minutes total).

Results go to Lars before any further step.
