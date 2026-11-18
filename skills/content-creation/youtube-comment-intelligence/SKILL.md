---
name: youtube-comment-intelligence
title: YouTube Comment Intelligence
category: content-creation
source_type: original_operational_framework
language: Indonesian
description: "Use when a request needs comment triage and creator-voice replies."
triggers:
  - "komentar"
  - "balas komen"
  - "comments"
out_of_scope: "Broader PR ownership or unapproved moderation actions"
escalation: "Hand off work involving Broader PR ownership or unapproved moderation actions to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# YouTube Comment Intelligence

## Purpose
Turn a comment section into a prioritized community-response and audience-learning workflow. Own comment triage and response recommendations, not moderation actions or the overall brand reputation strategy.

## Inputs
Comment thread/export, video topic, creator voice, channel policies, and timing/context when known.

## Triage
Classify comments into:
- Genuine questions: answer accurately and capture recurring questions as content ideas.
- Corrections: verify the claim; acknowledge valid corrections plainly.
- Constructive criticism: identify the specific issue and respond proportionately.
- Praise: respond selectively and specifically; avoid repetitive boilerplate.
- Discussion/conversation: join when it adds value.
- Spam, harassment, or bait: recommend ignore, hide, report, or boundary-setting according to platform policy and user approval.

## Workflow
1. Identify recurring questions, misconceptions, and themes.
2. Separate factual corrections from opinion and abuse.
3. Draft concise replies in the creator's voice.
4. Recommend one comment to pin only when a clear community benefit exists.
5. Extract content ideas from repeated questions or unresolved needs.
6. Flag safety, privacy, legal, or reputation concerns for the appropriate owner.

## Output
Counts by category, priority queue, proposed replies, comments best left unanswered, optional pin recommendation, and content insights.

## Decision rules
- Never invent expertise, sources, or promises.
- Do not argue when facts are unverified.
- Do not reveal private information or encourage dogpiling.
- Never post, pin, delete, hide, or report without explicit authorization and a supported action.
- Keep replies natural and specific, not automated-sounding.

## Ownership boundary
This skill owns comment triage and draft replies. **Communication Decision Engine** chooses communication approach when needed; **Brand Communication & PR** handles broader public reputation messaging; **Viral Content Engineering** owns general engagement design. Follow [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md).
