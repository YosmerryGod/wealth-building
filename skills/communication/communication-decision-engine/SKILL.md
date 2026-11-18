---
name: communication-decision-engine
title: Communication Decision Engine
category: communication
subcategory: orchestration
source_type: AI-operational-orchestration-framework
language: English
description: "Use when a request needs chooses communication mode, channel, and specialists."
triggers:
  - "presentasi"
  - "negosiasi"
  - "komunikasi"
  - "pesan penting"
out_of_scope: "Psychology ownership or domain response-mode selection"
escalation: "Hand off work involving Psychology ownership or domain response-mode selection to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# Communication Decision Engine

## Purpose

Act as the routing and decision layer for the Communication domain. Understand the communication situation, identify the user's goal and role, assess the audience and relationship context, select the smallest useful set of Communication skills, and produce an actionable approach.

This engine coordinates specialist skills. It does not replace them and does not force every situation into a fixed script.

## Context continuity

Use [Contextual Understanding & Intent Inference](../../../orchestrator/contextual-understanding/SKILL.md) to interpret short follow-ups and reuse relevant prior messages, audience details, roles, communication goals, channel choices, constraints, and approved wording. Do not restart intake or ask the user to repeat context already available. Preserve unchanged constraints when the user changes only one part of the request. Ask one focused clarification only when the missing detail materially changes the communication outcome. For complex human situations, use the context packet prepared by the Human Behavior Intelligence Layer.

## Context-aware response strategy integration

For requests that combine situation reading, psychology, communication, and possible marketing or service recovery, consult [Context-Aware Response Strategy Engine](../../../orchestrator/context-aware-response-strategy-engine/SKILL.md) first. It selects the appropriate response strategy from the full context; this Communication engine remains responsible for designing the practical wording, listening, negotiation, feedback, and delivery. Do not assume every interaction requires persuasion, marketing, apology, or compensation.

## Psychology integration and natural response

For interpersonal communication requests, check whether relevant Psychology knowledge changes the recommended approach. Use the [Psychology Decision Engine](../../psychology/psychology-decision-engine/SKILL.md) and its specialist map when behavior, motivation, emotion, trust, relationship stage, social context, or power dynamics matter. Select only the relevant skills; do not mechanically load the whole Psychology domain.

The final answer should follow [Companion Interaction Style](../../../orchestrator/companion-interaction-style/SKILL.md): lead with useful practical advice, explain the psychological or communication principle briefly when it helps, and keep internal skill routing invisible unless the user asks to inspect it. Ask one short question at most when a missing detail materially changes the next step. Do not turn casual advice into a formal report or end every response with an offer.

## Core operating principles

1. Start with the user's actual communication goal and the situation, not a favorite technique.
2. Identify who is communicating, to whom, through which channel, and under what circumstances.
3. Identify the user's role and the other person's role; do not assume the user is always the leader, subordinate, customer, persuader, or person in the right.
4. Separate observable facts, the user's interpretation, possible explanations, and unknown information.
5. Select only the specialist skills needed for the task. Combine skills when the situation genuinely spans multiple capabilities.
6. Adapt language, formality, directness, length, pace, and delivery to the audience and channel while preserving the user's authentic intent.
7. Optimize for mutual understanding and the legitimate outcome, not merely for sounding impressive or obtaining agreement.
8. Explain the reason for the recommended approach and identify what response or evidence should guide the next step.
9. Reassess when the user supplies new context or reports the outcome.

## Situation intake

Identify the relevant dimensions:

### 1. User role

Possible roles include:
- Owner, founder, or entrepreneur
- Executive, manager, supervisor, or team lead
- Employee, subordinate, or job applicant
- Coworker, peer, or collaborator
- Seller, service provider, or negotiator
- Customer, client, or buyer
- Speaker, presenter, trainer, or facilitator
- Friend, family member, acquaintance, or romantic partner
- Community member, creator, or public representative

Roles can overlap and may change during the interaction. A role is context, not proof of authority, credibility, or intent.

### 2. Audience and relationship

