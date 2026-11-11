# PROPOSAL v3: positive route. A `%` mechanism using E JOINTLY with checked invariants (SNOW)

> **STOPPED (Lars ruling on attribution, DSCRD).** The stated contract (v4, v5 note) uses SOURCE-USE attribution.
> Bridge B (output-component attribution) is NOT part of the stated contract; it is a contract-strengthening
> candidate for the deferred strengthened-promise phase. Under outcome (ii) the EJ-MOV design STOPS.
> - The text below is retained as a record only. No build or run plan will be written.
> - Recorded findings, in Astra's `pct_scoped_negatives_report.md`:
>   - the bridge-B finding;
>   - the attribution ruling;
>   - "the E-advantage exists only relative to the confinement ruling; an unconfined generic alternative plausibly
>     recovers essentially all of it".

**Status: paper proposal only, on PAPER HOLD per Astra's review (`astra_positive_route_review.md`, C41F).**
- No build, run, solver or words work.
- v2 answers the five required revisions of C41F (section 10 maps each one).
- All soundness, cost and fusion statements are obligations (O-…) or `[INFERENCE]`.
- The five targets remain **E-UNKNOWN**.

**v1** (`10eb1703`) is superseded. Its claims are withdrawn where C41F found them unsupported:
- the confinement lower bound;
- the "outside-E" classification of the section-3 witness;
- GK as a closure argument;
- the strict-discard row;
- "bounty < 50k iff coverage".

---

## v3: Lars's rulings Q1 / Q2 applied (OVERRIDES the v2 text below wherever they conflict)

**Rulings.**
- **Q1:** the `%` mechanism stays CONFINED to the `%` machinery.
- **Q2:** the ONLY permitted generic-rule hook is ONE metadata bit maintained at the generic stack push. It is active
  only when the program contains `%`, it is semantics-neutral, and it is fully costed.
- BUILD NOT approved.
- The write-up must state that any asymptotic E-advantage is RELATIVE to this confinement, and must estimate what a
  generic alternative could recover.

**v2 items that used generic hooks, now REMOVED, with their confined replacements.**

| v2 item | Generic hook (now excluded) | v3 confined replacement | Consequence |
|---|---|---|---|
| event-precise COPY-SPLIT (O-MAP) | copy-event ids inherited at derived-copier creation sites | E-certifiable record versions are ONLY: (i) an untouched ACT record (all doors are distinct source occurrences of ONE activation instance, never separated by a copier); (ii) children of a K-aware SUP split keyed by the SUP NODE identity, not its numeric label. A binder SUP is born once per DUP-LAM event, so a split on it is event-precise with no hook. COPY-SPLIT children (lambda values touched by ordinary copiers) are NEVER E-certified: the fast path is refused and G applies | O-MAP must now be proved only for (i) / (ii). Label-memo sharing across events is never used for an E inference |
| PB binder confinement | the "may-leak" bit at same-label DUP-SUP annihilations | **PB-c (confined):** the moved lambda's binder slot is unwritten (a read of the cell), AND its body cell is still an unreduced ALO code handle (a read of the body cell: an ALO-LAM output keeps `heap[bind] = ALO(body)`, whereas a DUP-LAM copy's body is a DP projection), AND its code site contains no SUP literal (a static book read at load). Lambdas produced by DUP-LAM fail PB-c | PB-c is strictly weaker in coverage than v2's PB |
| SC scan, O(frames) | — | Q2 bit at the stack push: `clean[p] = clean[p−1] ∧ frame_p ∈ {APP-head, ordinary-DP-demanded}`. O(1) per push, charged per push, maintained only when `%` is present. The SC check at a consumption is then O(1) | cost row updated |

**What confinement does to target coverage (paper, `[INFERENCE]`).**
- At the final application, the continuation values consumed in t1–t4 / the bounty are reached through `rep`'s
  ordinary R copies. They are DUP-LAM copies, whose bodies are DP projections, so **they FAIL PB-c**.
