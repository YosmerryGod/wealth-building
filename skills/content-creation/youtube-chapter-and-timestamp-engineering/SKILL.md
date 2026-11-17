---
name: youtube-chapter-and-timestamp-engineering
title: YouTube Chapter & Timestamp Engineering
category: content-creation
source_type: original_operational_framework
language: Indonesian
---

# YouTube Chapter & Timestamp Engineering

## Purpose
Create useful, accurate chapter timestamps from a transcript or verified timeline so viewers can navigate a video. Own chapter structure and validation, not retention diagnosis.

## Inputs
Timestamped transcript or source timeline, video duration, language, topic structure, and current platform chapter requirements.

## Workflow
1. Validate timestamp format, sequence, and video duration.
2. Identify meaningful topic boundaries, not every pause or sentence.
3. Draft concise, descriptive chapter names in the creator's voice.
4. Confirm the first timestamp and minimum chapter count/duration against current YouTube rules.
5. Check that every timestamp maps to the actual video and does not exceed its duration.
6. Review whether chapter names accurately represent each section and help viewers decide where to go.

## Output
Chronological timestamp list, chapter labels, validation results, and any timestamps requiring manual verification.

## Decision rules
- Never invent timestamps from an un-timestamped transcript.
- Do not use vague or keyword-stuffed chapter labels.
- Validate against current platform rules; do not hardcode rules as permanent.
- A chapter boundary is an editorial judgment, not proof of a retention drop.

## Ownership boundary
This skill owns chapter/timestamp generation and validation. **Audience Retention Intelligence** owns analytics diagnosis; **YouTube SEO & Search Intent** may place validated chapters in a description but does not create them. Follow [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md).
