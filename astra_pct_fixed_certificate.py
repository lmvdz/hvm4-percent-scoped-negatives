"""Restricted, executable issue-18 predicate certificate; NOT an HVM interpreter.

The source bridge is explicit: unfold make/id/fst/snd in the two fixed issue-18
programs, then expand their single ordinary closure copy.  Jan-4 is the same
minimal lambda term (after correcting the quoted transcription's first I1).
The copied closure's captured % aliases acquire ONE common copy-event identity
and side.  The % replacement copier does NOT generate resource identities.

An occurrence is an annotation on its delivered value.  An annotation on an
applied function follows the application result; substitution discards unused
arguments and their annotations.  Constructor fields retain annotations.
This is an erasure-sensitive affine-beta dependency certificate for these
closed terms, not a proved contribution analysis for arbitrary labeled nets.
No label-world projection, HVM parsing, recursive target or general preservation
lemma is implemented or claimed here.  All fixed cases have one output world.
"""
from dataclasses import dataclass, replace
from collections import defaultdict
import json


@dataclass(frozen=True, slots=True)
class Resource:
    site: str
    activation: int = 0
    copies: tuple = ()  # (logical closure-copy event, reference label, side)


@dataclass(frozen=True, slots=True)
class Use:
    resource: Resource
    occurrence: str


@dataclass(frozen=True, slots=True)
class Term:
    kind: str
    a: object = None
    b: object = None


def var(i): return Term("var", i)
def lam(body): return Term("lam", body)
def app(f, x): return Term("app", f, x)
def ctr(name, *fields): return Term("ctr", name, tuple(fields))


def marked(uses, value):
    uses = frozenset(uses)
    while value.kind == "mark":
        uses |= value.a
        value = value.b
    return Term("mark", uses, value) if uses else value


def map_children(t, fn, under_lambda=None):
    if t.kind == "var": return t
    if t.kind == "lam": return lam((under_lambda or fn)(t.a))
    if t.kind == "app": return app(fn(t.a), fn(t.b))
    if t.kind == "ctr": return ctr(t.a, *(fn(x) for x in t.b))
    if t.kind == "mark": return marked(t.a, fn(t.b))
    raise ValueError(t.kind)


def shift(t, delta, cutoff=0):
    if t.kind == "var":
        return var(t.a + delta) if t.a >= cutoff else t
    return map_children(t, lambda x: shift(x, delta, cutoff),
                        lambda x: shift(x, delta, cutoff + 1))


def substitute(t, value, depth=0):
    if t.kind == "var":
        return shift(value, depth) if t.a == depth else t
    return map_children(t, lambda x: substitute(x, value, depth),
                        lambda x: substitute(x, value, depth + 1))


def bound_count(t, depth=0):
    if t.kind == "var": return int(t.a == depth)
    if t.kind == "lam": return bound_count(t.a, depth + 1)
    if t.kind == "app": return bound_count(t.a, depth) + bound_count(t.b, depth)
    if t.kind == "ctr": return sum(bound_count(x, depth) for x in t.b)
    if t.kind == "mark": return bound_count(t.b, depth)
    raise ValueError(t.kind)


def closure_copy(t, event, label, side):
    """Explicit logical copy of the WHOLE enclosing closure, not an alias copy."""
    if t.kind != "lam": raise ValueError("copy must start at a closure")
    def go(x):
        if x.kind == "mark":
            uses = [replace(u, resource=replace(u.resource,
                    copies=u.resource.copies + ((event, label, side),))) for u in x.a]
            return marked(uses, go(x.b))
        return map_children(x, go)
    return go(t)


class Unsupported(Exception):
    pass


class Normalizer:
    def __init__(self, eager=False, budget=10000):
        self.eager, self.budget = eager, budget
        self.reads = set()
        self.beta_steps = 0

    def whnf(self, t):
        self.budget -= 1
        if self.budget < 0: raise Unsupported("reduction budget")
        if t.kind == "mark":
            self.reads.update(t.a)
            return marked(t.a, self.whnf(t.b))
        if t.kind != "app": return t
        f = self.whnf(t.a)
        x = self.whnf(t.b) if self.eager else t.b
        uses = set()
        while f.kind == "mark":
            uses.update(f.a)
            f = f.b
        if f.kind != "lam":
            return marked(uses, app(f, x))
        if bound_count(f.a) > 1:
            raise Unsupported("implicit nonlinear beta: explicit copy certificate required")
        self.beta_steps += 1
        body = shift(substitute(f.a, shift(x, 1)), -1)
        return self.whnf(marked(uses, body))

    def nf(self, t):
        t = self.whnf(t)
        return map_children(t, self.nf)


def dependencies(t):
    if t.kind == "mark": return set(t.a) | dependencies(t.b)
    if t.kind == "var": return set()
    if t.kind == "lam": return dependencies(t.a)
    if t.kind == "app": return dependencies(t.a) | dependencies(t.b)
    if t.kind == "ctr":
        return set().union(*(dependencies(x) for x in t.b))
    raise ValueError(t.kind)


def render(t, names=()):
    if t.kind == "mark": return render(t.b, names)
    if t.kind == "var": return names[t.a] if t.a < len(names) else f"FREE{t.a}"
    if t.kind == "lam":
        name = chr(ord("a") + len(names))
        return f"λ{name}.{render(t.a, (name,) + names)}"
    if t.kind == "app": return f"({render(t.a, names)} {render(t.b, names)})"
    if t.kind == "ctr": return "#" + t.a + "{" + ",".join(render(x, names) for x in t.b) + "}"
    raise ValueError(t.kind)