- **Without bridge B,** EJ's fast path therefore probably does NOT apply to the targets' continuation consumptions
  under confinement. EJ would not fuse t1–t4 / the bounty, and the targets fall back to G (no fusion; VMOV v2 §6).
- **With bridge B (§4.1),** PB is not needed for E programs: a retained-binder observation of an omitted layer would
  be a sibling contribution, which E + UC excludes. The fast path then needs only SC (Q2 bit), GK′ and the confined
  O-MAP (i) / (ii).
  - In the targets the relevant splits are binder-SUP splits from `rep`'s DUP-LAMs, i.e. case (ii), so confined
    O-MAP plausibly covers them `[INFERENCE]`.
- **B is NECESSARY, not sufficient, for this design under confinement** (narrowed per Astra 2847). Without B, the
  confined fast path has no E-based answer to retained-binder effects of the §4 type. With B for that case, the
  remaining obligations (O-SKIP for all other omitted effects, UC, O-MAP, O-INH, public-label preservation,
  termination) are still open, and target coverage is an inference.

**Honest statement required by Q1: what a generic alternative could recover (paper estimate).**
- G+ is the unconfined generic design: G plus a snapshot copier per consumption, plus binder-escape tracking at
  generic DUP-LAM / annihilation sites, plus copy-event ids.
- **G+ would plausibly recover essentially ALL of EJ's asymptotic gain** `[INFERENCE]`:
  - its snapshot plus escape trap also avoids O(|word|) materialization at consumptions whose binder has not escaped;
  - lazy projection handles K-sides;
  - sibling reads use the snapshot;
  - G+ needs neither E nor certificates.
- **The residual E-dependent advantage of EJ over G+ is a constant factor per certified consumption:** no snapshot
  copier, and no escape bookkeeping on generic rules.
- **So any asymptotic E-advantage of EJ exists ONLY RELATIVE TO the confinement ruling.** Without confinement, a
  generic mechanism plausibly matches it.
- This also means G+ would plausibly fuse the DUP-version programs (`insert_A`, `clr_dup` …) too. G+ is a generic copy
  optimization that criteria (c).4 does not count as a `%` result.

**Next (per Lars):** Astra reviews v3. SNOW revises. Then a CONCRETE guarded implementation / run plan goes to Lars
for explicit approval before any build or run: exact patch scope, pinned base, corpus including the future-corpus rows
(`a00452c7`) and the §4 challenge row, caps, UNKNOWN handling, controls, and a flag-off identity check. **That plan is
NOT written yet**, because B and O-SKIP decide whether a build is meaningful.

---

## 0. Summary of what v2 claims and does not claim

**Two layers.**
- **G (generic, not counted):** a K-aware exact lazy representation of C1's `%` copier tree. Its obligations O-G are
  unchanged from D81C §2 and C41F §4.
- **EJ (the `%` step):** at a consumption meeting checked conditions, move the value without firing C1's `%` copier
  path.

**The `%` content is split into two parts.**
- **C-DEAD (accepted by Astra as a conditional logical step):** E + UC(d) ⇒ no distinct source occurrence of the same
  actual resource contributes in any world.
- **O-SKIP (the central OPEN obligation):** every C1 effect omitted by the move is unobservable. v2 does NOT derive
  O-SKIP from C-DEAD alone. It adds an explicit checked property, binder confinement PB with lazy layer replay
  (section 3), and states O-SKIP as the obligation that PB + C-DEAD + GK′ must discharge.

**Where E enters.** Only through C-DEAD. PB, GK′ and SC are generic checks. Without E, PB + GK′ + SC do not imply that
an untouched sibling occurrence is non-contributing.

**Advantage over a generic design (superseded by the v3 section above).** Relative to Lars's confinement ruling, an
asymptotic E-advantage may exist on the targets ONLY if bridge B holds. Without confinement, G+ plausibly recovers
essentially all of it, leaving a constant-factor E-dependent residue.

