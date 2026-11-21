---
name: scroll-driven-3d-storytelling
description: "Use when a request needs scroll-linked 3D narrative."
triggers:
  - "scroll 3d"
  - "web interaktif 3d"
out_of_scope: "General motion design or marketing strategy"
escalation: "Hand off work involving General motion design or marketing strategy to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# Scroll-Driven 3D Storytelling

## Purpose

Create brand and product websites where scrolling controls a cinematic journey through connected scenes. The skill covers story design, art direction, scene production, camera continuity, video optimization, frontend integration, and QA.

## Core concepts

- **Narrative journey:** arrange scenes around the customer's journey, product value chain, or brand story.
- **Scene cohesion:** keep a consistent art direction, palette, lighting, scale, and visual language.
- **Camera grammar:** choose a continuous forward walkthrough, a fly-through with scene reveals, or a locked-angle glide according to the subject.
- **Scroll scrubbing:** map scroll progress to video time or scene progress, with deterministic seeking and responsive fallbacks.
- **Continuity:** plan transitions before rendering. For frame-locked chains, connector start and end frames must match adjacent clips.
- **Progressive delivery:** provide posters, lazy loading, reduced-motion behavior, mobile layouts, and a non-cinematic fallback.

## Workflow

1. Discover the brand, audience, conversion goal, content, available assets, and technical constraints.
2. Build a storyboard of roughly 4–7 scenes, each with a purpose, headline, supporting copy, and visual description.
3. Select visual style, camera behavior, aspect ratios, and a production budget.
4. Create scene stills with a shared style specification; review cohesion before video generation.
5. Produce camera clips and transitions using a consistent model and rendering configuration where possible.
6. Inspect transition frames, timing, encoding, file size, and visual continuity.
7. Integrate a scroll-controlled playback engine into the existing framework without assuming a framework in advance.
8. Test desktop, mobile, touch, keyboard, reduced-motion, loading, resize, and low-performance behavior.
9. Measure performance and conversion; revise scenes based on evidence.

## Technical considerations

- Treat generated video and image services as external dependencies with changing models, pricing, quotas, and CLI interfaces. Verify current capabilities and prices before production.
- Estimate costs from actual test generations rather than relying only on historical estimates.
- Avoid blocking the main thread during video seeking; coalesce rapid scroll updates and preload the next required segment.
- Use poster frames and graceful fallbacks when video decoding or autoplay is unavailable.
- Make mobile composition intentional; a portrait render is not equivalent to cropping a landscape composition.
- Keep all user-owned assets and credentials in their intended local or secure storage locations.

## Quality checks

- The story makes sense without animation.
- Camera movement supports the content rather than distracting from it.
- Transitions do not visibly jump or flash.
- Text remains readable and key calls to action remain accessible.
- Reduced-motion and low-bandwidth users receive a usable experience.
- The page remains responsive and does not create excessive GPU, memory, or network load.

## Source and attribution

Adapted as an original knowledge synthesis from the workflow concepts in [oso95/scroll-world](https://github.com/oso95/scroll-world), licensed MIT. The upstream skill uses Higgsfield and Monid; this document describes transferable methods and does not bundle their tools, credentials, assets, or proprietary services. Retain upstream attribution when redistributing copied or adapted portions under MIT.