Identify:
- One person, a small group, or a public audience
- New contact, existing relationship, or established professional relationship
- Familiarity and prior interaction
- Relevant authority, dependency, expertise, or status differences
- Audience knowledge, likely concerns, and communication needs
- Cultural, language, accessibility, and channel considerations when known

Do not infer private motives or personality traits from sparse signals.

### 3. Communication goal

Classify the primary goal:

- **Inform:** explain facts, updates, instructions, or decisions.
- **Understand:** listen, ask questions, clarify needs, or learn another perspective.
- **Connect:** begin a conversation, build rapport, or maintain a relationship.
- **Present:** teach, pitch, explain, or speak to an audience.
- **Persuade:** make a case and support an informed decision.
- **Negotiate:** reconcile interests, terms, constraints, and alternatives.
- **Resolve:** address disagreement, misunderstanding, complaint, or conflict.
- **Coordinate:** align responsibilities, expectations, timelines, and next steps.
- **Represent:** communicate publicly on behalf of a person, team, or organization.

If the goal is unclear and materially changes the recommendation, ask one focused question.

### 4. Channel and constraints

Account for:
- Face-to-face conversation
- Phone or voice call
- Video meeting
- Email or formal letter
- Chat or direct message
- Social media reply or public post
- Presentation, speech, interview, or group discussion

Also identify time limits, message length, language, privacy, urgency, and whether a written record is important.

## Skill selection and routing

Use this routing map as a starting point, not as rigid keyword matching.

| Situation or need | Primary skill | Add when relevant |
|---|---|---|
| General clarity, first contact, audience fit | Effective Communication & First Impressions | Active Listening; Message Design |
| Understand someone, ask questions, sustain dialogue | Active Listening & Conversational Rapport | Effective Communication; Relationship Building |
| Build social or professional connections | Active Listening & Conversational Rapport | Relationship Building & Mutual Attraction; Effective Communication |
| Make a proposal, handle objections, seek agreement | Persuasive Communication & Negotiation | Active Listening; Message Design |
| Resolve a disagreement or complaint | Active Listening & Conversational Rapport | Persuasive Communication & Negotiation; Effective Communication |
| Prepare a written explanation, pitch, story, or introduction | Message Design & Storytelling | Effective Communication; Persuasive Communication |
| Deliver a speech, presentation, or live explanation | Public Speaking & Speaking Confidence | Message Design; Vocal & Nonverbal Delivery |
| Improve voice, posture, gesture, or delivery | Vocal & Nonverbal Delivery | Public Speaking; Effective Communication |
| Communicate across hierarchy or workplace roles | Effective Communication & First Impressions | Active Listening; Persuasive Communication & Negotiation |
| Communicate with customers or market audiences | Effective Communication & First Impressions | Persuasive Communication; Message Design; relevant Marketing skills |
| Maintain personal or romantic relationships | Active Listening & Conversational Rapport | Relationship Building & Mutual Attraction; Emotional Regulation when relevant |

### Specialist skill references

- [Effective Communication & First Impressions](../effective-communication-and-first-impressions/SKILL.md)
- [Active Listening & Conversational Rapport](../active-listening-and-conversational-rapport/SKILL.md)
- [Persuasive Communication & Negotiation](../persuasive-communication-and-negotiation/SKILL.md)
- [Message Design & Storytelling](../message-design-and-storytelling/SKILL.md)
- [Vocal & Nonverbal Delivery](../vocal-and-nonverbal-delivery/SKILL.md)
- [Public Speaking & Speaking Confidence](../public-speaking-and-speaking-confidence/SKILL.md)
- Related Psychology skill: [Relationship Building & Mutual Attraction](../../psychology/relationship-building-and-mutual-attraction/SKILL.md)
- For workplace power, coercion, or manipulation analysis, consult the relevant Psychology skills and the repository's Risk Assessment & Consequence Intelligence layer where the requested action has material consequences.

## Decision workflow

### Step 1 — Define the outcome

