---
name: content-intelligence-orchestrator
title: Content Intelligence Orchestrator
category: orchestration
source_type: original_repository_architecture
language: Indonesian
---

# Content Intelligence Orchestrator

## Purpose
Route creator and YouTube-related requests to the smallest sufficient set of Content Creation skills. Own task classification, specialist selection, handoffs, and final synthesis—not the specialist methods themselves.

## Entry conditions
Use for YouTube/channel growth, video planning, scriptwriting, packaging, editing from transcripts, retention analysis, Shorts repurposing, comment analysis, SEO metadata, chapters, competitor research, or channel audits. For unrelated marketing or general business growth, use the existing Marketing/Growth routing instead.

## Routing registry

| User need | Lead specialist | Optional supporting specialist |
|---|---|---|
| Write a video script or hook | Video Scriptwriting & Hook Engineering | Title & Thumbnail Packaging Optimization |
| Improve title and thumbnail | Title & Thumbnail Packaging Optimization | Video Scriptwriting & Hook Engineering |
| Analyze transcript for cuts | Transcript-Based Video Editing | Short-Form Video Repurposing |
| Diagnose audience drop-off | Audience Retention Intelligence | Transcript-Based Video Editing; Video Scriptwriting & Hook Engineering |
| Turn long video into Shorts | Short-Form Video Repurposing | Video Scriptwriting & Hook Engineering |
| Triage comments and draft replies | YouTube Comment Intelligence | Communication Decision Engine when communication stakes require it |
| Plan a content week/month | Content Calendar & Production Planning | YouTube Competitor & Viral Intelligence; Growth Metrics & Optimization |
| Write search-facing metadata | YouTube SEO & Search Intent | Title & Thumbnail Packaging Optimization |
| Generate chapters | YouTube Chapter & Timestamp Engineering | YouTube SEO & Search Intent |
| Research niche and competitor videos | YouTube Competitor & Viral Intelligence | Viral Content Engineering when interpreting broader attention principles |
| Audit a channel | YouTube Channel Audit & Optimization | Only specialists needed for the diagnosed bottleneck |

## Routing procedure
1. Identify the user's actual outcome and the asset/data they supplied.
2. Retrieve relevant creator context and voice profile only when available and relevant. Do not invent a persistent file or claim to have read one.
3. Choose one lead specialist. Add another only when its output can materially change the result.
4. Check input sufficiency. Ask one focused question if an essential input is missing; otherwise proceed and label limitations.
5. Pass a compact handoff: objective, audience, platform, source asset/data, constraints, evidence, and requested output.
6. Receive bounded specialist findings. Do not ask every skill to repeat the same analysis.
7. Synthesize one recommendation and clearly separate verified observations, estimates, and hypotheses.
8. Ask for approval before publishing, scheduling, replying, pinning, deleting, or taking any externally visible action.

## Shared quality and safety rules
- Preserve the creator's actual voice; do not force a generic viral tone.
- Never fabricate analytics, sources, comments, timestamps, search volume, or performance outcomes.
- Treat scoring rubrics as editorial heuristics, not predictors of success.
- Use public competitor information only and respect platform terms.
- Do not use misleading clickbait, fake scarcity, fake engagement, harassment, or manipulative outrage.
- Protect privacy and rights in source footage, music, images, and comments.
- A skill file does not itself provide YouTube API access, data collection, file processing, persistent memory, scheduling, or publishing.
- Do not claim to have executed a Python tool or edited media unless the capability was actually available and used.
- Keep the user in control of public actions.

## Handoff packet
- Goal and success measure.
- Audience, niche, language, and platform.
- Creator voice and content constraints.
- Source asset or dataset and its provenance/date.
- Known facts, assumptions, and missing evidence.
- Specialist output requested.
- Approval required before any external action.

## Relationship to existing repository skills
- **Viral Content Engineering & Attention Psychology** owns general cross-platform attention, hook principles, shareability, and reputation-aware iteration. The YouTube Script and Packaging skills own their specific video deliverables.
- **Digital Brand Awareness & Channel Strategy** owns cross-platform digital presence and channel roles. This orchestrator owns YouTube-specific production task routing.
- **Traction Strategy**, **Traction Channel Selection**, and **Bullseye Framework** own business acquisition channel strategy and testing; they are not replaced by content scheduling.
- **Growth Metrics & Optimization** owns general growth metric definitions and scorecard interpretation. Audience Retention Intelligence owns the YouTube-specific interpretation of retention curves.
- **Communication Decision Engine** owns communication approach where the comment interaction requires broader communication judgment. YouTube Comment Intelligence owns comment triage and creator-voice reply drafts.

## Governance
Follow [Skill Boundary & Routing Governance](../skill-boundary-governance/SKILL.md). The orchestrator is the single synthesis owner for YouTube/content-creation requests. It must not override specialist expertise, duplicate specialist analysis, or route simple requests through unrelated skills.
