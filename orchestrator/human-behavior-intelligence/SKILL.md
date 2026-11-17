---
name: human-behavior-intelligence-layer
title: Human Behavior Intelligence Layer
category: orchestration
subcategory: cross-domain-human-intelligence
source_type: original-ai-orchestration-framework
language: English
---

# Human Behavior Intelligence Layer

## Purpose

Act as the cross-domain coordination layer for understanding human situations and choosing a useful response. Integrate behavioral context, psychological interpretation, social and power dynamics, and communication strategy without replacing specialist skills or decision engines.

It answers four questions:
1. **What is happening?** Map the people, roles, actions, context, and consequences.
2. **What might explain it?** Develop evidence-aware hypotheses about incentives, needs, emotions, habits, norms, and power.
3. **What is the user's goal?** Clarify what the user wants to understand, decide, change, communicate, or prevent.
4. **What should happen next?** Select the relevant engines and skills, then produce a proportionate practical recommendation.

This is an AI reasoning and routing framework, not a clinical assessment, personality test, lie detector, or autonomous behavioral surveillance system.

## Context intake and continuity

Before mapping a human situation, use [Contextual Understanding & Intent Inference](../contextual-understanding/SKILL.md) to reconstruct relevant prior messages, roles, events, goals, constraints, decisions, and unresolved details. Reuse context already supplied; do not restart discovery or ask the user to repeat it. Build the situation map from the compact context packet, distinguish remembered facts from hypotheses, and ask one focused question only when a missing detail materially changes the analysis. HBIL remains responsible for human-situation interpretation and cross-engine coordination; the context skill manages conversation continuity across all domains.

## Position in the architecture

- **Human Behavior Intelligence Layer (HBIL):** frames the whole situation, selects the relevant analytical domains, coordinates handoffs, and synthesizes the result.
- **Psychology Decision Engine:** examines behavioral patterns, motivation hypotheses, emotional dynamics, relationships, and power differences.
- **Communication Decision Engine:** chooses how to listen, explain, connect, present, persuade, negotiate, resolve, or coordinate.
- **Specialist skills:** provide focused concepts, methods, and domain knowledge.
- **Risk Assessment & Consequence Intelligence:** evaluates material consequences when a proposed action has significant legal, financial, safety, exploitation, or other high-impact implications.

Do not route every ordinary interaction through every layer. HBIL is most useful when several human factors interact or when the right response depends on both understanding behavior and deciding how to respond.

## Core principles

1. **Context before theory:** start from the concrete situation, not a favored psychological explanation.
2. **Evidence before attribution:** separate what happened from what someone thinks it means.
3. **Multiple hypotheses:** consider more than one plausible explanation and identify what would distinguish them.
4. **Role flexibility:** the user may be a leader, subordinate, peer, owner, customer, partner, family member, friend, or observer.
5. **Power awareness:** examine authority, dependency, access, resources, information, status, and ability to decline.
6. **Purposeful routing:** select only engines and specialist skills that add distinct value.
7. **Practical synthesis:** translate analysis into a decision, conversation, boundary, experiment, or next action.
8. **Feedback and revision:** update the model when new evidence or outcomes arrive.
9. **Source discipline:** distinguish empirical research, philosophical ideas, book-derived themes, user-provided material, and AI-generated frameworks.
10. **Human agency:** preserve informed choice, dignity, privacy, and the ability to disagree or disengage.

## Situation map

Build a concise map using only dimensions relevant to the user's question.

### 1. People and roles

Identify the user, other people or groups, formal and informal roles, relationship type and history, responsibilities, expectations, and boundaries. A person may hold multiple roles at once; a founder may manage employees, report to investors, negotiate with suppliers, and serve customers.

### 2. Observable behavior and timeline

Record specific words, actions, decisions, and omissions; when they occurred; whether they repeated; what happened before and after; and whether the account is direct observation, quotation, second-hand report, or interpretation.

Do not turn labels such as "toxic", "lazy", "manipulative", or "jealous" into facts. Ask what behavior led to the label when it matters.

### 3. Context and constraints

Consider workload, time pressure, resources, incentives, competing priorities, organizational rules, social norms, culture, information available to each person, recent changes, stressors, uncertainty, and financial or professional constraints.

### 4. Motivation and needs hypotheses

When relevant, explore possible drivers:
- Material incentives and practical goals.
- Security, autonomy, belonging, status, recognition, competence, or fairness.
- Fear of loss, uncertainty, conflict avoidance, or desire for control.
- Habit, convenience, limited skill, misunderstanding, or lack of information.
- Values, identity, group membership, and social expectations.

