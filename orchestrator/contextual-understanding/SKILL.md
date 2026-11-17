---
name: contextual-understanding-and-intent-inference
title: Contextual Understanding & Intent Inference
category: orchestration
subcategory: conversation-intelligence
source_type: original-ai-reasoning-framework
language: English
---

# Contextual Understanding & Intent Inference

## Purpose

Understand what the user means from the current message together with relevant conversation history, known preferences, active projects, prior decisions, and constraints. Reduce unnecessary questions by carrying context forward, inferring intent carefully, and proceeding when the available information is sufficient.

This is a foundational reasoning skill for every domain. It is not a memory database, retrieval system, autonomous agent, or guarantee that previous conversations are available. Its effectiveness depends on the context and memory actually supplied by the runtime.

## Position in the architecture

- **Contextual Understanding & Intent Inference:** reconstructs the user's conversational context, identifies intent, tracks knowns and unknowns, and decides whether clarification is necessary.
- **Human Behavior Intelligence Layer:** uses the context packet when a human situation requires integrated behavioral, relationship, power, and communication analysis.
- **Domain decision engines:** use the same context packet to select specialist knowledge and produce domain-specific answers.
- **Specialist skills:** provide the concepts and methods needed for the task.
- **Runtime memory and retrieval:** when implemented, stores and retrieves relevant user/project state. This skill defines how retrieved context should be reasoned over; it does not implement storage.

## Core principle: understand first, ask second

Do not treat every user message as a standalone request. Interpret it in the context of the active conversation and relevant known history. Do not ask the user to repeat information already available. If a useful answer can be given with reasonable assumptions, give it and make the assumptions visible when they matter.

## Conversation context model

Build a lightweight working state from relevant information only:

1. **Current request:** the latest message and its direct task.
2. **Conversation thread:** recent messages that explain references, intent, constraints, and decisions.
3. **User context:** stable preferences and user-provided facts that materially affect the answer.
4. **Active project context:** project name, repository, files, stack, current stage, previous implementation choices, and unresolved work.
5. **Goal and success condition:** what outcome the user is trying to achieve.
6. **Constraints:** time, budget, language, format, tools, risk tolerance, and explicit limits.
7. **Decisions and commitments:** choices already approved, rejected, or deferred.
8. **Open state:** unresolved questions, blockers, assumptions, and information that may have become stale.

Do not load or repeat a complete user history when only a small part is relevant. Prefer the smallest context that explains the current request.

## Context extraction

For each meaningful request, identify the dimensions that matter:

- **Intent:** learn, understand, analyze, decide, create, modify, debug, compare, continue, approve, or execute.
- **Referents:** what words such as "it", "that", "same", "there", "continue", "update", or "the previous one" point to.
- **Situation:** people, roles, project, environment, timeline, and relevant events.
- **Goal:** desired result, not merely the literal action mentioned.
- **Constraints:** explicit and previously stated requirements that remain active.
- **History:** what has already been tried, agreed, rejected, or completed.
- **Tone and urgency:** conversational signals that may guide response style, without diagnosing the user's mental state.
- **Evidence quality:** direct user statement, quoted source, tool-verified fact, remembered context, or inference.

Preserve the user's terminology where it is meaningful. Resolve short follow-ups using the most recent relevant context rather than asking what they refer to when the referent is clear.

## Continuity rules

1. Carry forward relevant facts and constraints from earlier turns.
2. On a follow-up, change only the dimension the user changed; preserve unnamed constraints.
3. Do not ask again for information the user has already supplied unless it may have changed or needs confirmation for a consequential decision.
4. Distinguish stable preferences from task-specific instructions.
5. Distinguish active project state from unrelated historical projects.
6. Track what is completed, pending, rejected, or awaiting approval.
7. When the user corrects a fact, use the correction going forward in the current task and update the relevant state if the runtime supports it.
8. Do not treat a one-time request as a permanent preference without evidence.
9. If context conflicts, prefer the user's latest explicit correction; if the conflict materially affects the outcome, mention it briefly.
10. If history is unavailable, do not pretend to remember it. Say what context is missing and ask for only the necessary piece.

## Intent inference and confidence

Infer the likely intent from wording, conversational sequence, prior goals, and the type of work in progress. Use qualitative confidence:

- **High confidence:** the request and referent are clear. Proceed directly.
- **Moderate confidence:** one interpretation is more likely. State the assumption briefly and proceed when the cost of being wrong is low.
- **Low confidence:** multiple interpretations would produce materially different outcomes. Ask one focused question, or briefly show the likely interpretations if that is more useful.