## 1. Layer G (unchanged in role; generic)
The table is as in v1 §1:
- ACT (single-use: no record);
- doors with words;
- READ-ATOM, READ-VAR;
- K-aware SUP (annihilation by the innermost word side; handles 5365);
- COPY-SPLIT;
- MOV-MOV;
- MATERIALIZE (fires the door's C1 path with C1 labels).

**Change (item 4):** COPY-SPLIT is memoized by COPY EVENT, not by `(record, numeric label)`.
- A copy event is the root ordinary copier of one logical copy (a DUP-LAM or other root firing). Its id is inherited
  by every derived copier: body, field and commute copiers.
- This is a generic metadata hook at the derived-copier creation sites. C41F §6 says criteria (b) permits such hooks;
  the cost is charged.
- A child record = (parent version, event e, side s).

Open obligations O-G remain as listed in C41F §4.

## 2. The reference relation (item 4)

**C1 counterpart of an EJ state.** Every EJ state S corresponds to a C1 state C(S), obtained by re-inserting the
OMITTED objects of every fast move. For a move of record version V's value to door d, the omitted objects are:
- (a) the `%` copier nodes on d's path;
- (b) the copies made by those copiers for the other doors;
- (c) every binder write those copiers perform on cells they copy, together with the derived copiers they leave on
  free variables;
- (d) every SUP born from (a)–(c).

C(S) is defined only for states reached under the conditions in section 3.

**Resource mapping (for the E inference).** The siblings that C-DEAD may treat as "distinct source occurrences of the
same actual resource" are ONLY:
- the other doors of the SAME record version V;
- where V is either the record created by ACT for one activation instance, or an event-precise COPY-SPLIT child
  (parent, e, s).

Same-side doors of one event e are copies, made by the same logical copy, of doors of one parent resource. Under v4:
- if e is an enclosing-closure (capture) copy, they all carry the forked resource (parent, e·s);
- if e is a data copy, they carry the parent's resource.

In both cases they share ONE actual resource with d. **Obligation O-MAP:** prove this from v4's transport rules,
covering nested and mixed paths and repeated labels (C41F §4). Any door whose version cannot be placed by O-MAP is
excluded from the fast path (the move is refused, falling back to G).

**World relation.** UC is defined over the WORLDS OF C1 run from the related state C(S) (C41F §4: not over EJ's
future worlds).

## 3. EJ conditions (all checked at the consumption; otherwise G)

A consumption of door d in record version V is FAST iff all of the following hold.

**SC (control certificate).** As in v1 §2.1:
- an APP head or readback at an output root;
- only APP-head or ordinary-DP-demanded-side frames up to it;
- no MAT / SWI / USE / OP2 / EQL / AND / OR / DSU / DDU frame;
- empty driver world path.

**O-UC (open):** SC at state S ⇒ d contributes in every C1 world of C(S)'s continuation, including later CNF lifts,
shared substitutions and residual / lambda readback. **Q3 is NOT accepted by Astra.** It stays an obligation;
section 7 lists what its proof must cover.

**PB (binder confinement; NEW; generic check).** The moved value `v` is either:
- an atom (no binder); or
- a lambda cell whose binder slot has never been written (no prior APP / DUP-LAM on it), AND whose binder occurrences
  are CONFINED: the cell was created by ALO instantiation, or by a DUP-LAM whose copied body contained no SUP literal
  with that copier's label on a path to the binder occurrence.

The second clause is tracked by a one-bit "may-leak" mark set at DUP-SUP annihilations of a copier with its own label
inside a body copy (a generic metadata hook). That is exactly the handler-control leak shape.

*Why PB targets O-SKIP:* under PB, the omitted K binder write `x := SUP_K(x0,x1)` has readers ONLY inside v's body
copies, which the K body copier projects side by side. The selected side reads x0, and the argument written there by
d's application equals EJ's direct write. The x1 side is reachable only through the sibling copies (b).

**Lazy layer replay for environment reads (NEW; addresses retained aliases).** The moved value's FREE variables
(captured environment) would, in C1, carry the omitted path copiers (c). EJ therefore attaches the omitted path as a
pending LAYER STACK to the moved closure. When the closure's computation first demands a free variable's value w:
- w is an atom, or a variable-to-SUP chain that gets K-aware SUP treatment: no layer effect, so pass through.
- w is a lambda: apply PB to w recursively. If PB(w) holds, pass through, with layers transferred to w's own
  environment. If PB(w) fails, MATERIALIZE the pending layers on w exactly as C1 would fire them, giving C1's binder
  writes on w.
- Otherwise (CTR with fields, etc.): fields are handled lazily by the same rule.

Cost: one check per first demand of an environment value, plus materialization when it is needed.

**GK′ (redefined relative to C1's omitted births; item 3).**
- GK′ holds iff no `%`-site-label SUP is reachable in C(S), counting ALSO the omitted births (d).
- Under PB and lazy layer replay, the omitted births of (d) are confined to: v's own body projection (annihilated
  identically on the selected side), the sibling copies (b), and layers materialized lazily (which are then REAL
  births in EJ).
- So GK′ reduces to the executed guard GK: no executed `%`-label SUP birth and no public installation of such a label.
  That leaves the inductive obligation O-GK′: "omitted births are confined as stated".
- The public-label trap remains (5365).

**C-DEAD (the E step).** With O-UC and O-MAP: E + UC(d) ⇒ no other door of V contributes in any C1 world.

**O-SKIP (central, open).**
- Under SC ∧ UC ∧ PB ∧ lazy layer replay ∧ GK′ ∧ C-DEAD, every omitted object (a)–(d) of the move is unobservable:
  - (a) and (b) are reachable only through V's other doors (dead by C-DEAD and never demanded; a demand is a tombstone
    hit, so replay);
  - (c) on v's own binder is handled by PB;
  - (c) on the environment is either materialized exactly or passed through under PB recursively;
  - (d) is handled by GK′.
