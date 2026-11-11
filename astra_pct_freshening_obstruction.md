# Paper review: E does not license unconditional freshening of percent labels

Status: source/scalar-rule derivation only. No executable fixture was created, no parser/interpreter/native run was performed, and no solver was used. This reviews O2 of `snow_copy_aware_pct_rule_proposal.md` (0885); it is not a general no-fusion result or a classification of any target.

Reference H: `astra_evidence/reference_repro_6defdfc_gcc_o2/src/hvm.c`, upstream 6defdfc, SHA256 `3d2724d0716b5d6b1c07a3b0b3c5cb89f848487a43d364ea689658f9aeb75fe7`. Percent means the established lexical replacement by cloned let `! &`.

## 1. The proposed O2 is universal and retains public labels

The proposal says that every E-valid program has equal full collapse output and termination when each percent copier is assigned a globally fresh label, with all ordinary/source labels unchanged. Criteria v4 impose no public-label exclusion, freshness promise, or restriction to the five target syntaxes. In particular, the reference permits a public dynamic SUP to use an auto-copier's numeric label.

Here is a paper source schema, with no earlier definitions or auto-dup sites:

```text
@main =
  % x = &(8388608){#Left{}, #Right{}};
  (lambda a. lambda b. a)(x, x)
```

`lambda` in this display denotes the native lambda token. The two x occurrences are distinct source aliases, in argument order. This is not a proposed source change to a target or a new recorded oracle case.

### Pin-relative parser bridge

- H:226 initializes `PARSE_FRESH_LAB` to `0x800000`, which is decimal 8388608.
- H:3068-3109 parses `&(term){left,right}` as a dynamic SUP; decimal NUM is parsed at H:3166-3179. No auto-copier label is allocated by that literal or by either single-use/erasing selector binder.
- Cloned let is lambda application plus `parse_auto_dup` (H:2601-2661). Exactly two x uses cause one fan, label K=8388608 (H:2043-2054,2079-2086).
- The first x becomes side 0 and the second side 1 by child order (H:2006-2013,2034-2038).
- Dynamic SUP evaluation installs the supplied numeric label without an auto-label namespace exclusion (H:4152-4155).

Thus the relevant compiled graph is one fan d_K on `SUP_K(Left,Right)`, whose side 0 and side 1 are supplied to the first-selector lambda. There is no ordinary enclosing closure copy and no recursion.

## 2. Finite scalar derivation

In both evaluators the selector's first application saves d0 as a; its second, erasing application returns a without demanding d1. APP is function-first, and erased APP-LAM neither reads nor writes its argument (H:3732-3742,4765-4770,4952-4974).

**Reference C1:** d0 forces the dynamic SUP. Equal labels K/K select Left and cache Right on the unused opposite side (H:3923-3930). The final graph is the nullary constructor Left. Full collapse therefore has exactly one world:

```text
{ Left : 1 }
```

**Proposed C1^kappa:** d has fresh kappa != K; the source SUP remains K. Unequal-label commute produces `SUP_K(u0,v0)` with fresh copier u_kappa on Left and v_kappa on Right (H:3931-3938). Both are nullary copies (H:3949-3954). Full collapse queues both SUP children (H:6177-6181), giving:

```text
{ Left : 1, Right : 1 }
```

These are paper-derived multisets, not recorded native outputs. Both derivations terminate; the disagreement is already full-output equality, not a timeout inference.

## 3. Why this satisfies E under the authorized reading

There is one dynamic percent activation, no enclosing closure-copy fork, and one reference collapse world. Only its first alias supplies that result. The second alias is an argument of an erasing selector binder, is never entered, and has no retained binder-write or world-existence route. The opposite cache holding Right is unreachable from the result.

This argument keeps the compiled fan and both source alias positions fixed. It does not remove the dormant source occurrence and recompile, which would change the cloned-let fan arity. Nor does it use K's opposite sides to manufacture resource identities or separate worlds. There is simply at most one contributing alias in the one actual C1 world, so E holds.

Consequently the paper derivation refutes universal O2 as written: E is not a label-freshness or public-correlation-erasure guarantee.

## 4. Exact scope of the conclusion

- This blocks the submitted factorization through unconditional `C1^kappa`, subject to checking the displayed finite source/rule derivation. It is not executed evidence and has not been inserted into any historical certificate or clause pool.
- It does not establish a defect on the literal-free five targets. Their E status remains UNKNOWN.
- It does not refute every representation lacking physical K-tagged nodes: another representation can retain K's comparison/correlation information in metadata or fall back to C1 when needed.
- It does not establish that percent supplies no useful information, that generic compression is the only remaining route, or that copy-aware fusion is impossible.
- Silently excluding public auto-label collisions would strengthen the stated contract. A mechanism can instead propose a sound, costed preservation/fallback condition; that is a different obligation from universal O2.
- A bounded differential with no observed mismatch could not prove O2. An E-UNKNOWN mismatch would refute unconditional generic equivalence but would not by itself refute promise-domain soundness.

No build/run approval is requested or implied by this review.