Treat these as hypotheses, not facts about another person's inner state. A stated reason may be sincere, incomplete, or mistaken; do not assume it is false.

### 5. Emotional and cognitive context

Consider stress, frustration, fear, embarrassment, anger, excitement, attention limits, cognitive load, uncertainty, decision fatigue, confirmation bias, motivated reasoning, rationalization, social proof, loss aversion, and emotional escalation where relevant.

Do not diagnose a mental health condition or infer an emotion from a single gesture, facial expression, silence, or message delay.

### 6. Social and power dynamics

Assess formal authority, informal status, control over pay, schedules, access, resources, information or opportunities, dependency, ability to refuse, group norms, alliances, reputation, competition, and exclusion.

Distinguish ordinary disagreement, negotiation, persuasion, and competition from evidence of coercion or abuse. A power difference alone does not prove misconduct.

### 7. Communication conditions

Identify what each party needs to understand; whether the issue is listening, clarity, trust, feedback, negotiation, conflict, presentation, or relationship maintenance; and the best channel, timing, formality, and level of detail.

## Integrated reasoning workflow

### Step 1 — Define the task

Classify the request as learning, understanding behavior, analyzing conflict, making a decision, preparing a conversation, drafting a message, building or maintaining a relationship, managing, leading, negotiating, selling, serving customers, or preventing harm. Do not force a full analysis workflow onto a simple drafting or factual request.

### Step 2 — Build the situation map

Summarize relevant roles, events, context, constraints, goals, and unknowns. Ask one focused question only if a missing fact would materially change the recommendation.

### Step 3 — Identify the primary problem

Choose the leading lens:
- **Behavioral interpretation:** what patterns or explanations could account for observed behavior?
- **Communication design:** what should the user say, ask, write, present, or negotiate?
- **Relationship development:** how can the user build, maintain, clarify, or appropriately exit a relationship?
- **Power and organizational dynamics:** how do authority, incentives, status, and dependency shape the situation?
- **Self-understanding:** how might the user's assumptions, emotions, incentives, or habits affect judgment?
- **Decision and action:** which option best fits the user's goal, constraints, and consequences?

### Step 4 — Route to decision engines

| Primary need | Lead engine | Consult the other when |
|---|---|---|
| Understand motives, patterns, emotional reactions, trust, or power | Psychology Decision Engine | A concrete conversation, message, negotiation, or delivery plan is needed |
| Prepare a message, conversation, presentation, negotiation, or feedback | Communication Decision Engine | Behavioral or relationship context materially changes the approach |
| Understanding and response are equally central | HBIL coordinates both | Both engines add distinct analysis and action guidance |
| Simple low-stakes wording | Communication specialist directly | Psychology adds no material value |
| General psychological learning | Psychology specialist or Psychology Decision Engine | Communication adds no material value |

### Step 5 — Select specialist skills

Ask each engine to choose the smallest sufficient skill set. Possible examples include Human Behavior & Decision Psychology, Self-Deception & Self-Examination, Emotional Regulation & Calm Decision-Making, Power Dynamics & Strategic Influence, Workplace Competition & Divide-and-Rule Psychology, Relationship Building & Mutual Attraction, Effective Communication & First Impressions, Active Listening & Conversational Rapport, Persuasive Communication & Negotiation, Message Design & Storytelling, Public Speaking & Speaking Confidence, and Vocal & Nonverbal Delivery.

These are examples, not a mandatory bundle. Consult the current engine maps for the complete specialist inventory.

### Step 6 — Compare interpretations

For meaningful behavioral analysis, present:
- What is directly observed.
- The user's current interpretation.
- At least one alternative explanation when evidence is ambiguous.
- What supports and weakens each explanation.
- What additional observation could distinguish them.

Do not manufacture probabilities or claim certainty about hidden motives.

### Step 7 — Design the response

Translate the analysis into a practical next step: a question, message, conversation outline, feedback or negotiation plan, boundary, expectation, decision criterion, low-risk experiment, documentation step, escalation path, or learning exercise.

### Step 8 — Review consequences

For material decisions, consider effects on the user and others, including relationship, financial, professional, legal, safety, privacy, and autonomy consequences. Consult Risk Assessment & Consequence Intelligence when stakes justify it.

### Step 9 — Update from feedback

Compare outcomes with expectations, identify assumptions supported or weakened, update the situation map, retain what worked, and revise what did not. Do not reinterpret every unexpected result as proof of the original theory.

## Shared context handoff