Write one sentence describing what a successful communication outcome would look like. Distinguish the user's desired outcome from what the other person is free to decide.

### Step 2 — Map the situation

Record only relevant facts:
- User's role and responsibility
- Other party's role and relationship
- Communication goal
- Channel and setting
- Prior messages or events
- Constraints and known sensitivities
- What is known versus inferred

### Step 3 — Choose the communication mode

Select the dominant mode:
- Listen and understand
- Explain and inform
- Connect and build rapport
- Present and teach
- Persuade and negotiate
- Resolve and coordinate

Some situations require a sequence, such as listening first, clarifying the issue, then making a proposal.

### Step 4 — Select specialist skills

Choose the smallest sufficient combination. Usually one primary skill and zero to two supporting skills are enough. Add more only when the situation clearly requires them.

### Step 5 — Design the approach

Specify:
- Opening or first move
- Main message or question
- Supporting reason, evidence, or example
- Tone and level of directness
- Appropriate length and channel
- How to invite a response or confirm understanding
- What should happen if the response differs from expectations

### Step 6 — Produce the practical output

Depending on the request, provide:
- A ready-to-send message
- A conversation outline
- A presentation structure or speaking notes
- A negotiation plan
- Questions for discovery or listening
- A conflict-resolution sequence
- A practice exercise or feedback checklist

Use the user's requested language and voice. Do not make a simple request unnecessarily elaborate.

### Step 7 — Review and adapt

After the interaction, assess:
- Was the central message understood?
- Did both sides have a fair chance to speak?
- Was the intended outcome achieved?
- What response or evidence was observed?
- Was there a misunderstanding, unmet need, or constraint?
- What should change next time?

Do not treat one reply, silence, an emoji, eye contact, or a single gesture as conclusive evidence of intent.

## Role-specific application

### Leader or manager

Prioritize clear expectations, context, feedback, listening, decision rationale, and accountability. Distinguish instructions from suggestions and make responsibilities and deadlines explicit.

### Employee or subordinate

Prioritize accurate updates, respectful upward communication, clarification of priorities, evidence-based disagreement, and early escalation of blockers. Do not confuse respectful communication with automatic agreement.

### Peer or coworker

Prioritize shared goals, role clarity, coordination, direct clarification, and timely feedback. Avoid triangulation when a direct and safe conversation is appropriate.

### Owner, seller, or service provider

Understand customer needs before presenting an offer. Explain value, price, terms, limitations, and next steps clearly. Use persuasion and negotiation to support informed decisions, not to hide material facts.

### Customer or client

Clarify the desired outcome, describe the problem and relevant facts, ask about options, and confirm commitments in writing when useful.

### Presenter or public speaker

Adapt structure and delivery to the audience, purpose, time, and venue. Use Public Speaking, Message Design, and Vocal & Nonverbal skills together when needed.

### Friend, family member, or partner

Prioritize listening, emotional context, clear needs, mutual respect, and appropriate boundaries. Do not convert every personal conversation into a persuasion exercise.

## Output format

For a meaningful or complex request, respond with:

1. **Situation:** brief description of roles, relationship, channel, and goal.
2. **Recommended mode:** listen, inform, connect, present, persuade, negotiate, resolve, or coordinate.
3. **Selected skills:** primary and supporting skills, with a short reason for each.
4. **Approach:** practical steps and the reasoning behind them.
5. **Example:** wording, questions, outline, or delivery guidance when requested or useful.
6. **What to watch:** signs of understanding, confusion, agreement, objection, or boundary.
7. **Next adjustment:** how to respond to the likely outcomes.

For simple tasks, answer directly and omit sections that add no value.

## Interaction rules

- Ask one focused clarification only when a missing detail would materially change the response.
- Do not ask the user to repeat context already present in the conversation or project.
- If the user provides an exact message or transcript, analyze that material rather than inventing missing dialogue.
- If asked to draft, produce a complete usable draft in the requested tone and language.
- If the user asks for analysis, distinguish observed wording from interpretation.
- If the user asks for learning, explain the underlying communication principle and give a practice example.
- Do not force a form, checklist, or framework onto casual, low-stakes exchanges.
- Do not assume every interaction requires persuasion or strategic influence.
- Preserve the user's agency and the other person's ability to disagree, decline, or disengage.

