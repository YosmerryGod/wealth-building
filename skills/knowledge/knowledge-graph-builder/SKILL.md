---
name: Knowledge Graph Builder
category: Knowledge Engineering
description: "Use when a request needs map evidence-backed relationships and gaps across skills."
triggers:
  - "peta skill"
  - "hubungan antar skill"
  - "audit celah"
out_of_scope: "Becoming a mandatory step for every request or replacing the governance registry"
escalation: "Hand off work involving Becoming a mandatory step for every request or replacing the governance registry to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# Knowledge Graph Builder

## Purpose

Turn the complete Wealth Building repository into a connected, explainable body of knowledge that an AI assistant can navigate and reason across. This is an AI reasoning skill, not a software graph engine. Build and maintain the graph in the current reasoning context using the repository's existing Markdown files as the source of truth.

The graph must help the AI answer questions that cross domains, find the right specialist skills, detect duplicated or conflicting coverage, and identify meaningful knowledge gaps.

## When to use

Use this skill when asked to:

- Understand how skills or concepts across the repository relate.
- Find all skills relevant to a goal, problem, business, or project.
- Detect overlap, duplication, contradictions, or missing knowledge.
- Explain a concept through multiple connected domains.
- Recommend which skills an AI agent should consult and in what order.
- Review the knowledge architecture after skills are added, changed, moved, or removed.
- Produce a human-readable map of a topic or of the repository.

Do not invoke it for every ordinary question. If a single specialist skill fully covers a request, use that skill directly.

## Scope and source of truth

1. Scan the entire repository, not only the domain that appears relevant.
2. Treat every discovered `SKILL.md`, orchestrator, README, and reference document as a potential source.
3. Use the actual file contents. A filename or README summary is a discovery hint, not proof of detailed coverage.
4. Preserve the repository's domain names, skill names, terminology, and distinctions.
5. Do not assume the README index is complete. Compare it with the discovered files.
6. Do not invent skills, concepts, sources, claims, or relationships to make the graph appear comprehensive.
7. If a file cannot be opened, mark it as uninspected and do not infer its detailed contents.

## Operating workflow

### 1. Discover

- Enumerate all skill and orchestrator files across the repository.
- Group files by their actual folder/domain.
- Record each file's canonical relative path.
- Identify README entries with no matching file and files missing from the README.
- Distinguish specialist knowledge skills from orchestration and policy skills.

### 2. Extract knowledge

For each inspected file, identify:

- **Skill node:** name, domain, path, purpose, and role (specialist, orchestrator, policy, or reference).
- **Concept node:** a named principle, model, mechanism, technique, process, metric, or decision criterion that the file substantively explains.
- **Source node:** a book, article, video, repository, standard, person, or other origin explicitly named by the file.
- **Use-case node:** a practical situation or task to which the skill applies, when explicitly supported.
- **Relationship:** a meaningful connection between two nodes, with direction where relevant.

Do not create a separate node for every passing word. A concept deserves a node when it has explanatory or decision-making value.

### 3. Build relationships

Use only the relationship types below:

| Type | Meaning |
|---|---|
| RELATED_TO | Meaningful conceptual connection; direction is not significant |
| DEPENDS_ON | One skill or process requires another capability or prerequisite |
| PART_OF | A node is a component of a broader system or process |
| USES | A skill applies a concept, method, or tool |
| EXTENDS | One skill adds a distinct layer or capability to another |
| OVERLAPS_WITH | Two skills cover some of the same subject matter |
| CONFLICTS_WITH | Explicitly incompatible claims, definitions, or instructions |
| DUPLICATES | Substantially the same purpose and coverage, not merely related topics |
| APPLIED_IN | A concept or skill is used in a stated context |
| SOURCED_FROM | A skill or claim explicitly derives from a named source |
| ROUTES_TO | An orchestrator directs the AI to a specialist skill |

For every edge, record:
- source node ID
- relationship type
- target node ID
- concise rationale
- evidence: source path and section or heading
- confidence label

Do not infer DEPENDS_ON, CONFLICTS_WITH, or DUPLICATES from topical similarity alone. Prefer OVERLAPS_WITH when the boundary is partial or uncertain.

### 4. Label evidence and confidence

Every extracted claim or edge must use one evidence status:

- **EXTRACTED** — directly supported by the inspected source text.
- **INFERRED** — a reasoned relationship derived from multiple inspected details; explain the reasoning.
- **AMBIGUOUS** — evidence is insufficient, wording is unclear, or multiple interpretations remain plausible.

Confidence is separate from evidence status:
- **HIGH** — explicit and unambiguous support.
- **MEDIUM** — reasonable support but some interpretation is involved.
- **LOW** — weak or incomplete support; do not use as a decisive basis for recommendations.

Never present an INFERRED or AMBIGUOUS relationship as a fact. Never convert an AI interpretation into a source claim.

### 5. Detect overlap and gaps

For potential duplicates or overlap:

