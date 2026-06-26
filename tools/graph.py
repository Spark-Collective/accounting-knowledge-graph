#!/usr/bin/env python3
"""Query + validate the typed-edge graph (the `relations:` frontmatter).

Usage:
  python3 tools/graph.py                 # summary (nodes, edges, by predicate)
  python3 tools/graph.py --node NAME     # outbound + inbound edges for a node
  python3 tools/graph.py --validate      # dangling targets + unknown predicates (exit 1 on error)
  python3 tools/graph.py --dot           # graphviz DOT of the typed edges

Wikilinks are for reading; `relations:` is the machine-traversable layer. See AGENTS.md.
"""
import os, re, sys, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ["concepts", "references"]
VOCAB = {"requires", "unlocks", "gates", "grounded_by", "affects", "alternative_to", "part_of"}
REQUIRED_FM = {"type", "title", "description", "tags", "sources", "confidence",
               "created", "updated", "verify_live", "review_after"}

def md_files():
    for d in DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            for f in files:
                if f.endswith(".md"):
                    yield os.path.join(dirpath, f)

def parse(path):
    """Return (basename, {predicate: [targets]}) from a file's frontmatter."""
    name = os.path.basename(path)[:-3]
    rels = {}
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    if not lines or lines[0].strip() != "---":
        return name, rels
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), len(lines))
    fm = lines[1:end]
    in_rel = False
    for ln in fm:
        if re.match(r"^relations:\s*$", ln):
            in_rel = True; continue
        if in_rel:
            m = re.match(r"^\s+(\w+):\s*\[(.*)\]\s*$", ln)
            if m:
                rels[m.group(1)] = [t.strip() for t in m.group(2).split(",") if t.strip()]
            elif re.match(r"^\S", ln):   # next top-level key ends the block
                in_rel = False
    return name, rels

def build():
    nodes, edges = set(), []
    for p in md_files():
        n, rels = parse(p)
        nodes.add(n)
        for pred, targets in rels.items():
            for t in targets:
                edges.append((n, pred, t))
    return nodes, edges

def cmd_summary(nodes, edges):
    by = {}
    for _, p, _ in edges:
        by[p] = by.get(p, 0) + 1
    sourced = len({s for s, _, _ in edges})
    print(f"nodes: {len(nodes)}  |  nodes with relations: {sourced}  |  typed edges: {len(edges)}")
    for p in sorted(by, key=lambda k: -by[k]):
        print(f"  {p:<14} {by[p]}")

def cmd_node(nodes, edges, name):
    out = [(p, t) for s, p, t in edges if s == name]
    inb = [(s, p) for s, p, t in edges if t == name]
    if name not in nodes:
        print(f"warning: '{name}' is not a known page");
    print(f"# {name}")
    print("outbound:")
    for p, t in out: print(f"  --{p}--> {t}")
    if not out: print("  (none)")
    print("inbound:")
    for s, p in inb: print(f"  {s} --{p}-->")
    if not inb: print("  (none)")

def cmd_validate(nodes, edges):
    errs = []
    for s, p, t in edges:
        if p not in VOCAB:
            errs.append(f"unknown predicate '{p}' on {s} -> {t}")
        if t not in nodes:
            errs.append(f"dangling target: {s} --{p}--> {t} (no such page)")
    if errs:
        print("VALIDATION FAILED:")
        for e in errs: print(f"  {e}")
        return 1
    print(f"OK , {len(edges)} edges, all targets resolve, all predicates in vocab.")
    return 0

def cmd_dot(edges):
    print("digraph accounting_kb {")
    print('  rankdir=LR; node [shape=box, style=rounded];')
    for s, p, t in edges:
        print(f'  "{s}" -> "{t}" [label="{p}"];')
    print("}")

def cmd_lint():
    """Check every concept/reference page has the required frontmatter + >=2 wikilinks."""
    errs = []
    for p in md_files():
        rel = os.path.relpath(p, ROOT)
        with open(p, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        if not lines or lines[0].strip() != "---":
            errs.append(f"{rel}: no frontmatter"); continue
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), len(lines))
        keys = {m.group(1) for ln in lines[1:end] if (m := re.match(r"^([A-Za-z_]+):", ln))}
        missing = REQUIRED_FM - keys
        if missing:
            errs.append(f"{rel}: missing frontmatter {sorted(missing)}")
        if "\n".join(lines[end + 1:]).count("[[") < 2:
            errs.append(f"{rel}: fewer than 2 [[wikilinks]]")
    if errs:
        print("LINT FAILED:")
        for e in errs: print(f"  {e}")
        return 1
    print(f"OK , all pages have the required frontmatter and >=2 wikilinks.")
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--node")
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--lint", action="store_true")
    ap.add_argument("--dot", action="store_true")
    a = ap.parse_args()
    nodes, edges = build()
    if a.lint: sys.exit(cmd_lint())
    if a.validate: sys.exit(cmd_validate(nodes, edges))
    if a.node: cmd_node(nodes, edges, a.node); return
    if a.dot: cmd_dot(edges); return
    cmd_summary(nodes, edges)

if __name__ == "__main__":
    main()