- Proof obligations: every skipped cell write and side selection, its possible readers, and preservation of effects on
  the selected copy and on aliases outside the record (C41F §1).

## 4. The section-3 witness, reclassified (item 2)

```text
@main =
  ! &F{f,g} = λx.&F{x,#Other{}};
  ! &F{a,b} = f(#First{});
  % h = g;
  #Pair{h(#Second{}), (λu.b)(h)}
```

- **C1 two worlds vs naive-MOVE one world:** this paper derivation is consistent with the pinned CNF child order (C41F
  §2).
- **E status: UNKNOWN** (not outside E, and not E-valid).
- **Under v2,** `g` FAILS PB: its binder `x1` is retained by `b` through the F-label annihilation, so the may-leak bit
  is set. The consumption is therefore NOT fast; G MATERIALIZEs and reproduces C1's two worlds.
- **The program is now a mandatory paper CHALLENGE row for O-SKIP / PB**, not evidence for or against E-enabling.
- **Consequence for the "E is needed" argument:** v1 used this program to show that the fast path is not generic.
  With PB in place it no longer shows that. A replacement separation witness is needed. It must be a program where SC
  ∧ PB ∧ GK hold, a sibling occurrence contributes in some world (so E fails), and the fast move changes C1's output.
  **Its existence is OPEN.** If none exists, the fast path would be generic (PB + SC + GK sufficient), and the
  `%`-enabling claim fails (falsifier F2).

### 4.1 The decisive question: bridge B

Writing v2 exposed the following dichotomy. It is a paper observation, not a theorem.

