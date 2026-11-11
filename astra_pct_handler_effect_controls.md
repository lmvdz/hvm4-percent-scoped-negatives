# Fixed handler-effect controls

## Result and scope

An application with a discarded return value can contribute to the C1 collapsed result through a retained binder slot. Propagating alias dependencies only to the returned body/constructed result misses this route. This is a counterexample to that proposed transport inference, not a general impossibility result for `%` and not a classification of any target.

Pinned reference: `astra-repr/hvm_base`, SHA256 `ea6cb779f7a529e4ad2c797d702338affc3edb0dcdd5dba519f07600a2ad56da`. `%` is lexically replaced by ordinary cloned let `! &` for C1. No HVM flags; `-C64`; 8 seconds / 500 MB per invocation. All three executions exited 0, complete, with no gate reasons. Raw bytes and hashes:

`astra_evidence/pct_substitution/sessions/d1fb4b1097be4ed6851410f55b43f33a/result.json`

Sources and hashes: `astra_pct_substitution_manifest.json`.

| Control | Complete C1 world | Interactions |
|---|---|---:|
| unforced_substitution | `#Pair{#First{},a}` | 5 |
| forced_substitution | `#Pair{#First{},#Second{}}` | 7 |
| percent_forced_substitution | `#Pair{#First{},#Second{}}` | 8 |

The free-variable result `a` is included, not constructor-filtered.

## Fixed source and scalar explanation

```text
@main =
  ! &F{f,g} = λx.&F{x,#Other{}};
  ! &F{a,b} = f(#First{});
  % h = g;
  !! unused = h(#Second{});
  #Pair{a,b}
```

The forced ordinary control omits `% h = g` and applies `g`; the unforced control additionally changes `!! unused` to lazy `! unused`.

Ordinary `DUP-LAM_F` creates distinct output binders `x0,x1` and substitutes `x := SUP_F(x0,x1)`. The body fan meets the literal same-label SUP and annihilates: `f` returns `x`, while `g` returns `#Other{}`. Calling `f(#First{})` writes `x0 := #First{}`. The second F fan projects the returned SUP into `a = #First{}` and `b = x1`. Calling `g(#Second{})` writes `x1 := #Second{}` even though its body returns `#Other{}` and that returned value is discarded. Without the strict call, the retained slot remains free in readback.

This explanation uses the reference's equal-numeric-label rule, not ordinary lambda-world projection or a same-family-annihilation assumption. The source explicitly contains the colliding F label. It is not asserted to occur in t1. The `% h` control has only one source alias, so it cannot violate exclusivity by using two aliases; nevertheless its application has an observable substitution effect.

Upstream implementation of the relevant writes: HVM4 `6defdfc`, `src/hvm.c`, `wnf_app_lam` 3732–3742 and `wnf_dup_lam` 3882–3910. The modified words sources are not needed for this argument.

## Consequence for proposal H

A conservative dependency model must include at least:

- persistent source-occurrence identity, separate from a value's ordinary dependency tags;
- control dependence on a tagged function at the writes its rule performs, not just its returned term;
- dependencies on binder/copier slots transported through every subsequent semantic read, including free-variable and lambda readback;
- separate storage/version treatment when native rules repurpose a location;
- branch/world handling for SUP, projection, collapse and shared substitutions.

These are obligations, not a completed propagation proof. Ordinary pure erasure controls can exclude an unused value's dependency only when no retained substitution/graph effect exists. A selector-only positive control must use observationally distinct branches.

An over-approximation may support a VALID verdict only after a no-under-approximation transport argument and a reference bridge. Multiple tainted aliases alone give a candidate violation, not INVALID. Until then: diagnostic tags and UNKNOWN, not target E certification.

## DUP-LAM effect: the copied function is never applied

The second fixed differential keeps the context identical and changes only
the value supplied to the one-use percent alias:

```text
@main =
  ! &F{f,g} = λx.&F{x,#Other{}};
  ! &F{a,b} = f(#First{});
  % h = VALUE;
  ! &R{h0,h1} = h;
  !! unused = h0;
  #Pair{a,b}
```

| VALUE | Complete result multiset | Interactions |
|---|---|---:|
| `g` | `#Pair{#First{},a}` with multiplicity **2** | 9 |
| `λu.#Other{}` | `#Pair{#First{},a}` with multiplicity **1** | 8 |

Both runs exited 0, complete, with no gate reasons under the same pin and
8-second/500-MB/-C64 limits. Manifest: `astra_pct_dup_effect_manifest.json`.
Raw evidence:
`astra_evidence/pct_dup_effect/sessions/a59dcaf303c5445ba331537e15746ff9/result.json`.

Forcing h0 only exposes a lambda; neither h0 nor h1 is applied. The copy of g
writes its original binder x1 to `SUP_R(y0,y1)`. The retained b reads that SUP,
and collapse produces two worlds. The replacement lambda has an erased binder;
copying it leaves the retained x1 free, producing one world. No argument-write
through an application of either output copy is involved.

Thus tagging only later APP-LAM writes of the two copied functions is not
sufficient. Dependency transport must cover the original DUP-LAM binder write
and reference world existence/multiplicity, not just the values printed in
individual worlds. The prototype's SUP-at-readback UNKNOWN is an appropriate
unsupported boundary; these controls are not evidence that it emitted a false
E verdict.
