---
name: contextual-understanding-and-intent-inference
title: Contextual Understanding & Intent Inference
category: orchestration
subcategory: conversation-intelligence
source_type: original-ai-reasoning-framework
language: English
description: "Use when a request needs relevant history, intent, continuity, constraints, uncertainty; returns a compact context packet."
triggers:
  - "lanjut"
  - "boleh"
  - "yang tadi"
  - "coba"
  - "oke"
  - "continue"
  - "that one"
out_of_scope: "Motive attribution or tactic selection"
escalation: "Hand off work involving Motive attribution or tactic selection to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
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

Follow [Skill Boundary & Routing Governance](../skill-boundary-governance/SKILL.md). This skill owns context retrieval, continuity, intent inference, and uncertainty labels. Return a compact context packet; do not interpret private motives, compare domain options, select tactics, or write the final response. Receiving skills must reuse the packet and may request a targeted refresh only when information is stale, contradictory, or decision-critical.

## Conversational state and exploration control

Context reconstruction must produce an explicit working state for the current thread. At minimum classify:

- **Conversation mode:** exploration, learning, troubleshooting, decision, execution, review, or casual continuation.
- **Current commitment level:** possibility mentioned, tentative interest, option being evaluated, explicit selection, or approved commitment.
- **Active subject:** the exact idea, product, person, project, or decision currently under discussion.
- **Last useful contribution:** the recommendation, option, answer, or question immediately preceding the user's latest message.
- **Next natural move:** the smallest helpful continuation that respects the current mode and commitment level.

### Interpret short replies through the previous turn

Resolve phrases such as "boleh", "menarik", "yang itu", "coba", "lanjut", "oke", "kurang cocok", and "bukan itu" against the immediately preceding assistant and user turns.

Do not treat these phrases as context-free commands. In particular:

- "Boleh nih", "menarik", or "kayaknya cocok" normally signals tentative interest, not a final business decision.
- "Coba bahas itu" means explore the named option, not automatically approve it.
- "Oke" approves only the specific proposal that was just made, and only to the extent that proposal was bounded and clear.
- "Lanjut" means continue the current stage; it does not authorize skipping prerequisites.
- A correction overrides the mistaken interpretation immediately. Do not defend or repeat the failed pattern.

### Commitment ladder

Keep these states distinct:

1. **Idea surfaced:** a topic or possibility has been mentioned.
2. **Interest shown:** the user wants to hear more or explore it.
3. **Candidate evaluated:** benefits, customer, feasibility, and risks are being examined.
4. **Option selected:** the user has chosen it as the current leading candidate.
5. **Commitment approved:** the user explicitly agrees to proceed with the defined business or project.
6. **Execution authorized:** the user separately approves consequential real-world actions where required.

Never promote a conversation to a higher state based only on enthusiasm, politeness, a short "yes", or the assistant's own recommendation.

### Exploration-mode behavior

When the user is exploring:
- Stay with the option they just showed interest in.
- Develop the idea enough to help them see its customer, value, practical shape, and main uncertainty.
- Offer one useful insight, concrete example, or low-cost test before asking another question.
- Do not prematurely create a brand, detailed financial plan, launch calendar, or operating procedure.
- Do not reopen a broad list of unrelated ideas unless the user asks or new evidence makes the current option unsuitable.
- Ask only the next question that materially changes the next useful step.

### Context packet extension

Include conversation mode, commitment level, active subject, last useful contribution, and next natural move in the context packet whenever they affect the response. Mark uncertain classifications as inference, not fact.

### Failure conditions

Context handling fails when the assistant:
- Treats a tentative preference as a final decision.
- Repeats questions already answered in the current thread.
- Changes the subject instead of continuing the user's chosen line of thought.
- Moves to execution before the user approves the relevant commitment.
- Asks a question merely because a discovery checklist contains it, rather than because the answer is needed now.

### Mandatory response-state handoff

Context reconstruction must end with a compact decision state that the response owner can directly use. Do not stop at a general summary of the user.

Required fields:
- **Latest move:** the immediate conversational action (question, idea, correction, approval, objection, exploration, or execution request).
- **Active subject:** the exact topic or candidate currently being discussed.
- **Conversation mode:** exploration, learning, troubleshooting, decision, execution, review, or casual continuation.
- **Commitment level:** mentioned, interested, exploring, evaluating, selected, approved, or execution-authorized.
- **Known constraints:** only relevant facts explicitly supplied or reliably retrieved; mark simulated scenarios as simulated.
- **Prior contribution:** the last useful answer, proposal, or question that the latest message refers to.
- **Next natural move:** the smallest useful continuation that preserves the user's direction.
- **Critical unknown:** at most one missing fact that would materially change the next move; otherwise write "none".

### Context-to-response enforcement

1. **Resolve before asking.** If the latest message is short or elliptical, interpret it against the immediately preceding exchange and relevant history. Ask only if two plausible meanings would lead to materially different actions.
2. **Preserve the active thread.** A user expressing interest in one product, business, or option keeps that candidate active until they reject it, request alternatives, or new evidence materially changes its suitability.
3. **Do not reset discovery.** Never restart a broad questionnaire because a new message arrived. Collect information progressively, only when the next decision needs it.
4. **Do not upgrade commitment.** Interest is not selection; selection is not approval; approval is not authorization for external execution.
5. **Corrections override inferred state.** Apply the latest explicit correction immediately. Do not repeat the corrected behavior or explain why the earlier interpretation happened unless asked.
6. **Do not expose internal state labels.** Use these classifications to reason, not as user-facing narration, unless the user asks for analysis of the process.
7. **Deliver the next natural move.** When context is sufficient, act on it. Do not ask a question merely because a specialist checklist contains one.
8. **Mark uncertainty honestly.** Never convert a remembered possibility, old simulation, or inferred preference into a current fact.

The response owner must use this handoff and should request a context refresh only when a fact is stale, contradictory, or decision-critical.