- **Under PB, E is not needed for correctness.** With the binder confined and siblings never read (a read is a
  tombstone hit, then replay), the omitted objects (a)–(d) have no reader outside the selected projection. So
  SC ∧ PB ∧ GK′ plus tombstone / replay would preserve C1's output WITHOUT E `[INFERENCE; O-SKIP under PB]`.
  - E would then at most reduce replays, and not even that: a non-contributing physical sibling demand still forces a
    replay.
  - EJ-with-PB would be GENERIC (F2).
- **E can do essential work only where PB fails,** that is, where an omitted `%`-label binder layer IS observable
  through a retained alias (the §4 shape).
- **Bridge B:** an observable effect of an omitted `%` firing that is visible only on a SIBLING side of a `%`-label
  SUP (for example the retained `b = x1` world in §4) is a v4 contribution of that sibling SOURCE OCCURRENCE in that
  world. C41F §1–2 says this occurrence-to-effect bridge is not established.
  - **If B holds (for this effect class):** E + UC(d) would exclude retained-binder observations of omitted sibling
    layers of the §4 type, so PB would not be needed FOR THAT EFFECT CLASS.
    - This is NOT a soundness theorem for EJ: O-SKIP for every other omitted effect, UC, O-MAP, O-INH, public-label
      preservation, termination and replay remain independent obligations.
    - The §4 witness would be E-invalid under that reading.
  - **If B fails:** E does not cover this effect class, so the EJ design needs PB (or an equivalent check) for it.
    - This does NOT prove that PB is necessary for every E-enabled mechanism, nor that every E-enabled mechanism is
      generic. Mechanisms that keep or defer the binder write, or combine E with other information, remain open.
      Those necessity / exhaustiveness claims are unproved.
- **So, for THIS design family, B is a necessary condition for an E-enabled fast path to reach the §4 effect class.**
  It is not sufficient for soundness, and its failure is not a general negative. B is a question about v4's
  contribution reading for ERASED source occurrences whose copier component is observed through a retained binder.

## 5. Corrected control rows

- **5365:** the public install of a `%` label makes GK false, so G (K-aware annihilation) gives `{Left:1}` = C1, if
  O-G holds.
- **Issue #18 minimal / make_B:**
  - REF values make READ-ATOM apply in G.
  - With heap-lambda values: event-precise COPY-SPLIT gives per-copy versions. The certified `a(b)` consumption moves
    under PB (instantiated, unwritten, no leak).
  - The sibling (the door dropped by `@fst`) is in the same version, so it is dead by C-DEAD, subject to O-UC / O-MAP.
- **Jan-4:** `G = λy.y`. Its APP-SUP argument copies are COPY-SPLIT event children, and `H₀(I₁)` is the root head. If
  O-UC / O-MAP hold, the move applies and the result is the identity, = C1.
- **Handler + DUP-LAM-effect controls:** single-use, so no record; C1 verbatim.
- **Two-use retained-binder variants:** PB fails (may-leak), so G applies.
- **Strict discard** (`!! u = h(1); h(2)`, corrected per C41F §3):
  - `h(1)` is under USE, so MATERIALIZE. When `h`'s value is a NON-erasing lambda, this creates a `%`-label binder SUP,
    and GK turns false.
  - `h(2)` is then NOT fast: it is G's read of the cached half, exact by O-G.
  - If any fast move preceded the flip, replay is required by policy. If `h`'s value has an erasing binder (no SUP
    birth), GK stays true, and `h(2)` may be fast if SC / PB hold.
- **Superposed scrutinee / literal; identical-branch match:** SC fails, so G applies (exact by O-G). There is no E
  advantage in these contexts.

## 6. Replay: termination and output commitment (item 5)
- **Finite-prefix discipline.** The speculative EJ prefix is budgeted. If EJ has performed any fast move and the
  prefix exceeds `B = c · (interactions at the last fast move) + B0`, EJ aborts and replays in G.
  - `c` and `B0` are stated constants. The work is charged.
  - This bounds the speculative waste to a constant factor of the work that was useful when the move was made.
  - It does NOT prove that EJ terminates whenever C1 does. Obligation **O-TERM**: on E programs satisfying the
    conditions, the fast path changes no demanded control path, so EJ's prefix follows C1's demand order. Otherwise
    the budget triggers replay.
