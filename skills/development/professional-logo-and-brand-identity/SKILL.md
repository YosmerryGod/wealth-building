---
name: professional-logo-and-brand-identity
description: "Use when a request needs logo and identity system design."
triggers:
  - "logo"
  - "identitas brand"
  - "favicon"
out_of_scope: "Product UI or trademark/legal clearance"
escalation: "Hand off work involving Product UI or trademark/legal clearance to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# Professional Logo & Brand Identity

## Purpose

Guide an AI design agent through a complete identity-design process, from understanding a brand to producing usable vector assets and a compact identity kit.

## Modes

- **Design:** create a new identity from a brief.
- **Critique:** evaluate an existing mark and explain strengths and weaknesses.
- **Redesign:** preserve useful brand equity while improving the identity.
- **System:** extend a mark into typography, color, lockups, patterns, and sub-brand rules.
- **Assets:** prepare favicon, app icon, social, monochrome, reversed, and export variants.

## Design workflow

1. **Discovery:** establish brand name, audience, category, positioning, personality, competitors, use cases, constraints, and required deliverables.
2. **Research:** inspect the competitive visual landscape and identify category conventions, opportunities, and visual clichés.
3. **Strategy:** define the core idea, desired associations, and criteria for judging concepts.
4. **Concepts:** explore materially different directions such as wordmark, monogram, letterform, pictorial, abstract, emblem, mascot, or combination mark.
5. **Vector construction:** build clean, editable SVG geometry. Start in monochrome so the concept does not depend on color effects.
6. **Refinement:** check optical balance, spacing, negative space, stroke consistency, and small-size legibility.
7. **Testing:** inspect at favicon size, in one color, reversed on dark backgrounds, at large scale, and in realistic brand contexts.
8. **Checkpoint:** present a small set of distinct concepts with rationale and trade-offs. Get the user's selection before building a full identity kit.
9. **Delivery:** create approved logo variants, SVG and raster exports, color and typography guidance, spacing rules, and usage examples.

## Evaluation criteria

- Distinctiveness and memorability
- Relevance to the brand without being overly literal
- Simplicity and scalability
- Legibility at small sizes
- Reproducibility in one color
- Suitability across digital and physical applications
- Consistency with the intended positioning

## Production standards

- Prefer clean SVG paths and explicit viewBox dimensions.
- Avoid unnecessary filters, embedded raster images, and fragile effects in core marks.
- Keep source files editable and exports organized.
- Verify rendering in more than one browser or SVG renderer when possible.
- Do not present generated concepts as trademark-cleared. Similarity searches and legal clearance are separate tasks.

## Source and attribution

Original knowledge synthesis based on the workflow in [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill), licensed MIT. The upstream repository includes scripts and a reference-logo collection; this skill does not copy those assets. The upstream project notes that its trademark reference materials have separate terms, so do not assume every referenced logo is reusable.
