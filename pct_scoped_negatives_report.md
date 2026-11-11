# Scoped negative results about the stated `%` promise

For Lars's decision on whether to send this report to Taelin. It contains the two original failed implications and the subsequent source-use/bridge-B finding, **not a no-fusion theorem**. No native, model, solver or compiler run was made to prepare this report; existing evidence was read and the new corpus files were reviewed statically. The bridge-B finding depends explicitly on Lars's later attribution ruling.

## 1. Contract and reference used

Taelin's [December 30 statement](https://discord.com/channels/912426566838013994/915345481675186197/1455530019890659399) is: “only one of the 3 x's is reachable within the same label universe (that's the contract the user makes).” We use **Lars's authorized v4 reading plus his v5 source-use attribution clarification**, recorded in [percent_contract_criteria.md](percent_contract_criteria.md), not a claim that Taelin supplied every formal detail below:

- A universe is one world of the reference's full collapsed output, with its label correlation. Identical printed worlds retain their multiplicity.
- Reachability means semantic contribution to that result, not merely a physical evaluator read. Retained binder writes and changes to world existence/multiplicity can contribute.
- **Source-use attribution, v5:** an occurrence contributes only via its own demand. Effects created by copying that serves another occurrence's demand are not attributed to it. This does not discard retained effects of the demanded occurrence or equate contribution with physical read counts.
- A resource is a dynamic `%` activation **following copies of its enclosing/capturing closure**. Its own replacement copier cannot manufacture separate resource identities for its aliases. Distinct source occurrences are counted; repeated use of one occurrence is not automatically a second occurrence.
- Soundness is required on **all promise-keeping programs**, including superposed scrutinees. There is no added promise that public labels cannot coincide with parser-assigned labels, that labels are fresh per activation, or that closure copies never recombine.

Write `C(a, pi, u, o)` for contribution of occurrence `o` from activation `a`, with complete enclosing-copy history `pi`, to world `u`. Then:

```text
E(P): for every a, pi, u,  |{o : C(a, pi, u, o)}| <= 1.
```

Here `pi` identifies the actual copy at the contributing occurrence, not every prefix of its history and not a numeric-label/side heuristic. A general native transport construction for this identity is still open; the fixed witnesses below have explicit finite histories.

The reference is unmodified HVM4 `6defdfc`, `src/hvm.c` SHA256 `3d2724d0716b5d6b1c07a3b0b3c5cb89f848487a43d364ea689658f9aeb75fe7`. A retained `gcc -O2` reproduction is byte-identical to `hvm_base`, SHA256 `ea6cb779f7a529e4ad2c797d702338affc3edb0dcdd5dba519f07600a2ad56da`. This reference does **not** parse `%`: C1 inputs use the exact lexical replacement `%` -> `! &`. The reproduction establishes a recipe, not the historical command originally used to build the binary.

## 2. Negative A: E does not imply copy-insensitive exclusivity

### Exact witnesses and derivation

The existing executable-source fixture for the minimal [issue #18](https://github.com/HigherOrderCO/HVM4/issues/18) example is:

```text
@id = λa.a
@fst = λa.λb.a
@snd = λa.λb.b
@make = λss.λf.% s = ss; f(s,s)
@main = ! &x = @make(@id); !a = x(@fst); !b = x(@snd); a(b)(#Token{})
```

File: [astra_cases/falsifier.issue18.minimal.pct.hvm](astra_cases/falsifier.issue18.minimal.pct.hvm). The final `#Token{}` application is the fixed observer of the identity result. The second issue example, with applied branches (`make_B`), is separately fixtured as:

```text
@id = λa.a
@fst = λa.λb.a
@snd = λa.λb.b
@make = λss.λa.λb.% s = ss; λf.f(s(a),s(b))
@main = ! &x = @make(@id,@fst,@snd); !f = x(@fst); !s = x(@snd); f(s,@id)(#Left{},#Right{})
```

File: [astra_cases/falsifier.issue18.applied_branches.pct.hvm](astra_cases/falsifier.issue18.applied_branches.pct.hvm). Its fixed observer returns `#Right{}`.

Taelin's derivation makes the relevant recombination explicit. Its initial term is:

```text
% G = λy.y;
! F &L = λx.x(G,G)
F₀(λa.λb.a)(F₁(λc.λd.d))
```

It reduces to `H₀(I₁)`: the first alias from closure copy 0 is applied to the second alias from closure copy 1. This is **one final reference world**, not two worlds separated by their historic visits to L0/L1. Under v4, each resource copy has one contributing alias, so E holds. Across both copies of the original activation, two alias instances contribute.

The issue derivation is dated January 3, 2026, 13:10Z; the [January 4 Discord repost](https://discord.com/channels/912426566838013994/915345481675186197/1457331764862124074) is the same derivation. The verbatim appendix in the criteria file preserves its apparent intermediate index/rule-heading errors; the left branch's intermediate `I₁` must be `I₀`. The conclusion does not rely on that typo.

Define the stronger copy-insensitive premise:

```text
Phi_ci(P): for every a, u, |{(pi,o) : C(a, pi, u, o)}| <= 1.
```

These fixed examples satisfy E and falsify Phi_ci. Therefore **E does not imply Phi_ci**. In particular, the fact that each closure copy selects one alias does not license treating all copies of the original activation as one exclusive-use resource.

### Evidence and missing guarantee

**Proved, with the stated fixed-source bridge:** the quantifier non-implication above. The missing guarantee is exclusivity across the distinct resource copies that can recombine in a final world. That guarantee is stronger than the authorized per-copy promise.

**Executed previously:** the restricted annotated affine-beta certificate in [astra_pct_fixed_certificate.py](astra_pct_fixed_certificate.py), retained in [astra_pct_fixed_certificate_results.json](astra_pct_fixed_certificate_results.json), classifies the minimal, make_B and January-4 initial terms as per-copy valid and per-activation invalid. It normalizes the selectors rather than being supplied the selected alias set. Same-copy Pair and self-certifying-replacement controls distinguish the intended identity rule. [astra_pct_copy_insensitive_checks.json](astra_pct_copy_insensitive_checks.json) records `E=true`, `Phi_ci=false`, and fixed-position beta checks showing that changing either of the minimal witness's surviving identity functions changes its observer result.

**Scope of that execution:** a restricted finite source/closure-copy certificate, not a general native HVM provenance checker. The fixed-position perturbations are dependency checks, not a general definition of contribution. Preparing this report did not rerun the certificate or execute a new MOV implementation. The detailed source/rule argument is [astra_pct_copy_insensitive_obstruction.md](astra_pct_copy_insensitive_obstruction.md).

**Limit:** Phi_ci is not proved necessary for every fusing mechanism. This result refutes the copy-insensitive exclusivity inference used to justify MOV-style sharing; it does not refute retaining per-copy substitution/history state, immutable-code sharing, or deferred decisions. Lars's separate lead about per-copy resources is not itself falsified by naming this stronger predicate Phi_ci. No physical-copy or interaction lower bound follows.

## 3. Negative B: E does not license universal `%`-label freshening

### Exact witness

The 5365 paper witness is now fixtured, without execution, as `contract.freshening.public_auto_label`:

```text
@main =
  % x = &(8388608){#Left{}, #Right{}};
  (λa.λb.a)(x, x)
```

Files are under [snow_future_corpus/astra_cases/](snow_future_corpus/astra_cases/); the C1 file differs only by replacing `%` with `! &`. There are **no preceding definitions or auto-dup sites**. The parser's first auto label is `K = 0x800000 = 8388608`; the two occurrences of x create one K copier, with the first occurrence its side 0. The public dynamic SUP has that same numeric K.

Define C1^kappa here precisely: only the replacement copier(s) of each `%` activation receive fresh labels, descendants inherit them, and the public SUP and every ordinary/source label remain unchanged. For this one-copier program the fresh label is `kappa != K`. This is not a consistent alpha-renaming of every correlated use of K.

### Finite scalar derivation, not an execution result

The selector returns its first argument. Its second argument is erased without demanding x's second output. The payloads are nullary constructors, so that unused argument creates no retained lambda-binder effect.

| Semantics | Demanded copier/SUP step | Paper-derived full collapse multiset |
|---|---|---|
| C1 | `DP0_K(SUP_K(Left,Right))` annihilates | `{#Left{}: 1}` |
| C1^kappa | `DP0_kappa(SUP_K(Left,Right))` commutes; constructor copies reduce | `{#Left{}: 1, #Right{}: 1}` |

Both paths terminate by these finite scalar steps. No native interaction count or measured termination result is claimed for this fixture.

**E-valid under v4:** there is one activation, no enclosing closure-copy fork, and one C1 result world. Only the first source occurrence contributes. The second occurrence is not entered, and its unused cached constructor cannot affect that world. This reasoning keeps the original two-use compiled copier intact: it does not delete the second occurrence and recompile to a one-use source.

The source/parser and rule derivation uses pinned H: initial auto label at line 226; use ordering at 2001-2041; cloned-let auto-dup construction at 2043-2090 and 2601-2661; public dynamic SUP parsing at 3068-3109 and DSU-NUM at 4152-4155. The detailed argument is [astra_pct_freshening_obstruction.md](astra_pct_freshening_obstruction.md).

### Evidence and missing guarantee

**Proved on paper against the pinned source/rules:** this E-valid witness has different full collapse multisets under C1 and the specified unconditional freshening. Thus universal `E(P) => C1(P) = C1^kappa(P)` is false under v4.

**Not executed:** the new fixture, its E classification and the two multisets are paper-derived, not an executed certificate or a T1 differential. The corpus correctly leaves `expected_multiset` unset and stores those outcomes only as paper notes.

The missing guarantee is that changing the replacement label cannot change an observable equality/correlation with other labels. E restricts contributing occurrences, not that label equality. Public K supplies a direct counterexample. Absence of this particular public SUP alone is not established as a sufficient invariant for freshening in arbitrary recursive programs.

**Limit:** this does not refute representing a copier without its physical C1 node while retaining K's semantics; nor does it refute a checked invariant with exact fallback. A rule preserving public-label correlation is not the transformation disproved here. A ban on public collisions, fresh-label semantics, or recursion-level exclusivity would be additional assumptions/reference changes, not consequences silently available from E. No failure on any of the five targets is inferred.

## 4. What a remaining positive route must preserve

The scoped findings do not settle fusion. A proposed rule may retain history and substitution state, check a sufficient invariant, or defer a decision, with its full work charged. It must identify a step justified by E that a generic K-aware copy repair does not already justify.

Returned-value erasure is not a substitute for this argument. Existing **native** [handler-effect controls](astra_pct_handler_effect_controls.md) show:

- A discarded APP-LAM result can still write a binder slot observed in a retained result.
- Merely exposing and discarding one DUP-LAM output, without applying it, can change a retained result from one world to two identical worlds via the original binder-SUP write.

Those observations use the reproduced upstream reference, not the Words implementation. They require preserving effects and world multiplicity, not just the printed value of a selected alias. They do not classify t0..t4 or establish a general copying lower bound. Superposed scrutinees, demand/termination and the full collapse multiset remain part of the required soundness domain.

### Bridge B: source-use exclusivity does not erase a retained copying effect

**Attribution ruling and evidence tier.** Lars has now explicitly chosen source-use attribution: an occurrence contributes only via its own demand; copying effects serving another occurrence's demand are not attributed to it. Astra signs off the following existing challenge as **E-valid by paper derivation under that ruling**, not an executed certificate. The full source/rule argument and fixed-control check are in [criteria §(f)](percent_contract_criteria.md#f-bridge-b-joint-paper-settlement-and-v5-classification).

```text
@main =
  ! &F{f,g} = λx.&F{x,#Other{}};
  ! &F{a,b} = f(#First{});
  % h = g;
  #Pair{h(#Second{}), (λu.b)(h)}
```

Call the two source occurrences h0 and h1, and the C1 replacement label K, distinct from F. There is one h resource, with no enclosing copy of its activation. K's own replacement does not split that resource.

CNF visits the first Pair field first. h0's demand copies g, writing g's **original binder** `x1 := SUP_K(y0,y1)`; h0's application writes `y0 := #Second{}` and returns `#Other{}`. The runtime lambda retains its non-erasing binder flag even though its selected body becomes constant. The second field erases its h1 argument without demanding it, then obtains b through the ordinary F copies. b retains x1 and therefore exposes the K-SUP. Its y1 component is a free variable: h1's cached lambda is never applied or entered.

| Paper semantics | Full result multiset, free variable alpha-normalized |
|---|---|
| C1 | `#Pair{#Other{},#Second{}}` once; `#Pair{#Other{},a}` once |
| Direct MOVE omitting the K binder-SUP write | `#Pair{#Other{},#Second{}}` once |

The retained binder and world multiplicity are accounted for, not ignored. Under the source-use ruling, however, the generated y1 component is **not h1's contribution**: its copying interaction served h0's demand, and h1 has none of its own. In each reference world at most h0 contributes, so E holds.

**The missing guarantee:** no contribution by a sibling SOURCE occurrence does not imply no observable effect in a GENERATED sibling component. Bridge B would credit that retained component to h1 despite h1's erasure. B is outside the stated contract; it is recorded as a **contract-strengthening candidate, deferred**, and EJ-MOV is stopped under outcome (ii).

This does not contradict issue #18, its `make_B` example, January 4, or 5365. Their accepted resource/world classifications are unchanged. The existing APP/DUP-LAM handler controls still credit retained writes/world effects to the demanded occurrence; they do not require crediting a distinct, erased `%` occurrence. The capture-copy/data-copy controls also retain their classifications.

**Limits.** The challenge and both multisets above are paper-derived from the pinned native rules, not new executed observations. Before the attribution ruling its E status was UNKNOWN; the earlier schema-level ambiguity was not itself a semantic counterexample. Neither a delivered-value perturbation nor the restricted affine annotation rules supplied a general contribution definition. The finding refutes this particular omitted-write inference, not all E-enabled mechanisms, not a physical-copy lower bound, and not every fast path retaining or replaying the write. PB is not proved universally necessary. The remaining obligations include resource mapping, checked invariants, deferred-work accounting, public-label preservation and termination.

## 5. Related evidence that must not be promoted into a general negative

### Backend-8: the initial admissibility gap is closed by D1, within the fixed language

The historical backend-8 UNSAT result remains a result about its tested action language and original full-corpus constraints. It is not a theorem over all `%` mechanisms. Ruling B additionally requires semantic witnesses in the promise domain or an independently applicable exact gate/proof.

The initial witness ledger (`af386a12...`, preserved as `snow_b8_witness_ledger_v1.json`) exported the **full pool**, 118 semantic clauses plus 3 separate performance clauses, not a minimal core. Its semantic witnesses were 31 exact door programs, initially all E-UNKNOWN. The old proof uses 104 semantic clauses and all 3 performance clauses. That initial lack of support did not establish E-invalidity or falsity of any clause, and no reduced-set SAT/UNSAT claim followed from it.

**D1 update:** Astra has now signed all 31 exact sources **E-valid by finite paper proof under v5**: [per-program source-pinned sign-offs](astra_d1_door_signoff.json), SHA256 `7028168684a15d232d1c87b230ab486578687cc539e4a0db0f99b382a2c7f998`, and [review/proof](astra_d1_door_review.md), SHA256 `cd4dd6dc016ead8c0970156113785de813ac7c0a5c0cc26bf3069eb1e925973c`. Thirteen erased-second-argument cases follow directly from source-use; eighteen LIVE cases additionally use a finite per-value isolation proof, not merely outer-S syntax or physical trigger attribution. All 62 source hashes and all 31 lexical C1 mappings were checked. This is paper E certification, not a new native/model execution.

The [updated ledger](snow_b8_witness_ledger.json), SHA256 `d0cfc3729b2d0b4090f3e9d58adbda399bef061c09adf6f7d972563c56fe3727`, therefore supports **118/118 semantic clauses**, including **104/104** used by the existing proof. The three exact-bounty performance clauses remain separate, not E evidence. An independent metadata comparison found all clause literals, witness identities, proof-use flags, performance rows and the runtime fingerprint unchanged; the historical proof, export and manifest remain byte-identical. No solver, proof replay or core minimization was run for D1.

Under the inherited runtime/source-correspondence and trace-extrapolation assumptions, the old proof now excludes a C1-exact, sub-50k solution **within that fixed backend/table family** on these promise-valid witnesses and the mandatory bounty. It does not establish general insufficiency of E. The family is **stateful**: K retains C1 copies/cache state; C uses an instance-label memo; dispatch reads origin/erasure/stack context; M/S construct persistent copier structure. Calling it “memoryless” or categorically unable to retain history would be wrong. The exclusion covers whatever history-preserving behavior is expressible by its fixed primitives, but does not quantify over new primitive implementations, arbitrary provenance/deferred protocols, other key spaces or runtimes. The inspected working tree is not a source-hash reproduction of the pinned backend-8 binary; that historical source-correspondence assumption is not discharged by D1.

The subsequent approved [recorded-results-only query](snow_b8_gate_query.md) found 41 fully classified table/configuration keys: all five exact suite outputs match, but every exact bounty result has at least 50,000 interactions. Zero qualify. Eight earlier-stopped rows have unrecorded gates. This excludes **no unrecorded or partially recorded table/configuration**, and provides no new E evidence or general impossibility result.

### Words: an executed generic compression data point, not a `%` result

The closed macro4 track recorded:

| Exact bounty configuration | Interactions |
|---|---:|
| macro4 scalar control, Words off | 97,890 |
| macro4 COMMUTE+NOD word macros | 52,058 |

The complete readback multiset matched, and the two-kind accounting identity passed. The final selector-cache closure also completed all five formerly timed-out cases, without changing the guard caps. Records: [checker summary](snow_evidence/words_macro4_r32_checker/summary.json), [timeout-closure summary](snow_evidence/words_macro4_r32_rerun/summary.json), and `../rule_search_results.json: words_closure_release32`. Binary SHA256 starts `7a1032c8`; the records retain its full identity and raw-run links.

This is **generic runtime copy-word compression, not a `%` result, and does not satisfy the bounty contract**: it neither uses E as enabling information nor stays within the required `%`-enabled change scope; it also remains above the numerical threshold. It is not a speed claim. The earlier approximately 37.8k figure was a counter-model projection, not a measured result. Words work is stopped.

## 6. Current disposition and reviewed future corpus

T1 is cancelled. Before cancellation, one compiler-only build had completed under prior approval; binary `8e0ab73c...` has **never been executed**. Its build record is preserved in `snow_t1_kappa/build_record.json`, and [the spec](snow_t1_kappa_spec.md) now marks all experiment gates superseded. There is no T1 differential result to report. VMOV is not approved for implementation.

SNOW's existing [future-corpus supplement](snow_future_corpus/manifest.json), SHA256 `a00452c7c786df72ffabdd26b78f3c7b047f7364274eb69b00f60c700fa53502`, is **accepted after static review**. No duplicate fixture was created. The review verified all ten source hashes, the exact 5365 source and lexical-C1 bytes, and the unchanged paths/configuration/provenance of:

- `labels.percent.first_auto`
- `labels.percent.dynamic_auto`
- `labels.percent.global_exc`
- `labels.percent.fresh_candidate`

The supplement is required for future corpora. The new 5365 row is **E-valid by paper derivation, not an executed certificate**; the four prior label cases remain UNKNOWN unless separately certified. Historical corpora/evidence were not rewritten, and including these files authorizes no run.

The five target E classifications remain UNKNOWN while the source/reference and resource-transport obligations are open. The [EJ-MOV positive-route proposal](snow_positive_route_proposal.md) is **stopped under Lars's bridge-B outcome (ii)**. Bridge B is a deferred contract-strengthening candidate, not an assumption available to that design under the stated contract. No EJ-MOV implementation or run is approved. Astra may continue the t0 bridge; the general retained-history/checked-invariant fusion question remains open.

**Confinement qualification:** any claimed asymptotic E-advantage of EJ-MOV existed only relative to Lars's confinement ruling: `%` machinery plus one fully costed, semantics-neutral certificate bit at generic stack push, active only when `%` is present. An unconfined generic alternative using snapshots and binder-escape tracking plausibly recovers essentially all of that proposed gain. This is a paper estimate, not a demonstrated E-advantage or measured speedup. It neither establishes a generic implementation nor turns the scoped findings into a no-fusion theorem.