def predicate(uses, reading="per_copy"):
    groups = defaultdict(set)
    for u in uses:
        r = u.resource
        if reading == "per_copy": key = (r.site, r.activation, r.copies)
        elif reading == "per_activation": key = (r.site, r.activation)
        elif reading == "per_site": key = (r.site,)
        elif reading == "replacement_forks": key = (r.site, r.activation, r.copies, u.occurrence)
        else: raise ValueError(reading)
        groups[repr(key)].add(u.occurrence)
    return {"status": "valid" if all(len(xs) <= 1 for xs in groups.values()) else "invalid",
            "world": 0, "resources": {k: sorted(v) for k, v in sorted(groups.items())}}


IDENTITY = lam(var(0))
FIRST = lam(lam(var(1)))
SECOND = lam(lam(var(0)))
PAIR = lam(lam(ctr("Pair", var(1), var(0))))


def fixed_closure(site, applied=False):
    r = Resource(site)
    left = marked([Use(r, "left")], IDENTITY)
    right = marked([Use(r, "right")], IDENTITY)
    if applied:
        left, right = app(left, FIRST), app(right, SECOND)
    return lam(app(app(var(0), left), right))


def issue_term(site, applied=False, observed=False):
    f = fixed_closure(site, applied)
    f0 = closure_copy(f, "outer-copy", "L", 0)
    f1 = closure_copy(f, "outer-copy", "L", 1)
    a, b = app(f0, FIRST), app(f1, SECOND)
    result = app(app(a, b), IDENTITY) if applied else app(a, b)
    if observed:
        result = app(app(result, ctr("Left")), ctr("Right")) if applied else app(result, ctr("Token"))
    return result


def classify(name, term, expected):
    normalizer = Normalizer()
    nf = normalizer.nf(term)
    actual = render(nf)
    if actual != expected: raise AssertionError((name, actual, expected))
    deps = dependencies(nf)
    return {"name": name, "output": actual, "worlds": 1,
            "beta_steps": normalizer.beta_steps,
            "uses": [{"site": u.resource.site, "activation": u.resource.activation,
                      "copies": u.resource.copies, "occurrence": u.occurrence}
                     for u in sorted(deps, key=repr)],
            "readings": {r: predicate(deps, r) for r in
                         ("per_copy", "per_activation", "per_site")}}


def run():
    cases = [
        classify("issue18.minimal", issue_term("minimal.s"), "λa.a"),
        classify("issue18.minimal.observed", issue_term("minimal.s", observed=True), "#Token{}"),
        classify("issue18.make_B", issue_term("make_B.s", applied=True), "λa.λb.b"),
        classify("issue18.make_B.observed", issue_term("make_B.s", applied=True, observed=True), "#Right{}"),
        classify("jan4.corrected_derivation", issue_term("jan4.G"), "λa.a"),
    ]
    for c in cases:
        assert c["readings"]["per_copy"]["status"] == "valid"
        assert c["readings"]["per_activation"]["status"] == "invalid"
        assert c["readings"]["per_site"]["status"] == "invalid"
        assert len(c["uses"]) == 2

    # Same copied closure, both aliases retained: the default must reject it.
    bad = app(closure_copy(fixed_closure("bad.s"), "outer-copy", "L", 0), PAIR)
    bad_nf = Normalizer().nf(bad)
    bad_uses = dependencies(bad_nf)
    assert predicate(bad_uses)["status"] == "invalid"
    assert predicate(bad_uses, "replacement_forks")["status"] == "valid"

    # Legal eager evaluation can inspect a subsequently erased alias.  This is
    # a MODEL scheduling control, not a claim about native HVM's physical trace.
    r = Resource("erasure.s")
    a = marked([Use(r, "left")], IDENTITY)
    b = marked([Use(r, "right")], IDENTITY)
    erased = app(lam(a), b)
    lazy, eager = Normalizer(), Normalizer(eager=True)
    lazy_nf, eager_nf = lazy.nf(erased), eager.nf(erased)
    assert render(lazy_nf) == render(eager_nf) == "λa.a"
    assert dependencies(lazy_nf) == dependencies(eager_nf) == {Use(r, "left")}
    assert predicate(eager.reads)["status"] == "invalid"
    assert predicate(dependencies(eager_nf))["status"] == "valid"

    return {"scope": "fixed affine-lambda certificate with an explicit ordinary closure-copy bridge; not general HVM SC certification",
            "source_fixtures": ["astra_cases/falsifier.issue18.minimal.pct.hvm",
                                "astra_cases/falsifier.issue18.applied_branches.pct.hvm"],
            "native_reference": "previously recorded manifest observations; no native rerun",
            "cases": cases,
            "controls": {"same_copy_pair_output": render(bad_nf),
                         "same_copy_pair_default": predicate(bad_uses),
                         "self_certifying_replacement": predicate(bad_uses, "replacement_forks"),
                         "erased_alias_semantic": predicate(dependencies(eager_nf)),
                         "erased_alias_eager_model_reads": predicate(eager.reads)},
            "historical_sides_note": "outer-copy sides 0/1 occur in ONE final result, not two collapse worlds",
            "target_classification": "not covered by this restricted model"}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False))