- **Output commit.** Collapse output is BUFFERED until the evaluation (EJ or the replay) completes, and only the
  completed run's full multiset is emitted. Buffer memory is O(output) and is charged.
  - A replay discards the buffer and all EJ heap / metadata state (a fresh runtime).
  - On divergence, nothing is emitted (UNKNOWN), matching the harness's treatment.
- **Detection completeness** (tombstone / GK hits) is part of O-SKIP / O-REPLAY. It is not assumed from the flag's
  existence (C41F §5).

## 7. Obligations

**O-G**, **O-MAP**, **O-UC** (over C1 worlds of C(S): later lifts, shared substitutions, residual / lambda readback),
**O-INH** (occurrence-level, for nested words), **PB-soundness** (the may-leak bit covers every binder-retention
route: annihilation leaks, unscoped binders `UNS`, late arguments), **O-GK′**, **O-SKIP**, **O-TERM**, **O-REPLAY**,
**O-COST**.

**Priority for paper work:** O-SKIP under PB, then O-UC, then O-MAP. These decide whether EJ is sound. The separation
witness (§4) decides whether EJ is a `%` result at all.

## 8. Targets: no fusion claim (item 5)
- v1's "fuses iff coverage" and "bounty < 50k iff coverage" are withdrawn.
- A per-target recurrence would have to count: G events, COPY-SPLIT ordinary copy work, event-id and word / site-map
  storage, memo lookups, SC scans, PB checks, lazy-layer materializations, and replay budget.
- **Open target-specific question:** do the continuation closures consumed at the final application satisfy PB?
  - They are ALO-instantiated (`λp.f(clr(p))` code) and copied only by `rep`'s ordinary R copies, whose bodies contain
    no R-label SUP literals. So the may-leak bit should stay clear `[INFERENCE]`.
  - Their binder slots are written by the R copies' DUP-LAM. PB must therefore be stated for the R-COPY cells (each
    unwritten until applied), not for the original cell.
- **t0:** generic (A-T0), not a `%` result.
- No target E status or fusion result changes.

## 9. Falsifiers (paper or approved-run; none run)
- **F1:** an E-valid program with EJ ≠ C1 without replay. Refutes O-SKIP / O-UC / O-MAP / PB / GK′.
- **F2 (`%`-enabling):** proof that SC ∧ PB ∧ GK alone (without E) imply sibling non-observability. Then EJ is generic.
  Conversely, a separation witness (§4) supports the `%` claim.
- **F3:** a target whose continuation consumptions fail PB or SC, or trigger replay.
- **F4:** a measured target recurrence that grows with N.
- **Corpus:** the future-corpus manifest `a00452c7` (5365 plus `labels.percent.*`) and the §4 challenge row are
  mandatory for any separately approved test.

## 10. Map of C41F's required revisions
1. **C-DEAD separated from O-SKIP:** sections 0 and 3. The added checked property is PB with lazy layer replay.
2. **Witness reclassified E-UNKNOWN:** section 4. It now fails PB and is a challenge row; the separation-witness
   question is opened.
3. **GK′ defined relative to omitted C1 births:** section 3. The strict-materialization row is corrected in
   section 5.
4. **Reference / world / resource relation:** section 2, with event-precise COPY-SPLIT, O-MAP and UC over C1 worlds of
   C(S).
5. **Replay finite-prefix budget and output buffering:** section 6. The confinement lower bound (sections 0 and 8) and
   the `< 50k iff coverage` claim are removed.

**Not claimed:** soundness, an E-dependent asymptotic advantage, fusion, a no-fusion result, or any E status.

**Decisive next step (paper):** settle bridge B (§4.1) with Astra. It decides whether this route can be `%`-enabling
at all.
