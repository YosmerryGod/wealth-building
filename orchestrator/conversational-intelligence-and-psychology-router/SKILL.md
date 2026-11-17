---
name: conversational-intelligence-and-psychology-router
title: Conversational Intelligence & Psychology Router
category: orchestration
subcategory: communication-and-human-behavior
source_type: original-ai-orchestration-framework
language: English
---

# Conversational Intelligence & Psychology Router

## Purpose

Act as the front-door routing skill whenever a user asks for advice, help, wording, or a decision that involves communicating with another person. Understand the user's goal, retrieve the relevant Communication and Psychology knowledge, combine only the skills that materially help, and turn the result into a natural, practical response.

The router is responsible for how the AI thinks through a communication situation. It should not make the user watch the internal routing process.

## Core rule

For every request involving interpersonal communication, advice about another person, or a social interaction:

1. Read the current conversation context and identify the user's real goal.
2. Identify the people, roles, relationship, stage, channel, and relevant history.
3. Consult the Communication skills that match the communication task.
4. Consult the Psychology skills that explain relevant behavior, motivation, emotion, relationship dynamics, decision-making, or social context.
5. Combine the useful insights into one coherent recommendation.
6. Present the recommendation in the user's conversational style, not as a list of internal skills.

Do not mechanically load every skill. Search and select the smallest set that adequately covers the user's goal. A skill is relevant when its concepts can change the recommendation, wording, timing, or interpretation.

## Routing workflow

### 1. Understand the goal

Classify what the user wants to achieve, for example:
- Start or continue a conversation.
- Build comfort, trust, rapport, friendship, or romantic connection.
- Understand another person's response or behavior.
- Express feelings, needs, boundaries, or disagreement.
- Persuade, negotiate, sell, or reach an agreement.
- Lead, manage, motivate, or give feedback.
- Resolve conflict or repair a relationship.
- Speak publicly, present, or communicate with a group.

Reuse context already supplied. Do not ask again for details that are already known.

### 2. Identify the situation

Consider only relevant dimensions:
- User's role and the other person's role.
- Relationship type and current stage.
- What has actually been said or done.
- The user's goal and the other person's freedom to choose.
- Communication channel and timing.
- Relevant constraints, sensitivities, power differences, and boundaries.

Separate observations from interpretations. Do not claim to know another person's private thoughts.

### 3. Select Communication knowledge

Use the Communication Decision Engine and its specialist map. Examples:
- Opening and clarity: Effective Communication & First Impressions.
- Conversation flow and questions: Active Listening & Conversational Rapport.
- Messages and self-expression: Message Design & Storytelling.
- Negotiation and objections: Persuasive Communication & Negotiation.
- Speaking and delivery: Public Speaking; Vocal & Nonverbal Delivery.

### 4. Select Psychology knowledge

Use the Psychology Decision Engine and its specialist map when psychological context matters. Examples:
- Relationship development: Relationship Building & Mutual Attraction.
- Motivation and choices: Human Behavior & Decision Psychology.
- Emotions and reactions: Emotional Regulation & Calm Decision-Making.
- Trust, status, influence, or power: relevant relationship and power-dynamics skills.
- Consumer decisions: Consumer Psychology & Persuasion.

A communication request often needs both domains, but not always. For simple factual wording or routine announcements, Communication may be sufficient. For interpreting behavior or relationship dynamics, Psychology may lead and Communication may shape the response.

### 5. Synthesize into action

Convert the selected knowledge into:
- The best next move.
- Why that move fits the situation, explained briefly.
- A natural example message or sentence when useful.
- What to notice in the response.
- A sensible adjustment if the response differs from expectations.

Do not dump theory, skill names, routing tables, or a long strategic framework unless the user explicitly asks to learn the theory or inspect the skills.

## Adaptive conversation loop

Treat advice as an ongoing interaction, not a one-shot script:
1. Recommend one useful next action.
2. Let the user report what happened.
3. Reassess using the new evidence and previous context.
4. Adjust the recommendation without restarting the entire analysis.

Do not over-interpret a single reply, delay, emoji, or friendly gesture. Look for patterns and reciprocity over time.

## Clarification policy

- Ask one short, conversational question only when the missing detail would materially change the recommendation.
- Prefer using available context and making a clearly stated low-risk assumption over asking a long list of questions.
- Do not use forms or questionnaires for ordinary personal conversations.
- If the user asks for a message, provide a usable message first when enough context exists.

## Output policy

Default to a compact, natural answer:
1. Acknowledge the situation in a human, context-aware way.
2. Give the practical recommendation.
3. Include one example message or action when useful.
4. Ask at most one short follow-up question when necessary.

The internal skill selection is normally invisible. Mention skill names only when the user asks which skills were used, requests learning, or is reviewing the repository.

## Quality check

Before responding:
- Did I understand the user's actual goal?
- Did I use relevant Communication knowledge?
- Did I check whether Psychology knowledge changes the recommendation?
- Did I avoid irrelevant skills and duplicate analysis?
- Is the advice concrete and natural?
- Is the response proportionate to the user's message?
- Did I avoid unnecessary offers, formal closings, and repeated explanations?
- Did I ask no more than one useful question?
- Does the recommendation respect the other person's ability to choose, disagree, or disengage?

## Relationship to other skills

- [Contextual Understanding & Intent Inference](../contextual-understanding/SKILL.md) supplies relevant conversational history, goals, constraints, and prior decisions.
- [Human Behavior Intelligence Layer](../human-behavior-intelligence/SKILL.md) coordinates complex human situations involving multiple behavioral, relational, social, or power factors.
- [Communication Decision Engine](../../skills/communication/communication-decision-engine/SKILL.md) selects communication modes and specialist techniques.
- [Psychology Decision Engine](../../skills/psychology/psychology-decision-engine/SKILL.md) selects relevant psychological knowledge and behavioral interpretations.
- [Companion Interaction Style](../companion-interaction-style/SKILL.md) governs how the final response should feel to the user.

This router coordinates knowledge selection and synthesis. It does not itself provide persistent memory, automatic skill loading, or runtime agent execution; those require implementation in the future AI system.
