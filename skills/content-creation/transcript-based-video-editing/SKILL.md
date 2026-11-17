---
name: transcript-based-video-editing
title: Transcript-Based Video Editing
category: content-creation
source_type: original_operational_framework
language: Indonesian
---

# Transcript-Based Video Editing

## Purpose
Turn a timestamped transcript into an editorial decision list that helps a human editor identify dead air, repeated takes, verbal filler, unclear passages, and structural opportunities. This skill analyzes transcript evidence; it does not directly edit or render media.

## Inputs
Timestamped SRT, VTT, or JSON transcript; target format and runtime; optional editing style and footage notes.

## Workflow
1. Confirm transcript format, timestamps, language, and whether timestamps align with source footage.
2. Identify long pauses, repeated phrases, false starts, filler that adds no meaning, and sections that repeat an earlier point.
3. Preserve meaningful pauses, demonstrations, emotional beats, and deliberate silence.
4. Identify missing context or transitions that may require a pickup line rather than a cut.
5. Produce a timecoded edit decision list with reason and confidence.
6. Flag every recommendation that must be checked against actual video/audio before editing.

## Output
- Timecoded KEEP / CUT / REVIEW recommendations.
- Reason and confidence for each segment.
- Estimated speech removed, clearly distinguished from total video runtime.
- Structural notes and pickup suggestions.
- Limitations caused by transcript-only analysis.

## Decision rules
- Never invent timecodes or infer visual events from transcript alone.
- Do not cut every pause; protect natural breathing and emphasis.
- Do not treat transcript word count as reliable final runtime when visuals or demonstrations are present.
- Human editor must verify recommendations against source media.

## Ownership boundary
This skill owns transcript-derived edit recommendations. **Audience Retention Intelligence** diagnoses viewer behavior from analytics; **Short-Form Repurposing** selects independent clips; neither should be substituted for transcript editing. Follow [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md).
