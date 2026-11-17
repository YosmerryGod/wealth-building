---
name: audience-retention-intelligence
title: Audience Retention Intelligence
category: content-creation
source_type: original_operational_framework
language: Indonesian
---

# Audience Retention Intelligence

## Purpose
Analyze YouTube audience-retention data to locate where viewers leave, rewatch, or remain engaged, then connect those patterns to the content and propose one prioritized improvement. This skill owns observed retention diagnosis, not script drafting or edit execution.

## Inputs
- Retention export or chart, video duration, and publication context.
- Timestamped transcript when available.
- Traffic source and audience mix when available.
- Video format and any known changes made after publication.

## Workflow
1. Validate data coverage, duration, sampling, and whether the export belongs to the stated video.
2. Describe the opening curve, notable drops, gradual decline, spikes/rewatches, and ending behavior.
3. Use transcript timestamps to identify what was being said at relevant moments; do not infer without transcript or footage.
4. Classify likely issue as promise mismatch, slow setup, unclear transition, pacing, repetition, interruption, or unknown.
5. Compare with similar videos or channel baseline only when comparable data exists.
6. Select one highest-priority change and define how to test it in the next video.

## Output
- Data quality and limitations.
- Key timestamps and retention observations.
- Transcript/context explanation where supported.
- One prioritized diagnosis, confidence, and proposed change.
- Additional issues only if requested.

## Decision rules
- Do not use universal retention thresholds as laws; benchmark against format, length, source, and channel history.
- Distinguish correlation from cause.
- A drop does not prove a specific edit or line caused it.
- Do not recommend rewriting a healthy hook when the main issue is elsewhere.
- If data is absent, request it or provide a diagnostic checklist rather than inventing metrics.

## Ownership boundary
This skill owns retention-data interpretation. **Video Scriptwriting & Hook Engineering** owns prospective script structure; **Transcript-Based Video Editing** owns transcript-based cut recommendations; **Title & Thumbnail Packaging Optimization** handles packaging when click-through is the diagnosed issue. Follow [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md).