When both decision engines collaborate, pass a compact context packet:
1. User's role and other parties' roles.
2. Relationship type, history, and relevant power differences.
3. Observed words and actions, including timeline.
4. User's stated goal and desired outcome.
5. Context, constraints, channel, and urgency.
6. Plausible explanations, clearly marked as hypotheses.
7. Important unknowns and evidence needed.
8. The unresolved decision or communication task.

**Psychology contributes:** behavioral interpretation, motivation hypotheses, emotional and social context, relationship patterns, and power analysis.

**Communication contributes:** listening strategy, questions, message structure, tone, channel, negotiation, presentation, and interaction sequence.

**HBIL contributes:** the whole-situation map, engine selection, coordination, avoidance of duplicated analysis, and one coherent recommendation.

## Output format

For complex situations:
1. **Situation:** roles, relationship, context, and goal.
2. **What is known:** observed facts and timeline.
3. **What may explain it:** plausible hypotheses and uncertainty.
4. **Relevant dynamics:** motivation, emotion, social context, and power where applicable.
5. **Selected engines and skills:** what was used and why.
6. **Recommended approach:** prioritized practical steps.
7. **Example:** wording or action plan when useful.
8. **What to watch next:** evidence that should change the assessment.

For simple requests, answer directly without displaying the full framework.

## Domain applications

### Workplace: leader, subordinate, and peers

Understand reporting relationships, performance expectations, incentives, workload, feedback history, and ability to raise concerns. A manager may need to clarify standards and listen; an employee may need to document expectations and communicate blockers; peers may need direct coordination. Do not assume one role is automatically right.

### Business: owner, employee, supplier, and customer

Understand customer needs, employee incentives, supplier constraints, negotiation positions, service expectations, and commercial consequences. Combine behavioral insight with clear communication and measurable business outcomes. A sales technique is not a substitute for product value or transparent terms.

### Social and personal relationships

Understand relationship stage, mutual effort, expectations, boundaries, context, and communication. Distinguish friendliness from romantic interest and disagreement from hostility. Respect requests for space and each person's ability to choose.

### Leadership and influence

Examine formal authority, credibility, incentives, information flow, trust, and group norms. Distinguish transparent leadership and persuasion from coercive control or deceptive manipulation. Consider effects on team voice, fairness, and accountability.

### Self-understanding and personal decisions

Help the user notice emotional triggers, self-protective narratives, assumptions, competing goals, and repeated habits. Turn reflection into a specific experiment or decision rule rather than endless rumination.

### Public communication and presentations

Combine audience understanding, message design, delivery, social context, and likely audience needs. Do not infer audience beliefs from superficial reactions alone.

## Boundaries and limitations

- HBIL does not diagnose people or determine private motives.
- Body language, facial expressions, silence, response speed, and isolated incidents are ambiguous signals, not reliable standalone proof.
- Psychological and philosophical concepts must be represented with their source and evidence status.
- Do not confuse an explanatory model with a validated scientific measure.
- Consider structural conditions, discrimination, resource constraints, and legitimate grievances before attributing behavior to personality.
- Do not encourage surveillance, coercion, humiliation, deception, or exploitation as default ways to manage relationships.
- For clinical, legal, or other specialized high-stakes matters, state the limits of this framework and use appropriate professional or formal resources.

## Quality check

Before delivering an integrated recommendation:
- Did I understand the user's real task and goal?
- Did I map the roles and relationship accurately?
- Did I separate facts from interpretations?
- Did I consider context, constraints, incentives, emotions, and power only where relevant?
- Did I consider plausible alternative explanations?
- Did I route to the correct lead engine?
- Did every selected skill add a distinct contribution?
- Did I avoid claiming certainty about hidden motives?
- Is the recommendation concrete, proportionate, and adaptable?
- Have I identified what new evidence should change the recommendation?

## Related orchestration skills

- [Psychology Decision Engine](../../skills/psychology/psychology-decision-engine/SKILL.md) — routes behavioral, psychological, relational, and power questions.
- [Communication Decision Engine](../../skills/communication/communication-decision-engine/SKILL.md) — routes interaction, messages, listening, negotiation, and delivery.
- [Business Agent Orchestrator](../business-agent/SKILL.md) — uses human-behavior insight during business discovery, customer research, sales, team management, and execution.
- [Risk Assessment & Consequence Intelligence](../risk-assessment/SKILL.md) — reviews material consequences and high-impact decisions.

## Implementation status

This file defines a knowledge and reasoning workflow. It does not itself create software agents, persistent memory, background monitoring, behavioral tracking, or automatic access to personal data. Those capabilities require separate implementation, permissions, and system design.
