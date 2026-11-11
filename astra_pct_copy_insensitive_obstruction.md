# Copy-sensitive exclusivity does not imply copy-insensitive exclusivity

Status: intermediate negative result under `percent_contract_criteria.md` v4.
Not a general no-fusion result, not a physical-copy lower bound, and not a
classification of the five canonical targets (which remain UNKNOWN).

## Definitions and witness

Write a promised resource as `(a, pi)`: original dynamic activation `a` plus
the COMPLETE enclosing-closure copy history `pi` carried by that contributing
occurrence. Do not also count it under every prefix of pi, and do not pad it
with later forks it did not traverse. A history may be a prefix of another
occurrence's history without identifying their resource versions. Logical
copy-event identities, not numerical label names, distinguish repeated copies.
Occurrence `o` is one of that resource's source aliases. Let `C(a, pi, u, o)`
mean semantic contribution to C1's collapsed (-C) result world `u`, with the
reference's label correlation and v4's authorized interpretation.

The stated promise is:

```
E(P): for every a, pi, u,
      |{o : C(a, pi, u, o)}| <= 1.
```

The stronger, copy-insensitive exclusivity assertion is:

```
Phi_ci(P): for every a, u,
           |{(pi, o) : C(a, pi, u, o)}| <= 1.
```

Issue #18 and the January-4 derivation are a counterexample to `E => Phi_ci`.
The enclosing ordinary copy produces histories `pi0` and `pi1`. Its two
captured aliases within each history retain ONE common resource identity;
the `%` replacement's own copier does not fork identities. In the one final
world the program uses:

```
C(a, pi0, u, left)
C(a, pi1, u, right)
```

Each resource contributes one alias, so E holds. Their union has two members,
so Phi_ci fails. Historical visits to opposite L sides do not make these two
final worlds: the calls recombine as `H0(I1)` in Taelin's derivation.

This is the quantifier distinction `for each copy, at most one` versus
`across all copies together, at most one`. No radius/locality assumption,
label freshness assumption, cost model, or hypothetical infinite family is
needed for this non-implication.

`Phi_ci` names copy-INSENSITIVE exclusivity, not Lars's separate candidate
about preserving per-copy resources. The latter is an open implementation
obligation/route; this witness does not refute it or establish that it requires
physical copying. Using one unqualified name Phi for both would be misleading.

## Evidence and semantic-contribution qualification

The source/scalar bridge and alternatives are recorded in criteria section
(e). Executed evidence is `astra_pct_fixed_certificate.py` and
`astra_pct_fixed_certificate_results.json`: issue18 minimal, make_B and the
Jan-4 initial program all pass the authorized per-copy reading; all reject
the copy-insensitive activation-only reading. Same-copy retention of both
aliases is a rejecting control. The certificate is restricted affine-beta
normalization with an explicit closure-copy expansion, not a general HVM
interpreter or an all-target transport theorem.

The two dependencies in the observed minimal case are not inferred merely
from two physical reads. Its reduced expression is `H(J)(#Token{})`, with
both H and J identity functions. Replacing H's delivered value by
`lambda ignored. lambda arg. #Changed{}` changes the observation to
`#Changed{}`; separately replacing J by `lambda arg. #Changed{}` does so too.
These are direct beta calculations at the two fixed occurrence positions;
they are not a general counterfactual definition/checker for contribution.
The original one-world program, not the modified diagnostics, is the witness.

Executed quantifier checks and these three reduced beta calculations are
retained in `astra_pct_copy_insensitive_checks.json`: each fixed certificate
has at most one contributing alias per resource copy and two across its
activation; the reduced observations are respectively `#Token{}`,
`#Changed{}`, `#Changed{}`.

Primary fixed test: https://github.com/HigherOrderCO/HVM4/issues/18
The Jan-4 repost (Discord 1457331764862124074) is transcribed verbatim in the
criteria appendix; its apparent intermediate index typo is not silently
used as a rule.

## What inference this refutes

E alone does not justify forgetting enclosing-copy histories and treating
the surviving aliases of an original activation as mutually exclusive.
In particular, an argument for MOV-style sharing that requires Phi_ci cannot
obtain it from E. This is the missing guarantee established here.

A concrete representation hazard is raw reuse of ONE mutable instantiated
lambda with unchanged destructive consumers and no ownership mechanism.
In unmodified upstream HVM4 commit `6defdfc`, independently read from
[src/hvm.c](https://github.com/HigherOrderCO/HVM4/blob/6defdfc/src/hvm.c):

- `wnf_app_lam`, lines 3732-3742: read the body at `loc`, then substitute
  the argument into that SAME location for a non-erasing lambda.
- `wnf_dup_lam`, lines 3882-3910: read that body, create distinct output
  lambda/binder locations, then substitute the binder SUP into the SAME
  original `lam_loc`.

These source operations explain why sharing immutable code is different
from handing out the same consumed heap-lambda cell twice. The relevant
first consumer may be a DUP-LAM, not only an APP-LAM. The cited source is
inspection evidence about these operations, not a new native MOV experiment.
Nor does this inspection prove that every shared representation must behave
like that mutable cell.

## What remains unproved

- Phi_ci is NOT shown necessary for every sound fusing implementation. It is
  necessary only for the exclusivity inference explicitly identified above.
- E does not require allocating a full fresh physical value for every logical
  copy. Immutable code with separate substitution state, retained provenance,
  deferred decisions, or another ownership representation are not excluded.
- Even Phi_ci per final world would not by itself establish safe destructive
  reuse across different worlds or under reference demand order.
- This witness alone gives no asymptotic lower bound and no target cost result.
- The backend-8 finite-table CEGIS exclusion is separate; it cannot fill the
  missing general necessity/unavoidability argument.

Thus the accepted tiered report is: the stated promise does not justify
MOV-style sharing based on copy-insensitive exclusivity. The general
promise-enabling fusion question remains OPEN.
