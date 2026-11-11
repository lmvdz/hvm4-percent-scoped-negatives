# % contract criteria — v5, Lars-authorized source-use attribution

Status: **v3 framework accepted; v4 records Lars's A/B rulings; v5 records his subsequent source-use attribution ruling.**
The predicate/checker work is authorized under the default reading below.
Alternative readings are comparison cases, not blockers. First classify issue
#18, the January-4 derivation, and the five targets; then develop the argument.

## Scope and fixed primary sources

The primary question is Taelin's stated promise, not a strengthened promise.
Generic copy-word compression is a separate closing data point, not a `%` result.

- [December 30 promise](https://discord.com/channels/912426566838013994/915345481675186197/1455530019890659399):
  “only one of the 3 x's is reachable within the same label universe
  (that's the contract the user makes)”.
- [Scott-branch explanation](https://discord.com/channels/912426566838013994/915345481675186197/1455532025980391550)
  and [identification as the user's promise](https://discord.com/channels/912426566838013994/915345481675186197/1455532069722525808).
- [Superposed scrutinees must work](https://discord.com/channels/912426566838013994/915345481675186197/1453425196483608606).
- [Issue #18](https://github.com/HigherOrderCO/HVM4/issues/18): both the
  `make_B` example and the minimal example are fixed gates. Taelin's issue
  derivation is dated **2026-01-03T13:10Z**; he explicitly accepts the initial
  input as following the demanded format.
- [January 4 Discord repost](https://discord.com/channels/912426566838013994/915345481675186197/1457331764862124074)
  is located and transcribed in the appendix. It is not a different test.

The pinned C1 executable `hvm_base` (`ea6cb779...`) is now byte-reproduced from
unmodified upstream `6defdfc:src/hvm.c` (`3d2724d0...`) with GCC 13.3.0,
`gcc -O2 -o src/hvm src/hvm.c`; exact `cmp` succeeds. Record and source:
`astra_evidence/reference_repro_6defdfc_gcc_o2/record.json`. This executable
does not parse promised `%` bindings: reference sources use the lexical
replacement `! &`. The record establishes a source/binary correspondence,
not evaluator soundness, ownership, resource transport, or the original
historical build command. No reference executable was replaced.

## (a) Authorized default reading

    E(P) := for every promised resource b and collapse world u,
            |{o in O_b : Contributes(P,b,u,o)}| <= 1.

Here O_b is the set of distinct promised alias occurrences belonging to b.
The following meanings are Lars's authorized interpretation of the informal
promise, not a claim that the primary quotation already supplies these details:

1. **Reachability is semantic contribution to the world's collapsed result.**
   Merely reading an alias during physical C1 evaluation does not establish
   contribution. Conversely, contribution need not leave an alias-shaped node
   in the final term: an applied function can contribute to the returned result.
2. **A universe is a collapse world**, with the reference's label correlation.
   Identical printed results in two worlds remain two results. Historic visits
   to opposite label sides do not by themselves prove different final worlds.
   Repeated labels, nested projections, binder SUPs, APP-SUP and annihilation
   retain reference behavior; no replacement by fresh labels is authorized.
3. **Resource identity is per dynamic `%` activation and follows copies of the
   enclosing closure.** Each ordinary DUP-LAM copy carries its own resource.
   Captured aliases move with that closure's copy, including the January-4
   example where G is bound outside F. Two aliases captured by the SAME copy
   must still be checked together; assigning each alias a separate resource
   would trivialize the predicate.
4. The C1 replacement DUP for the `%` binding itself cannot manufacture the
   branch separation or independent resource identities that certify its own
   aliases. The ordinary enclosing-closure copy lineage must be distinguished
   from this replacement mechanism.

**Attribution ruling (v5, Lars via DSCRD):** the stated contract uses
**SOURCE-USE attribution**: “an occurrence contributes only via its own demand;
effects created by copying that serves another occurrence's demand are NOT
attributed to it.” This fixes an attribution question that v4's explicit
schema and fixed-case facts had left unresolved. It does not replace semantic
contribution by a physical-read count: a demand must still contribute through
the returned result, retained substitution effects, or world existence/
multiplicity. An erased return can therefore contribute through its writes.

In particular, observing a generated sibling component does not, by itself,
credit an erased source occurrence with another occurrence's copying effect.
The output-component attribution bridge B is **not part of the stated
contract**. Per Lars's decision it is a contract-strengthening candidate,
deferred to the strengthened-promise phase. The compiled copier tree and
reference worlds remain fixed when making this distinction; deleting a
source occurrence and recompiling can change that tree and is a different
operation. This is Lars's explicit clarification, not a claim that Taelin's
original quotation independently resolves the attribution question.

This is per-world, per-copy exclusivity, not global single use. It does not by
itself bound repeated demands of one source alias. Resource/copy identity is
not numeric-label identity, and is not a requirement for fresh physical copies.

**Certificate notation:** a copy history is the complete history carried by
the particular contributing occurrence, not each of its prefixes. Do not pad
it with later forks that occurrence did not traverse. Different occurrences
may carry prefix-related or incomparable histories; their identity transport
must be justified rather than collapsed by numerical-label equality. Repeated
propagation of one logical fork is not a new fork.

**Checker obligations:** resource transport and semantic contribution must be
justified, not inferred from unchanged unannotated output or a read histogram.
A conservative contribution analysis can establish E only with an established
over-approximation property for the SAME resource/world identities. A candidate
violation needs semantic evidence, not merely an over-approximation containing
two aliases. Incomplete reduction, uncertain world alignment, unsupported
transport or failed native-reference comparison yields UNKNOWN. No total
decision procedure for arbitrary programs is assumed.

### Alternative readings to test, not to adopt silently

| Reading | Difference from the authorized default | Required first check |
|---|---|---|
| Per activation, ignoring enclosing copies | Descendants retain the original resource identity | Issue-18 minimal and make_B; January-4 G/F derivation |
| Per source site | Activations and copies are identified | Same gates; then recursive targets |
| Historical opposite-label sides define separation | May separate uses that later recombine in one collapsed world | H0(I1) in the January-4 derivation |
| Every copier forks resource identity | Includes value/data copies and potentially the `%` replacement itself | Circular-certification control and issue #18 |
| Physical reads define reachability | Counts work later erased from the result | Erased-branch/demand control and the fixed gates |
| Output-component attribution (bridge B) | Credits an unentered occurrence with a sibling component generated while serving another occurrence's demand | Outside the stated contract under the v5 ruling; deferred strengthening candidate |

These are sensitivity tests. A reading excluding an author-accepted issue-18
input does not replace Lars's default and does not settle the stated question.

**Ruling A:** formalization work proceeds under the default above. No global
exclusivity, freshness, label-absence condition, recursion-level restriction or
ban on recombination is added. The earlier v1 physical-read/provenance-pair
choices are not authoritative.

Lars's proposed Phi lead is that per-copy resources are what fresh copying
provides and might prevent fusion. This is an **inference to verify**. Logical
independence alone is not a lower bound on physical copying, allocation or
reduction: a necessity argument must address alternative representations and
deferred decisions.

### (a.1) Soundness domain — ruling B
[bounty gist](https://gist.github.com/VictorTaelin/ee5cc9e6828169e3cdbe747e64e365b0)
requires the two insert versions to give the same `-C1` output and the MOV
version to halt below 50,000 interactions. The
[announcement](https://x.com/VictorTaelin/status/2006818916211834900), retrieved
through the [FXTwitter mirror](https://api.fxtwitter.com/status/2006818916211834900)
because direct X reading was unavailable, adds:

> your solution must be correct, in the sense that using either MOV nodes and DUP nodes to pass a value to different branches produces the same output

**Lars's ruling B: promise-keeping programs only.** For every P satisfying the
agreed E(P), MOV must equal DUP on the full collapsed output, including
superposed scrutinees. Behavior on promise-violating programs must be documented;
detecting violations or falling back is optional, not required.
This supersedes the earlier internal “MOV == DUP on all programs” wording.
Source confinement to `%` lines and `%` as enabling information remain binding.

## (b) Information available to a candidate

The stated promise does not impose a graph radius or prohibit provenance,
erasure tracking, separate activation state, deferred decisions, or inspection
of a larger context. Current implementation limitations are not contract axioms.

The default admissible space therefore does NOT have an assumed radius bound.
A candidate must specify:

- Source changes confined to permitted `%` lines and the associated runtime
  mechanism. Its proof must actually use E(P); a generic optimization equally
  justified for ordinary copies is not a `%`-enabling result.
- What current graph/code/closure information it reads; what provenance,
  resource, substitution or erasure state it maintains; and when it decides.
- Any traversal, simulation, copying, replay or deferred work, including its
  cost and its effect on demand/termination. No uncomputed future oracle,
  hidden uncharged exponential work, or forcing an otherwise unused loop.
- The preservation obligations for public-label projections/correlations,
  independently usable consuming state, result multiplicity and residual terms.

**Subsequent Lars Q1/Q2 ruling for the EJ-MOV phase:** the candidate mechanism
is confined to `%` machinery. The sole permitted generic-rule hook is an O(1)
one-bit certificate flag maintained at generic stack push, active only when
`%` is present, fully costed and semantics-neutral. Generic binder-escape or
copy-event instrumentation is not authorized by that exception. Any claimed
asymptotic E-advantage must be explicitly relative to this confinement; the
paper must also estimate what an unconstrained generic snapshot/binder-escape
design could recover. This restriction is a declared model boundary, not a
proof that only the proposed implementations are possible. No build/run is
approved: reviewed paper plus an exact guarded plan must return to Lars.

A bounded-radius class may be studied as a **separately scoped subclass**.
It must specify distance/ports, state size, earlier state-building transitions,
static-code access, deferred decisions and costs. An indistinguishability proof
must cover that entire permitted protocol, not just the first decision snapshot.
Even a result for every fixed radius is not automatically a result for mechanisms
with traversals, growing metadata or deferred decisions. Restricting the primary
question to such a subclass needs Lars's approval before work.

## (c) Settlement evidence

### Positive: sound, promise-enabling fusion

All are required:

1. A complete agreed definition of E(P), an explicit mechanism/invariant, and
   identification of where the promise supplies necessary information.
2. A soundness argument for every program satisfying the agreed E(P):
   observations, label correlations, multiplicity, substitution ownership and
   demand/termination. Issue #18 is a mandatory first gate, not the whole proof.
   Document behavior outside E(P); do not impose mandatory detection/fallback.
3. Complete full-world-multiset differentials, including residual/free-variable
   results, against the fixed reference on the agreed corpus and fixed cases.
   Caps, failures and missing output are UNKNOWN, never successful equality.
4. The exact bounty below 50,000 interactions and fusion of all five canonical
   targets. State the input family and cost bound; measured scaling alone is
   evidence, not an asymptotic theorem. Charge and report metadata/deferred work.
   No source recoding or generic copy compression may be counted as this result.

### Negative: rigorous insufficiency for the stated question

All are required:

1. A complete agreed definition of E(P), plus concrete witnesses proven to
   satisfy it. Executed bounded traces alone do not prove a quantified family.
2. A precise missing guarantee Phi, with a proof that E does not imply Phi.
3. A **necessity/unavoidability argument**: every sound mechanism meeting the
   agreed fusion requirement in the admitted implementation/cost model would
   need Phi, or an equivalent general contradiction/lower bound. It may not
   simply assume one globally consuming cell, immediate wiring, no replay,
   no auxiliary state, or a fixed observation radius.
4. Explicit handling of mechanisms that retain distinctions or defer the
   decision. Any restriction used in the proof must be stated and approved.

**Tiered reporting, explicitly accepted by Lars:** items 1–2 alone are a
reportable intermediate result: “the stated promise does not justify MOV-style
sharing”, with the exact Phi and representation/inference identified. This
does NOT settle the general fusion question. The full necessity/unavoidability
argument remains the negative settlement goal.

The backend-8 finite action-language CEGIS exclusion remains separately scoped.
Its historical requirement was C1 equality on the entire 299-case corpus.
Under ruling B, that is not automatically an exclusion of the same language
on promise-keeping programs. Reusing a semantic nogood for the present
contract requires an E-certified refuting witness, an independently
mandatory output gate, or another proof that the clause holds in the
present domain. E has not been established for every historical witness.
The recorded full-corpus UNSAT result remains intact; it is not silently
promoted to a promise-domain UNSAT result. No new search is authorized by
this qualification.
No strengthened promise is explored until Lars accepts that the stated question
has been settled under these criteria. Any further scope change is raised first.

## (d) First classification batch and ownership

ASTRA owns this criterion, the predicate evidence contract, issue #18 (both
examples), the January-4 derivation and the alternative-reading comparison.
SNOW owns the five canonical target classifications, using the same predicate:
`suite.t0.published_main` through `suite.t4.published_main`, whose `pct_source`
and `c1_source` paths are in `astra_manifest.json`. `bounty.published` is a
separate sixth exact-performance gate, not one of those five.

Report valid/invalid/unknown per concrete input and distinguish a checked input
from a proof for an input family. Start with the predicate/classifications, then
the sharing/fusion argument. Send Lars the first concrete result or blocker.
Any further change of scope is raised with Lars before starting it.

## (e) First fixed-case classification evidence

Executed `astra_pct_fixed_certificate.py`; results are retained in
`astra_pct_fixed_certificate_results.json`. This is a restricted annotated
affine-beta certificate with an explicit ordinary closure-copy expansion,
**not a general HVM interpreter or a five-target preservation theorem**.

Source bridge: unfold `make`, `id`, `fst`, `snd` in the fixed programs. The one
ordinary enclosing copy produces F0 and F1; both aliases captured by F0 receive
the SAME resource version G[copy,0], and both aliases captured by F1 receive
G[copy,1]. No resource fork is attributed to the `%` replacement copier.
The fixed initial values are identity functions. Copying an identity with its
own binder SUP yields identities again; the `%` and enclosing copier labels
are distinct in these fixed sources. The January-4 APP-SUP derivation exposes
the same calls H0(I1). Its first intermediate `I1` in the left branch must be
`I0`; the verbatim quotation below remains unchanged.

The certificate normalizes the actual selectors and applications, rather than
being given the selected alias set. An applied function's annotation follows
its result; ordinary substitution discards unused arguments and annotations.
Its classifications are:

| Fixed program | Authorized per-copy reading | Per activation / per site | Observation |
|---|---|---|---|
| Issue-18 minimal | Valid | Invalid | identity; `#Token{}` after the fixed observer |
| Issue-18 make_B | Valid | Invalid | second selector; `#Right{}` after the fixed observer |
| January-4 initial program | Valid | Invalid | identity |

Each has ONE result world. Its two contributing aliases belong to two resource
copies: the left alias of copy 0 and the right alias of copy 1. Historic L0/L1
visits are not two final worlds. The observed constructor results agree with
the previously recorded fixture expectations; no native reference was rerun.

Negative controls: returning both aliases from the SAME copied closure is
rejected. Giving each alias a fresh identity via its own replacement would
incorrectly accept that control. A separate erased-argument control has one
contributing alias under both lazy and eager affine-beta schedules, although
the eager MODEL reads two. This is not a claim about native HVM's read trace.

The five canonical targets currently remain **UNKNOWN**: their syntax places
one alias in each Scott case argument, but lifting that fact through reference
copying, same-site label reuse and collapse requires the outstanding
preservation/transport obligation R. SNOW's earlier informal “proved-valid”
claim was withdrawn. Local branch syntax and output equality alone do not
discharge R; neither UNKNOWN nor failure of a sufficient certificate means
the target violates E(P).

The scoped intermediate result is in
`astra_pct_copy_insensitive_obstruction.md`, with executed quantifier and
fixed-occurrence beta checks in `astra_pct_copy_insensitive_checks.json`.
It proves `E` does not imply **Phi_ci**, copy-insensitive exclusivity across
the closure copies of one original activation in a final world. Phi_ci is
NOT Lars's separate per-copy-resource/physical-copy lead. No necessity of
Phi_ci for all fusing mechanisms, or lower bound on their costs, is proved.

### Reference-preservation counter-control: late arguments

The proposed confinement lemma K (“no foreign same-label SUP in the copied
value initially implies no later cross-family annihilation”) is false as
stated. A small ordinary-C1 control is:

```text
@id = λa.a
@mk = λz. ! &A{f0,f1} = λx.x(z); f0(@id)
@main = ! &B{g0,g1} = @mk; g1(@id)(g0(&A{#Left{},#Right{}}))
```

The scalar derivation creates the A-family while evaluating `g1(@id)`, with
`z = &B{z0,@id}` and z0 unset. An A copier on z commutes across B and leaves
an A copier on z0 in the stored g0 result. The subsequent g0 argument supplies
the foreign A-SUP; that stored copier projects it. Initial absence was not a
future-stability guarantee.

Executed on pinned `hvm_base` (`ea6cb779…`), flags stripped, `-C64`, 8 s /
500 MB per invocation:

| Final argument label | Complete collapsed output | Interactions |
|---|---|---:|
| A | `#Left{}` | 14 |
| C (distinct-label control) | `#Left{}`, `#Right{}` | 16 |

Raw bytes, hashes and gate records:
`astra_evidence/pct_confinement/sessions/0840b698885b4120ab6404e7dcb5ff13/`.
The native outputs check the late-label distinction; the family/birth argument
is the scalar derivation, not an instrumented family trace. This is a
counterexample to a proposed preservation premise, **not** a `%`-promise
violation or a general no-fusion result.

### Fixed transport and retained-substitution controls

`astra_pct_transport_certificate.py` and its executed results distinguish
captured-alias closure copying from ordinary data copying. Under the v4
capture-copy reading: the erasing-closure copy and its constant-forced-capture
variant are valid; the uncopied closure and `Box(alias)` data-copy controls
are invalid. All four fixed outputs match complete native C1 runs. This is
a fixed affine source/capture-copy certificate, not general HVM transport;
the constant-forcing case does not implement general USE semantics.

`astra_pct_handler_effect_controls.md` records a separate native counter-control:
an application returning discarded `#Other{}` writes a binder slot retained by
another result. The unforced source collapses to `#Pair{#First{},a}`, whereas
the strict ordinary call and strict one-use-% call collapse to
`#Pair{#First{},#Second{}}`. All three outputs are complete, including the free
variable. Therefore “the application's returned value is erased” does not by
itself imply semantic non-contribution. A proposed conservative dependency
analysis must account for substitution effects as well as returned values.
No target E verdict follows from these controls.

## (f) Bridge B: joint paper settlement and v5 classification

**Astra sign-off:** the existing section-4 challenge is **E-valid under Lars's
source-use ruling, by the finite paper derivation below**. This is not an
executed certificate, a general contribution interpreter, or a target
classification. No new fixture, native/model run, build or solver was used.
SNOW's analysis and fixed-control audit are retained in
`snow_bridge_B_analysis.md` and `snow_bridge_B_audit.md`.

### Existing challenge and reference route

```text
@main =
  ! &F{f,g} = λx.&F{x,#Other{}};
  ! &F{a,b} = f(#First{});
  % h = g;
  #Pair{h(#Second{}), (λu.b)(h)}
```

F is the same named label at the three written F sites, distinct from the
parser-assigned replacement label K for `% h`. The two source occurrences
are h0 in the first field and h1 in the erased argument of the second field.
Keep the compiled two-use K fan intact. There is one h activation and no
enclosing copy of that activation; K itself does not fork its resource.

The pinned H source gives the following lazy order, rather than evaluating
`f(#First{})` eagerly:

1. CNF visits the first Pair field first. Demand of h0 forces g, the side-1
   output of the first F fan. DUP-LAM_F writes the original binder
   `x := SUP_F(x0,x1)` and caches f.
2. DUP-LAM_K on g writes `x1 := SUP_K(y0,y1)` and caches h1's lambda.
   Applying h0 writes `y0 := #Second{}`. The first F body fan annihilates
   the literal F-SUP: g's selected body becomes `#Other{}`, while the
   opposite cached body is x. The first field therefore becomes `#Other{}`.
   The copied lambda nodes retain the original non-erasing binder flag;
   they are not reparsed as constant lambdas with erased binders.
3. The second field's erased APP-LAM returns b without substituting,
   demanding, or marking its h1 argument. b then forces cached f, whose
   application writes `x0 := #First{}`. The second F fan projects the
   returned `SUP_F(x0,x1)` to x1.
4. Thus the second field is `SUP_K(#Second{},y1)`. No operation applies
   h1's cached lambda or reads its cache through the h1 source edge.
   Reading VAR(y1) does not execute its unmarked lambda-body cell: y1
   remains a free residual variable. Collapse gives two worlds,
   `Pair(Other,Second)` and `Pair(Other,free y1)`.

Source anchors in the reproduced upstream H: APP-LAM 3732–3742,
DUP-LAM 3882–3910, equal-label DUP-SUP 3927–3930, VAR entry 4740–4749,
CNF child order 5855–5868, and collapse worklist 6164–6181.
These establish the paper route; the similar executed handler controls
do not constitute execution of this challenge.

### Attribution and the precise failure

The retained binder and both worlds are real semantic effects. The h1
source occurrence, its cached output lambda, that lambda's binder y1, and
the observation through b are nevertheless different entities. By the
v5 ruling, the last observation is not attributed to h1 merely because
it uses a component generated on h1's nominal copy-side. The copying
interaction served h0's demand; h1 has no demand of its own.

Consequently the contributing-occurrence set for the one resource is a
subset of `{h0}` in EACH reference world. E holds. B would instead credit
the retained y1 observation to h1. B is therefore false for this fixed
program under the now-authorized source-use attribution.

Directly moving g to h0 while omitting the K DUP-LAM write changes the
reference: application writes `x1 := #Second{}` directly, and b exposes
that value, not a K-SUP. Only `Pair(Other,Second)` remains. Thus absence
of a sibling SOURCE contribution does not imply unobservability of an
effect in that sibling's GENERATED component. This refutes that skipped-
effect inference, not every implementation of `%`.

### Fixed gates, qualifications and disposition

The ruling leaves the accepted fixed cases unchanged:

- Issue-18 minimal/make_B and January 4 still use distinct enclosing-copy
  resources in one result world. Identity copying may create binder SUPs;
  no zero-SUP-birth claim is needed.
- 5365 still has one contributing source occurrence; its opposite cache
  has no retained effect route. Its paper freshening counterexample stands.
- The three APP-handler and two DUP-LAM-effect controls still require
  retained writes and world multiplicity. Where `%` is present it has one
  source use; the DUP-LAM-effect control's two-way copier is ordinary R.
- The four capture/data-copy controls keep their recorded classifications:
  copied capture and forced capture valid; uncopied and data-copy invalid.

Before Lars's clarification, the explicit schema/fixed facts admitted both
attributions on the challenge: `{h0}` in both worlds, or additionally h1 in
the y1 world. That was schema-level non-entailment, not a total HVM
contribution semantics or an E-valid certificate. The present paper E
classification depends explicitly on the subsequent ruling.

Neither delivered-value counterfactuals nor restricted affine annotations
were promoted to a general attribution definition. In particular, replacing
h0's delivered lambda AFTER DUP-LAM cannot undo its already-written SUP;
replacing the source edge BEFORE demand is a different intervention.
Clause (a).4 concerns resource separation and does not itself forbid
contribution attribution through copier effects.

**Outcome (ii):** B is recorded as a contract-strengthening candidate,
deferred; EJ-MOV design is stopped. The finding proves neither universal
necessity of PB nor impossibility of fusion/retained-history/checked-invariant
mechanisms. Accepting B in a future contract would also not, by itself,
prove O-MAP, UC, O-SKIP or termination. No build/run is authorized.

## Appendix: January 4 repost, verbatim code

Source: Discord message 1457331764862124074, 2026-01-04T11:16:08Z.
The code is copied without repairing its apparent intermediate index/rule-heading
errors; a subsequent derivation must distinguish source text from corrections.

```text
% G    = λy.y; 
! F &L = λx. x(G, G)
F₀(λa.λb.a)(F₁(λc.λd.d))
------------------------------------------- DUP-LAM
% G    = λy.y; 
! F &L = &L{x0,x1}(G, G)
(λx0.F₀)(λa.λb.a)((λx1.F₁)(λc.λd.d))
------------------------------------------- APP-SUP
% G    = λy.y; 
! &L H = G
! &L I = G
! F &L = &L{x0(H₀,I₁),x1(H₁,I₁)}
(λx0.F₀)(λa.λb.a)((λx1.F₁)(λc.λd.d))
------------------------------------------- APP-SUP (2x)
% G    = λy.y; 
! H &L = G
! I &L = G
! F &L = &L{(λa.λb.a)(H₀,I₀),(λc.λd.d)(H₁,I₁)}
F₀(F₁)
------------------------------------------- APP-LAM (4x)
% G    = λy.y; 
! H &L = G
! I &L = G
! F &L = &L{H₀,I₁}
F₀(F₁)
-------------------------------------------  DUP-SUP
% G    = λy.y; 
! H &L = G
! I &L = G
H₀(I₁)
```
