---
name: short-form-video-repurposing
title: Short-Form Video Repurposing
category: content-creation
source_type: original_operational_framework
language: Indonesian
description: "Use when a request needs select and adapt moments from long video into shorts."
triggers:
  - "shorts"
  - "reels"
  - "potong video"
  - "repurpose"
out_of_scope: "Detailed transcript edit lists or general content strategy"
escalation: "Hand off work involving Detailed transcript edit lists or general content strategy to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# Short-Form Video Repurposing

## Purpose
Find self-contained moments in long-form content that can stand as Shorts or other short-form clips, then adapt their opening and framing to the new audience context.

## Inputs
Long-form video transcript with timestamps, source video aspect ratio, target platform, audience, and any footage restrictions.

## Workflow
1. Find candidate spans that make sense without surrounding context.
2. Prefer moments with a clear claim, demonstration, story turn, useful answer, or complete emotional beat.
3. Reject clips that depend on an earlier explanation or end before delivering a point.
4. Rank candidates by standalone clarity, audience relevance, value, visual potential, and edit effort.
5. Write a new opening line when the original assumes long-form context.
6. Specify on-screen text, crop/reframing notes, captions, and a natural ending or loop only when appropriate.
7. Verify every suggested timecode against the source before editing.

## Output
Top candidate clips with start/end timecodes, standalone premise, original opening, proposed new opening, visual/crop notes, and reason for selection.

## Decision rules
- Do not assume every viral-looking sentence makes a good Short.
- Preserve the original meaning; do not remove context in a way that changes the claim.
- Do not fabricate footage or imply a visual exists when it has not been inspected.
- Respect platform format, copyright, privacy, and creator permissions.
- Treat performance as uncertain and measure each format separately.

## Ownership boundary
This skill owns clip selection and short-form adaptation. **Transcript-Based Video Editing** owns detailed transcript cut lists; **Video Scriptwriting & Hook Engineering** owns standalone script creation; **Viral Content Engineering & Attention Psychology** provides broader attention principles. Follow [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md).