## Source and evidence boundaries

This is an original AI orchestration framework that routes to the repository's Communication specialist skills. It is not a direct adaptation of one book and does not claim to reproduce the complete contents of any cited book.

The Communication specialists currently include book-inspired operational syntheses drawing on *Bicara Itu Ada Seninya* by Oh Su Hyang and public catalogue descriptions of:
- *Cara Mudah & Praktis Belajar Public Speaking* by Mulasih Tary and Devi Ardiyanti
- *Rahasia Lancar Berkomunikasi* by Mulasih Tary and Devi Ardiyanti
- *Seni Membangun Relasi* by Devi Ardiyanti

Public catalogue descriptions are not equivalent to access to complete book texts. Keep source-derived themes distinct from AI-generated routing logic and additional interpretation.

## Relationship to other orchestration skills

- **Psychology Decision Engine:** analyzes behavior, relationship patterns, emotional dynamics, incentives, and power differences. Consult it when these factors materially affect the communication recommendation. This Communication engine remains responsible for turning that context into a practical communication approach.
- **Joint workflow:** first identify the primary problem. If the user mainly needs wording, listening, presentation, negotiation, or delivery, lead with Communication and consult Psychology only for meaningful behavioral or relationship context. If the user mainly needs to interpret repeated behavior, motives, conflict patterns, emotional reactions, or power dynamics, lead with Psychology and consult Communication when a concrete conversation or message is needed.
- **Information handoff:** pass only relevant context between engines: roles, relationship, observed facts, stated goal, channel, constraints, hypotheses with uncertainty, and the practical decision still needed. Do not repeat the full analysis or duplicate specialist advice.
- **Avoid unnecessary routing:** ordinary low-stakes communication does not need a Psychology analysis. A psychological topic does not automatically require a communication script. Use both only when each contributes a distinct result.
- **Sequence:** Psychology may explain what dynamics could be occurring; Communication then designs how to listen, clarify, express, negotiate, or set expectations. New evidence from the interaction can return to Psychology for reassessment.
- **Business Agent Orchestrator:** coordinates business lifecycle work. During customer research, sales, negotiation, team management, and marketing preparation, it can delegate communication-specific decisions to this engine.
- **Risk Assessment & Consequence Intelligence:** evaluates material risks and consequences of a proposed action. It does not replace communication expertise or suppress analysis of difficult topics.

## Success criteria

The engine succeeds when it:
- Selects an appropriate communication approach for the actual situation.
- Uses only the specialist skills needed.
- Produces clear, context-sensitive, usable guidance.
- Explains the rationale without overexplaining.
- Adapts to evidence and feedback.
- Improves mutual understanding while respecting the choices and boundaries of everyone involved.

## Ownership and routing boundary

Follow the canonical [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md). This engine owns communication approach, channel, structure, and selection of Communication specialists. Context-Aware Response Strategy owns the decision about what kind of response is appropriate; Psychology Decision Engine owns psychology specialist selection. Accept their handoff when present and do not repeat situation analysis. Message Design owns message structure; Persuasive Communication owns ethical persuasion/negotiation; Active Listening owns listening/rapport; Public Speaking and Vocal/Nonverbal Delivery own live delivery. Use only those that materially improve the outcome.

## Ownership and routing boundary

Follow the canonical [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md). This engine owns communication approach, channel, structure, and selection of Communication specialists. Context-Aware Response Strategy owns the decision about what kind of response is appropriate; Psychology Decision Engine owns psychology specialist selection. Accept their handoff when present and do not repeat situation analysis. Message Design owns message structure; Persuasive Communication owns ethical persuasion/negotiation; Active Listening owns listening/rapport; Public Speaking and Vocal/Nonverbal Delivery own live delivery. Use only those that materially improve the outcome.
