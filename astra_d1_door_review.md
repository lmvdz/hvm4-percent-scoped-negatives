# D1: Astra review and per-program paper sign-off

**Decision:** all 31 exact door witnesses are **E-valid by finite paper proof under v5 source-use attribution**. None is classified by output agreement alone. This is not an executed E checker, a general HVM transport theorem, or a classification of the five targets.

The individual sign-offs, full pct/C1 hashes, case flags and proof-family references are in `astra_d1_door_signoff.json`. They cover exactly the 31 witnesses in the original ledger `af386a12b5e0a543c284ae631df34ce1dd4400a06340c0192e104a59eff57d1a`; there are no additional programs. All 62 current source hashes match that ledger, and every C1 file is the exact lexical `%` → `! &` replacement of its pct file. No native/model run, build, solver, new program or historical-certificate edit was performed.

Reviewed SNOW paper: `snow_d1_door_classification.md`, revision `d381354a`, including its finite branch-isolation repair. The earlier A8CE argument left trigger attribution unresolved; the revised argument supplies the missing per-value invariant. The sign-off below uses that invariant, not a blanket rule about all cached copies.

## 1. Reference, resources and labels

Reference H is reproduced upstream `6defdfc`, source SHA256 `3d2724d0716b5d6b1c07a3b0b3c5cb89f848487a43d364ea689658f9aeb75fe7`, executable `ea6cb779f7a529e4ad2c797d702338affc3edb0dcdd5dba519f07600a2ad56da`. Source: `astra_evidence/reference_repro_6defdfc_gcc_o2/src/hvm.c`.

Each exact source has one top-level `% v` activation and two source occurrences, v0 and v1. Neither its enclosing closure nor a closure capturing its aliases is ordinarily copied. In the selector cases, APP frames consume both arguments of `@T` before an outer copier can act on the result; a partially applied selector is not duplicated. In lambda-value cases, the source alias is applied before the top copier sees a value. Other copied values are SUPs, constructors or their fields. The replacement K copier does not fork resource identity. Thus both occurrences belong to the same resource `(activation, empty history)`.

E counts distinct source occurrences, not duplicated data nodes. The two fields of a Pair copied from one alias remain repeated use of that occurrence. No resource split is inferred from numeric-label equality.

The exact labels are K = 8388608, R = 44, S = 45, B = 28, `F___` = K, and `F__a` = K+1. The closed `@T/@F` definitions consume no earlier automatic label. In particular S differs from every payload label and every top-level ordinary-copier label in these 31 sources. The `.same_label` top copier is K, not S.

## 2. Finite contribution proof

### D: DEAD and TOP_DEAD — 13 programs

`@T(A(v0), B(v1))` drops the second argument through an erased APP-LAM before demanding it. Any top copier acts only after this selection. Therefore v1 has no own demand, and v5 excludes its contribution in every result world. The remaining results, including both outputs of a top data copier, can involve at most v0. This proof does not assume that the discarded sibling's generated components are inert: source-use attribution is precisely the necessary occurrence distinction.

### I: the seven closed payload forms

For the LIVE cases, outer-S syntax alone is not enough. The following finite invariant covers the shared fan cell, generated copier cells, the original lambda binder and the payload SUP storage. Let q0 = `#Left{}` and q1 = `#Right{}`; A0/A1 are the actual nullary `#First{}`/`#Second{}` arguments.

| Payload | Side-i observable result | Why the other side's application cannot influence it |
|---|---|---|
| `lambda x.x` | Ai after application | DUP-LAM_K writes the original binder to SUP_K(x0,x1). Its body copier selects/caches the pointer xi, never the other binder's contents. Only application i writes xi. |
| `lambda x.SUP_R(x,Other)` | SUP_R(Ai,Other) | K/R commute retains a K projection on x. That child annihilates the original binder SUP to xi; Other is closed. The ordinary R copier acts on the application result, not on this lambda. |
| ERA lambda returning SUP_K(q0,q1) | qi | The body K copier annihilates the public K-SUP. The erased argument produces no binder write. |
| ERA lambda returning SUP_(K+1)(q0,q1) | SUP_(K+1)(q0,q1) | K commutes with K+1 over closed nullary payloads; application writes nothing. |
| Box(SUP_K(q0,q1)) | Box(qi) when its field is read | DUP-NOD creates a lazy field K copier. That copier selects qi when forced, in either demand order. No application state exists. |
| SUP_R(q0,q1) | SUP_R(q0,q1) | K/R commute makes only closed nullary child copies. A top R may annihilate this R-SUP, but both selected components still come from the same source occurrence. |
| SUP_B(SUP_K(q0,q1),Last) | SUP_B(qi,Last) | K/B commute retains an inner K projection; forcing it selects qi, while Last is closed. |

These are read-observable templates, not an authorization to normalize lazy fields eagerly. In the Box case an outer copier first installs another field copier around the inner K door. **Only when that derived copier fires** must it force the inner door before copying a WHNF. Likewise, the nested B/K case preserves the inner projection through an outer commute. An outer ordinary K therefore does not obtain the raw internal K-SUP before the inner selected door acts.

For the two used-binder lambda forms, the shared body/child cache contains a selected binder pointer, not a copy of the other caller's substituted argument. No outside source pointer retains the original binder. For the ERA lambda forms, the erased flag is a property of the source lambda and survives copying. For constructor/SUP forms, all leaves are closed and no binder write exists. The argument holds whether a half is returned by the first firing or obtained from its sibling cache; only allocation/cache-preparation timing differs. It does not assign every generated cache value to the first physical demander.

### L: LIVE, LIVE_CORRELATED and TOP_LIVE — 18 programs

