# Cover note for Taelin

*Draft for Lars to send himself; not posted or sent to Taelin by the sessions.*

*Basis: current D1-inclusive report `7e58d459`; criteria v5 `3b7b3b41`.*

Hi Taelin,

We studied your MOV/`%` bounty and whether its enabling information follows from your [December 30 statement](https://discord.com/channels/912426566838013994/915345481675186197/1455530019890659399): “only one of the 3 x's is reachable within the same label universe (that's the contract the user makes).” We would appreciate your correction of our interpretation before taking these findings further.

**Our interpretation**, rather than formal details we attribute to you, is:

- A `%` resource belongs to a dynamic activation and follows copies of its enclosing/capturing closure; its own replacement copier cannot create separate resources for its aliases.
- A universe is one reference collapse world, retaining label correlation and world multiplicity; reachability means semantic contribution, not merely an evaluator read.
- Attribution is **source-use**: an occurrence contributes through its own demand, including retained effects; effects created by copying that serves another occurrence's demand are not attributed to it.

Under that reading, we obtained two scoped findings:

1. **Per-copy exclusivity does not imply exclusivity across copies:** [issue #18](https://github.com/HigherOrderCO/HVM4/issues/18), both examples, and your [January 4 derivation](https://discord.com/channels/912426566838013994/915345481675186197/1457331764862124074) allow different copies' selected aliases to recombine in one world—supported by a finite source-level argument and a previously executed restricted annotated certificate, not a general native provenance checker.
2. **The promise does not justify universally freshening only the `%` replacement copiers:** in the example below, C1 returns only `Left`, whereas a replacement label fresh relative to the unchanged public SUP produces `Left` and `Right`—a finite paper derivation against the pinned parser/rules, not an executed differential.

```text
@main =
  % x = &(8388608){#Left{}, #Right{}};
  (λa.λb.a)(x, x)
```

With no preceding auto-dup sites, `8388608` is the reference parser's first auto label; only the first occurrence is demanded.

In the design explored so far, any proposed asymptotic `%`-specific advantage depends on confining the mechanism to `%` machinery plus a metadata-only stack hook; an unconfined generic alternative using snapshots and binder-escape tracking plausibly recovers essentially all that proposed gain. This is a paper estimate, not an implemented or measured advantage.

These are **not a no-fusion theorem or a physical-copy/interaction lower bound**. Retained-history and checked-invariant mechanisms remain open, and all five targets' promise classifications remain **UNKNOWN**.

The D1 paper review also makes the existing backend-8 exclusion promise-admissible for its fixed, stateful seven-primitive/20-key family, under the recorded runtime assumptions—not for arbitrary `%` mechanisms.

Two questions would help us:

1. Is per-copy resource identity your intended reading, so distinct closure copies may select different aliases that later recombine in one world?
2. Is source-use attribution intended, or should an undemanded occurrence also count when its copier component is observed through a retained binder write caused by demanding another occurrence?

The [full scoped report](pct_scoped_negatives_report.md) gives the exact witnesses, evidence tiers, reference pins and limitations.