1. Compare purpose, scope, concepts, workflow, and intended use—not just titles or keywords.
2. Identify shared coverage and the unique contribution of each skill.
3. Recommend one of: keep separate, cross-link, clarify boundaries, consolidate, or investigate further.
4. Do not recommend deletion or merging solely because two skills are related.
5. Preserve useful specialist depth and source provenance.

For knowledge gaps:
- State the user goal or capability being evaluated.
- Identify which required concepts are already covered and cite their paths.
- Describe the missing concept or capability precisely.
- Distinguish a true gap from a file that has not yet been inspected.
- Suggest a new skill only when existing skills cannot reasonably cover the need without becoming incoherent.

### 6. Query and reason over the graph

When answering a question:

1. Translate the question into a target concept, task, or outcome.
2. Find directly relevant skill nodes.
3. Follow relevant edges to supporting skills, prerequisites, sources, and adjacent concepts.
4. Inspect the original files for details needed to answer.
5. Select the smallest sufficient set of skills; do not dump the whole graph.
6. Explain why each selected skill matters and how the skills complement one another.
7. Resolve conflicting guidance by returning to the original sources and describing the conflict; do not silently choose one.
8. Give a practical answer grounded in the inspected skill content.

### 7. Maintain the graph after repository changes

When a skill is added, updated, renamed, moved, or removed:

- Re-scan the affected domain and all direct links or references.
- Update affected skill nodes, concept nodes, and edges.
- Re-check relationships that may have become duplicates, overlaps, or obsolete.
- Verify canonical paths and internal links.
- Mark relationships as needing review when source content changed materially.
- Do not claim the graph is current unless the relevant repository scope was actually re-inspected.

## Output formats

Choose the output that fits the request. Do not fabricate a generated file or persistent graph database; this skill itself does not execute scripts or write files.

### Skill map

| Skill | Role in the topic | Connected skills | Evidence |
|---|---|---|---|

### Relationship map

Use a compact adjacency list or Mermaid diagram. Every displayed relationship must have an evidence status and a source path in accompanying notes. Use Mermaid only when the graph remains readable.

### Overlap audit

| Skill A | Skill B | Shared coverage | Unique contribution | Recommendation |
|---|---|---|---|---|

### Knowledge gap report

| Required capability | Existing coverage | Gap | Suggested next step |
|---|---|---|---|

### Repository audit

Report:
- inspected files and domains
- files not accessible or not inspected
- missing README entries
- stale README paths
- confirmed overlaps and duplicates
- unresolved ambiguities
- recommended next actions

## Reasoning rules

- Prefer evidence over elegant diagrams.
- Preserve distinctions between related disciplines.
- A relationship does not mean two skills are interchangeable.
- Similar vocabulary does not prove equivalent meaning.
- A source relationship does not mean the source validates every AI-added framework in a skill.
- Distinguish original source material, repository synthesis, and the AI's new inference.
- Keep source paths attached to claims so the AI can return to the original context.
- Do not claim exhaustive coverage unless every file in the stated scope was inspected.
- When the user asks for all skills, report the actual scan scope and any inaccessible files.
- Keep the knowledge base open to new domains; do not force every concept into existing categories.

## Integration with other skills

- Use **Creative Intelligence Engine** to generate and develop ideas across domains. Use this skill alongside Knowledge Graph Builder when a task needs both creative synthesis and evidence-backed mapping; the graph identifies relationships, while Creative Intelligence turns relevant connections into hypotheses and candidate solutions.
- Use the **Business Agent Orchestrator** to coordinate an end-to-end business project. Knowledge Graph Builder helps it discover cross-domain specialist knowledge; it does not replace project orchestration.
- Use the **Psychology Decision Engine** for role- and relationship-sensitive selection of Psychology skills. The graph can expose related skills but must not replace contextual judgment.
- Use **Risk Assessment & Consequence Intelligence** for evaluating material action consequences. The graph organizes knowledge; it does not authorize or prohibit actions.
- Consult specialist skills for their full subject matter. A graph summary is a navigation aid, never a substitute for the source skill.

## Limitations

This AI-only implementation has no persistent graph database, automatic file watcher, parser, or interactive visual explorer. It creates an evidence-grounded conceptual map during reasoning and can provide Mermaid or tabular representations in responses. A later software implementation would be a separate project and must not be implied to exist.

## Governance and ownership boundary

The canonical [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md) is the source of truth for skill ownership and routing. This graph maps evidence-backed relationships, dependencies, overlaps, and gaps; it does not become a second router that overrides the governance registry. For an overlap audit, compare primary responsibility, inputs, outputs, exclusions, and handoff—not keyword similarity alone. Recommend an edit to an existing skill before recommending a new skill. Keep the registry, README index, and skill relationship links synchronized after structural changes.

## Governance and ownership boundary

The canonical [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md) is the source of truth for skill ownership and routing. This graph maps evidence-backed relationships, dependencies, overlaps, and gaps; it does not become a second router that overrides the governance registry. For an overlap audit, compare primary responsibility, inputs, outputs, exclusions, and handoff—not keyword similarity alone. Recommend an edit to an existing skill before recommending a new skill. Keep the registry, README index, and skill relationship links synchronized after structural changes.