Using I, side S1 reads no side-S0 argument or application-specific write, and symmetrically for S0. Shared cells supply fixed projections of the closed payload, independent of the other source use. World existence and multiplicity in each branch are also fixed by those payload labels and projections; there is no external retained-binder route like the bridge-B challenge.

The outer S survives the K/R/B/K+1 interactions. TOP_LIVE's ordinary L in {R,K} commutes over S, giving two correlated S outputs. CNF's S-labelled copies select the same S side in both Pair fields. LIVE_CORRELATED's second S literal similarly selects A with v0 or B with v1. An R-SUP inside a payload may instead be annihilated by a top R copier: this can put Left and Right in one Pair, but both still derive from the SAME occurrence selected by S. No proof assumes that every syntactic SUP independently chooses a world side.

Thus a reference world with outer choice S=i has contributing-occurrence set contained in `{vi}`. Subsequent R/B/K+1 worlds and identical printed results do not combine the two source occurrences. This proves E for the 18 exact LIVE sources. It is a fixture-specific isolation proof, not an additional v5 attribution axiom or a general resource-transport result.

Native-rule anchors: H APP-LAM 3732–3742; DUP-LAM 3882–3910; DUP-SUP 3927–3938; DUP-NOD 3949–3969; CNF child normalization/SUP lifting 5855–5905; collapse worklist 6158–6236. SNOW's recorded-output comparison is a separate world-output anchor, not the E proof.

## 3. Per-row disposition and ledger scope

Every row in `astra_d1_door_signoff.json` is signed by Astra against its exact source identity:

- DEAD/TOP_DEAD: proof D, with the source-specific closed payload checked.
- LIVE/LIVE_CORRELATED/TOP_LIVE: proof I for its payload plus L for its wrapper.
- **31 paper E-valid; 0 proved E-invalid; 0 UNKNOWN.** No claim is made about source variants, larger input families, or new programs.

The original export contains 118 semantic clauses, each with exactly one of these witnesses. Consequently all 118 acquire promise-domain support once these sign-offs are attached to the ledger. The existing proof uses 104 semantic clauses and the separate three performance clauses. Performance remains supported by the exact mandatory bounty gate, not by E certification.

This is an admissibility update to the **existing** proof, not a fresh solver result. The accepted audit `astra_b8_unsat_audit.json` records a 371-node elimination proof and its previous replay, without blocked-table assumptions and with runtime-valid actions allowed at unreachable cells 8/9. Its source-correspondence, deterministic/well-defined-run and unused-table-entry extrapolation assumptions remain unchanged. No re-check, solver invocation, core minimization, or claim of a minimal core is authorized or performed by D1.

The scoped consequence is: under those inherited assumptions, the recorded fixed backend/table family has no table that is C1-exact on these E-valid witnesses and meets the exact bounty objective. This is not a general insufficiency result for the stated promise.

## 4. Action-language expressivity: correction to the broad inference

The dispatch is **not memoryless**, and the family does not categorically lack copy history. K keeps C1 graph/cache state. Dispatch reads origin/erasure metadata and nearest ordinary-DP stack context; M/S allocate persistent copier structure; C consults an address-keyed instance-label memo. These are stateful effects.

The inspected working-tree source has SHA256 `a54eb1de4da488ecc9c05d0597899e2ae92ece5f75ed591fa94b22f5bdc2bf03`, not the candidate's source pin. Its key at 7811–7835 has five value classes times ordinary-copier-presence times opposite-door-dead, with a fixed unknown→K override. Its actions at 7974–8021 are:

| Action | Existing operation |
|---|---|
| K | C1 firing, preserving native copy/cache state |
| C | C1 firing relabelled through `exc_instance_label(loc)` |
| T | C1 firing relabelled with the enclosing ordinary copier's label |
| W | Return the value and cache ERA for the other half |
| R | Return the value and cache that same value for the other half |
| M | SUP split with persistent origin-marked child copiers |
| S | Wrap using the enclosing copier's label and persistent origin-marked structure |

The current C helper at 326–332 is an address-keyed open-addressed memo with a counter; table saturation returns an unmemoized counter label. This is not a proof of per-activation or per-copy-event identity, and not the cancelled C1^kappa experiment.

Candidate `hvm_search8` is pinned by binary SHA256 `041404f14b40987844984aba3aa8a029be9714261916e75f146da8f777f918ae`, flags `HVM_MOVR_INHERIT=1`, and the 20 exported cell domains. No source-hash reproduction record for that candidate was established here. Applying the inspected source description to it retains the historical audit's source-correspondence assumption; current line numbers do not repair that provenance gap. The reference `hvm_base` has its separate exact reproduction record.

Any SAT/UNSAT consequence concerns only selections among this backend's fixed primitives, domains, overrides and flags. It does not quantify over new primitive implementations, new record protocols or arbitrary retained-history/deferred mechanisms. Conversely, a valid exclusion DOES apply to history-preserving behavior already expressible by this table family. Neither a blanket inexpressibility theorem nor a theorem that all history-retaining mechanisms remain outside the family is established. D2 remains unapproved.

## 5. Immutable historical inputs

- `astra_b8_unsat_audit.json`: `f479cfab2fc010f804ad9472fd6e13dd2851f264a2d2ba30a8abfad883b8bb3a`.
- `snow_b8_unsat_constraints.json`: `4ed2ff4d3c5bd63316bf1846bc22e1d483d693733f52e63b230018651515900e`.
- `astra_door_manifest.json`: `154ea47c0e072bf255e68dc6650407e00ea8245b678d375c182a926021298ce3`.

These are provenance pins, not outputs of a new proof run. The old certificate must remain byte-identical when the separate witness ledger is updated.