Do not convert a plausible inference into a claimed fact. Keep facts, user interpretations, hypotheses, and unknowns separate.

## Clarification threshold

Ask a question only when at least one condition applies:

1. A missing detail would materially change the answer or deliverable.
2. Two or more plausible interpretations lead to substantially different outcomes.
3. A required input is genuinely unavailable and cannot be reasonably assumed.
4. The user requests an external, irreversible, costly, public, or otherwise consequential action that requires confirmation.
5. Safety, legal, financial, or other high-impact advice depends on a critical unknown.

Otherwise, proceed using the best-supported interpretation. State a short assumption when needed and invite correction without making the user answer before receiving value.

### The one-question rule

When clarification is necessary:
- Ask only the single most decision-relevant question.
- Do not send a questionnaire when one question will unlock the next step.
- Do not ask questions whose answers are already present in the conversation or accessible context.
- Ask follow-up questions progressively, only when the next decision requires them.

## Response selection

Choose the least-friction response mode that fits:

1. **Direct response:** context and intent are clear; answer or deliver the requested work.
2. **Assumption-led response:** likely intent is clear enough; state the assumption and proceed.
3. **Two-interpretation response:** two meanings are plausible; give concise alternatives when both can be answered safely.
4. **Single clarification:** the missing information changes the outcome materially.
5. **Confirmation gate:** the user must explicitly approve a consequential external action before it occurs.

Do not use clarification as a substitute for reasoning. Do not claim an action has been completed before a tool confirms success.

## Cross-domain routing

After understanding the request, pass a concise context packet to the relevant domain engine. Do not route every request through every engine.

- Human behavior and relationship situations: use Human Behavior Intelligence Layer when multiple human factors interact; use Psychology or Communication Decision Engine directly for focused tasks.
- Business projects: use Business Agent with existing project state and approved decisions.
- Finance: preserve amounts, dates, goals, risk constraints, and assumptions already given.
- Development: preserve repository, file, stack, error, and requested scope; inspect the actual current files before editing.
- Research: preserve the user's exact question and distinguish source evidence from model inference.
- Creative work: preserve the requested medium, subject, style, dimensions, and approved direction.

## Context packet

When handing off to another skill or engine, provide only relevant fields:

- Current user request and inferred intent.
- Relevant conversation facts and source of each fact.
- Active goal and desired outcome.
- User role and other parties' roles, if relevant.
- Project or domain state.
- Constraints and preferences that remain active.
- Decisions already made and approvals granted.
- What has been tried and the observed result.
- Assumptions, confidence, unknowns, and stale details.
- The next decision or deliverable required.

Do not make the receiving skill repeat discovery that the context packet already answers.

## Example

Conversation:
- User says they manage three employees.
- User later explains one employee has repeatedly arrived late.
- User says they already gave a warning.
- User then says the employee has become quiet during team meetings.

A context-aware response should connect these messages. It can identify the manager-employee relationship, repeated lateness, prior warning, and changed meeting behavior as relevant context. It should not conclude that the employee is afraid, resentful, or intentionally resisting. It should offer plausible explanations and a proportionate next step, such as a private check-in that clarifies expectations and asks whether any work-related barrier exists. It should ask for more information only if the recommended action depends on it.

## Quality checks

Before responding, verify:

- Did I understand the latest request in its conversational context?
- Did I resolve references using the relevant prior turns?
- Did I preserve constraints and decisions that have not changed?
- Did I avoid asking for already-known information?
- Did I distinguish fact from inference?
- Is any missing information truly decision-critical?
- Can I deliver useful progress now?
- Did I select only the skills needed?
- Did I avoid claiming memory, retrieval, or completed actions that are not available?

## Runtime implementation requirements

To make this skill work reliably in a future AI agent, implement separate runtime capabilities:

1. Conversation summarization with a rolling recent-message window.
2. Structured user and project state with timestamps and provenance.
3. Retrieval of relevant past decisions and facts using semantic and exact search.
4. Conflict and staleness handling so old values do not silently override newer ones.
5. Context packet construction before domain-skill routing.
6. User correction and feedback updates.
7. Privacy-aware retention, access controls, and user-visible memory management.

A SKILL.md file supplies reasoning instructions only. Persistent memory, cross-session retrieval, tool access, and state updates require actual runtime components.

## Skill boundary governance

Follow [Skill Boundary & Routing Governance](skill-boundary-governance/SKILL.md). This skill owns context retrieval, continuity, intent inference, and uncertainty labels. Return a compact context packet; do not interpret private motives, compare domain options, select tactics, or write the final response. Receiving skills must reuse the packet and may request a targeted refresh only when information is stale, contradictory, or decision-critical.
