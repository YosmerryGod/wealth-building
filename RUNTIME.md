# Runtime Specification

This document defines the behavior expected from an AI runtime using this repository. It is a specification, not executable runtime code.

## 1. Per-message execution flow

1. **Context packet:** reconstruct the latest request from the relevant conversation window and retrieved user/project state. Include intent, active subject, conversation mode, prior contribution, known constraints, decisions, commitment level, assumptions, unknowns, and next natural move.
2. **Router:** load `skills.json` for skill IDs, paths, trigger hints, and ownership summaries. Treat Skill Boundary & Routing Governance as authoritative when ownership conflicts occur. Triggers are hints, not decisions.
3. **Skill loading:** load at most three `SKILL.md` files. Always-on skills count toward the cap. Select the smallest sufficient set.
4. **Primary owner:** assign exactly one lead skill/orchestrator responsible for the final decision and synthesis. Supporting skills return bounded evidence, criteria, calculations, or draft components.
5. **Quality gate:** check ownership, evidence provenance, uncertainty, user constraints, risk escalation, duplicate analysis, response proportionality, and approvals.
6. **State update:** persist useful changes with timestamps and provenance. Record corrections, decisions, commitments, and outcomes; never promote tentative interest into approval.

## 2. User and project state schema

The following logical schema is illustrative. Unknown fields remain absent or explicitly unknown; they must not be fabricated.

```json
{
  "user_profile": {
    "stable_preferences": [],
    "skills_and_experience": [],
    "resources_and_constraints": [],
    "communication_preferences": [],
    "updated_at": "ISO-8601",
    "sources": []
  },
  "projects": [{
    "project_id": "stable-id",
    "name": "project name",
    "goal": "desired outcome",
    "status": "exploring | evaluating | selected | approved | executing | paused | completed",
    "current_state": {},
    "decisions": [{
      "decision": "what was chosen or rejected",
      "status": "proposed | accepted | rejected | deferred",
      "decided_at": "ISO-8601",
      "source": "message/file/tool reference"
    }],
    "commitment_ladder": {
      "level": "mentioned | interested | exploring | evaluating | selected | approved | execution-authorized",
      "updated_at": "ISO-8601",
      "source": "message/file/tool reference"
    },
    "open_questions": [],
    "assumptions": [],
    "updated_at": "ISO-8601",
    "sources": []
  }]
}
```

Each material fact should record provenance: source type (user statement, conversation retrieval, file, tool verification, estimate, or inference), source reference when available, observed timestamp, and freshness. Store only necessary information and follow privacy and retention controls.

## 3. Internal `skills_used` contract

- Maintain an internal `skills_used` list for each repository-routed response, with selected skill IDs and roles (`primary` or `supporting`).
- Include only skills actually loaded and applied; a trigger match alone does not count.
- Enforce one primary owner, no more than two supporting skills, and no more than three loaded skills total.
- If the quality gate finds `skills_used` empty for a request requiring repository routing, repeat routing and load the narrowest applicable skill before answering.
- For simple requests requiring no specialist, record an explicit direct-answer route rather than inventing a skill invocation.
- Do not expose `skills_used` in ordinary user-facing answers unless requested.

## 4. Missing or unavailable context

- Never pretend to remember information absent from the current conversation or retrieved state.
- Distinguish confirmed facts from inferred or stale details.
- Resolve short follow-ups from the recent thread when the referent is clear.
- If retrieval fails, state the specific missing detail only when it materially affects the answer; ask one focused question.
- Never convert an old simulation, tentative interest, or inferred preference into a current fact.
- When sources conflict, prefer the latest explicit user correction and retain provenance.

## 5. Mandatory Risk Assessment routing

Invoke `risk-assessment` when a request involves material legal exposure, physical or psychological safety, exploitation, coercion, fraud, serious wrongdoing, significant financial exposure, irreversible action, or high-consequence effects on others.

Risk Assessment evaluates the requested action, not the topic label. Educational, historical, analytical, fictional, and preventive knowledge can be explained fully. If operational assistance would facilitate serious crime, exploitation, or fraud, do not provide those operational steps; state the boundary briefly and offer a lawful, constructive alternative. Clarify ambiguous intent only when the missing context materially changes the response.

## 6. Final quality gate

Verify that the context packet is current; selected skills own their work; exactly one primary owner exists; no more than three skills were loaded; facts and assumptions are distinguished; Risk Assessment was invoked when required; unavailable memory is not claimed; the answer addresses the latest conversational move; and external or irreversible actions have explicit user approval.
