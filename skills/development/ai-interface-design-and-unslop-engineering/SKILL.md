---
name: AI Interface Design & Unslop Engineering
title: AI Interface Design & Unslop Engineering
category: development
source_type: adapted-open-source-skill-and-operational-framework
source: Adapted from Unslop by Damir Sokolovsky (https://github.com/heydamir/unslop), licensed CC BY 4.0; additional framework and integration written for Wealth Building
language: English
---

# AI Interface Design & Unslop Engineering

## Attribution and license

This skill adapts ideas and workflow concepts from **Unslop**, created by **Damir Sokolovsky** ([@heydamir](https://x.com/heydamir), https://heydamir.design/unslop), available at https://github.com/heydamir/unslop.

The upstream skill declares the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. This adaptation retains attribution. The original repository and its complete reference files remain the authoritative source for the upstream implementation. This document is an independent adaptation and integration for the Wealth Building knowledge base; it is not an official Unslop release.

## Purpose

Help an AI agent design, audit, improve, and implement digital interfaces that feel intentionally art-directed and specific to the product rather than generic AI-generated templates.

The skill combines product understanding, visual direction, interface craft, implementation, and visual quality review. It applies to landing pages, SaaS products, dashboards, admin panels, mobile web applications, commerce interfaces, and other digital products.

The central idea is: **remove generic visual habits without removing the product's identity, useful content, or functionality.** A clean interface is not automatically a distinctive interface. The result should communicate what the product does, who it serves, and what makes its visual world appropriate.

## Core design principles

### 1. Product-specific direction

Design direction must come from the product, its audience, its tasks, and its content—not from whatever style is trending.

### 2. Quiet interface, meaningful focal points

Navigation, controls, labels, and supporting surfaces should help users understand and operate the product. Visual richness belongs where it communicates something meaningful: product content, a useful chart, a real object, a distinctive illustration, or a key result.

### 3. Deliberate visual hierarchy

Every screen should make clear what matters first, what supports it, and what can remain quiet. Color, scale, spacing, typography, composition, and motion should reinforce the same hierarchy.

### 4. Product identity over template familiarity

A design should not be interchangeable with another product after changing its logo and title. Its character, visual world, content, and signature details should belong to the product.

### 5. Preserve the product

When improving an existing screen, preserve its purpose, features, content, information architecture, and section order unless the user requests a product or UX change. Visual refinement is not permission to silently remove functionality.

## Recognizing generic AI-looking interface patterns

Audit the actual screen rather than assuming every item below is wrong. Common warning signs include:

- Purple-to-blue gradients used without a product-specific reason.
- Glow, neon borders, colored shadows, radial washes, glossy blobs, and decorative orbs competing with content.
- Emoji used as interface icons or repeated decoration.
- Generic badges such as "New ✨", "PRO", or "Beta 🚀" without a functional need.
- Excessive uppercase labels with wide letter spacing.
- Heavy typography and too many competing font weights.
- Arbitrary spacing, inconsistent alignment, and components that should match but do not.
- Repeated cards with identical structure even when their content has different importance.
- Generic hero copy, unsupported metrics, vague claims, and filler visuals.
- Decorative motion that loops without communicating state or helping a task.
- Dashboards compressed into narrow centered columns or landing pages built from the same centered stack regardless of product context.

These are diagnostic signals, not universal prohibitions. A gradient, glow, emoji, card, animation, or particular layout may be appropriate when the brand, content, accessibility, or interaction purpose supports it. Evaluate context and execution.

## Workflow

### Phase 1 — Inspect the real interface

1. Locate the files and components that render the requested screen.
2. Identify framework, routing, component system, styling conventions, design tokens, fonts, breakpoints, and theme behavior.
3. Run the product when possible and inspect the rendered interface at the target viewport.
4. Capture a baseline screenshot when screenshot tooling is available.
5. If only a live URL is supplied, use an approved project/browser workflow to inspect it; do not pretend to have inspected source code that was not provided.
6. If only a screenshot is supplied, distinguish a visual reconstruction from a modification of the real application.
7. Record the current features, content, section order, responsive behavior, and interaction states before editing.

### Phase 2 — Audit

Review the whole screen and record concrete observations with their locations. Inspect:

- Product clarity and visual direction.
- Spacing, alignment, density, and grouping.
- Color palette, contrast, and semantic color usage.
- Icon style and consistency.
- Copy quality and factual claims.
- Typography and hierarchy.
- Layout, composition, and responsive behavior.
- Component details, borders, radii, and data visualization.
- Images, illustrations, and product-specific content.
- Motion, transitions, feedback, and interaction states.
- Accessibility, keyboard operation, touch behavior, and reduced motion.
- Performance and implementation consistency.

For each finding, state what is visible, where it occurs, why it matters, and whether it should be changed. Do not label a design element as a defect merely because it differs from a preferred aesthetic.

### Phase 3 — Choose the scope

Classify the audit:

- **Substantial redesign:** widespread issues undermine hierarchy, consistency, or product identity. Plan a coordinated visual direction and full-screen pass.
- **Focused polish:** the screen already has a coherent identity. Fix the observed issues and preserve its existing direction.
- **No meaningful issue:** say so plainly. Offer only a few concrete refinements and do not alter a good screen merely to create visible activity.

When the requested scope or visual direction is ambiguous, present the audit and proposed direction and ask for confirmation before editing. Skip this pause when the user has clearly asked for direct implementation.

### Phase 4 — Define the visual direction

Write five concise statements before implementation:

1. **Product:** what it does and for whom, in one plain sentence.
2. **Character:** two or three concrete traits that describe its personality, such as precise, energetic, warm, technical, playful, or restrained. Avoid generic labels that could describe almost any product.
3. **World:** the product's natural context, material, environment, or metaphor. A finance tool may relate to instruments and ledgers; a delivery product to routes and movement; a developer tool to terminals and workbenches.
4. **Moments:** one or two content areas that deserve richer color, material, illustration, or visual detail because they communicate something important.
5. **Signature:** one recognizable detail that belongs to this product and can be used consistently without becoming decoration everywhere.

Keep an existing, legitimate brand identity when it is part of the product. Improve the interface around it rather than replacing it for novelty. If the user asks for a rebrand, treat that as a separate explicit scope.

### Phase 5 — Improve in deliberate passes

Complete each pass across the screen before moving to the next. Revisit earlier passes only when a later change reveals a real inconsistency.

#### Pass 1: Spacing and alignment

- Establish a consistent spacing scale and use it across related components.
- A 4px base grid is a useful starting system, not a universal law. Use values that fit the platform, typography, density, and existing design system.
- Keep equivalent rows, controls, and cards consistent where they serve equivalent roles.
- Use spacing to distinguish groups and hierarchy.
- Align labels, icons, numbers, and controls deliberately.
- Match padding to content density and device size.
- Remove arbitrary one-off values when they do not solve a real optical or layout problem.
- Check compact navigation, sidebars, dense data tables, and mobile layouts separately.

#### Pass 2: Color

- Establish a coherent palette with background, surface, border, text, accent, and semantic roles.
- Use neutral surfaces when they improve prolonged reading and data interpretation; use richer surfaces when the brand and content benefit from them.
- Limit competing accents so primary actions and important information remain recognizable.
- Use semantic colors consistently for success, warning, error, and informational states.
- Verify text and control contrast in every theme and state.
- Avoid decorative gradients, glows, and color washes when they obscure hierarchy; retain them when they have a clear brand or information purpose.
- Treat charts as data communication: colors should distinguish meaningful series or states, not decorate them.

#### Pass 3: Icons and symbols

- Prefer a coherent icon family and consistent optical size, stroke, and alignment.
- Reuse the project's existing icon library where appropriate.
- Replace emoji used as generic interface controls when a consistent icon communicates the action more clearly.
- Retain emoji or custom symbols when they are part of the product's identity, content, or audience language.
- Give icon-only controls accessible names and visible interaction states.
- Remove symbols that add no meaning.

#### Pass 4: Copy and content

- Make headings specific to the page, task, and audience.
- Use concise labels that describe the actual action or information.
- Keep interface terminology consistent.
- Remove unsupported claims, invented customer counts, fake testimonials, and placeholder metrics presented as facts.
- Use realistic sample data when mock data is needed and identify it as illustrative where confusion is possible.
- Keep the voice appropriate to the product and its users; do not force one writing style on every brand.
- Preserve meaningful explanatory copy, legal text, and user-provided content unless editing it is in scope.

#### Pass 5: Typography

- Choose typefaces that support the product's character and reading needs.
- Reuse the project's brand typography when it is intentional and functional.
- Establish a clear scale for display, heading, body, labels, and metadata.
- Use weight, size, spacing, and color to create hierarchy without making everything bold.
- Check line length, line height, wrapping, numeric alignment, and multilingual rendering.
- Use tabular figures for financial or statistical columns when alignment improves scanning.
- Do not apply uppercase tracking, italics, or tight letter spacing mechanically; judge each use by legibility and character.

#### Pass 6: Layout and composition

- Preserve information architecture unless the user requests structural UX changes.
- Choose composition based on content and task: split layouts, asymmetric layouts, stacked layouts, sidebars, tables, grids, and full-width views all have valid uses.
- Keep dashboards usable at realistic desktop proportions; do not compress dense applications into narrow marketing-page layouts.
- Compose landing-page heroes around a clear message and a relevant visual or product preview.
- Give the main content an intentional focal point and supporting hierarchy.
- Ensure mobile layouts reflow in a meaningful reading and interaction order rather than merely shrinking desktop content.
- Avoid repetitive card grids when a table, list, chart, or open layout better represents the information.

#### Pass 7: Component details and data visualization

- Use radii, borders, shadows, and surface elevations consistently, while allowing meaningful components to differ.
- Make active, selected, disabled, loading, success, and error states distinguishable.
- Keep controls recognizable and consistent with the design system.
- Choose chart types that fit the data and the question users need answered.
- Establish a clear hierarchy between primary charts, supporting metrics, tables, and lists.
- Do not add sparklines, icons, badges, or mini charts to a component solely to fill empty space.
- Make dense data scannable through alignment, units, precision, and consistent formatting.
- Ensure empty, partial, stale, and error data states are designed rather than ignored.

#### Pass 8: Visuals and product-specific moments

- Prefer visuals that explain the product, its output, its environment, or the value it creates.
- Use real product content, relevant photography, diagrams, charts, rendered objects, or illustrations when they add information or emotional character.
- Use generated imagery when the user requests it or when it materially improves a clearly identified visual need.
- Leave intentional negative space for text when composing image-led heroes.
- Match visual material, lighting, perspective, and palette to the product direction.
- Avoid generic decorative objects that could be placed on any unrelated product.
- Do not invent product capabilities, data, customer evidence, or claims in mockups.
- If image generation is unavailable, build suitable visuals with project components or describe the missing asset clearly.

#### Pass 9: Motion and interaction

- Motion should communicate cause and effect, state change, hierarchy, or spatial relationships.
- Use transitions for meaningful feedback, not to animate every element.
- Define hover, focus-visible, pressed, selected, disabled, loading, success, and error states where applicable.
- Prefer efficient animation properties such as transform and opacity when appropriate.
- Respect reduced-motion preferences and input differences between pointer, keyboard, and touch.
- Avoid unnecessary looping, large movement, flashing, and motion that delays user tasks.
- Do not rely on animation or color alone to communicate important state.
- Follow the project's existing motion system when one exists.

### Phase 6 — Visual and functional quality assurance

1. Render the updated screen at the target viewport and compare it with the baseline.
2. Check the audit findings one by one; confirm which were fixed and which remain.
3. Test at relevant desktop, tablet, and mobile sizes.
4. Test keyboard navigation, visible focus, touch targets, contrast, and reduced motion.
5. Test the actual user flows and states affected by the changes.
6. Inspect console errors, broken assets, overflow, layout shifts, and loading behavior when tooling permits.
7. Confirm that existing features, routes, content, and interactions still work.
8. Avoid repeated render cycles without a concrete issue to investigate; the number of renders depends on the available tools and complexity, not a fixed universal limit.

### Phase 7 — Report

Summarize:

- The product-specific visual direction.
- The main findings from the audit.
- What changed in each relevant pass.
- Any features or content intentionally preserved.
- Responsive, accessibility, and interaction checks performed.
- Remaining issues, assumptions, or assets the user must provide.
- Whether the result was implemented in the actual project or reconstructed from a screenshot.

Do not claim a browser test, screenshot comparison, or accessibility audit was performed unless it actually was.

## Design decision framework

Use these questions when choosing between competing visual approaches:

1. Does this choice clarify the product or the user's task?
2. Does it strengthen the visual hierarchy?
3. Does it fit the product's audience, brand, and content?
4. Does it improve usability at the target viewport and input mode?
5. Does it preserve or improve accessibility?
6. Does it add useful information or only decoration?
7. Is it consistent with the existing product system?
8. What does it cost in implementation, performance, and maintenance?

A visual treatment is not inherently good or bad. Judge it by context, execution, user benefit, and product identity.

## Relationship to other Wealth Building skills

- **Modern Web Navigation & Interaction Patterns:** selects and implements navigation structures; this skill defines the overall visual direction and screen composition.
- **Micro-Interactions & UI Feedback Design:** focuses on component-level feedback and state responses; this skill integrates motion and interaction into the broader visual system.
- **Frontend Development:** implements the interface in the project's framework and architecture.
- **Product & UX Design:** clarifies user goals, task flows, information architecture, and usability.
- **Accessibility:** provides deeper standards and testing for inclusive interfaces.
- **Brand Identity & Creative Production:** defines the visual identity and assets that the interface should express.

Use these skills together when a task spans product UX, visual design, and implementation. Do not duplicate their full subject matter here.

## Source-derived ideas and added framework

The upstream Unslop skill describes a product-led visual direction, a screen audit, a staged improvement workflow, a restrained interface with meaningful content moments, visual QA, and an optional transformation-story video workflow. It also provides detailed pass guidance for spacing, color, icons, copy, typography, layout, details, visuals, and motion.

This Wealth Building adaptation reorganizes those ideas into a broader nine-pass interface-design process and adds explicit product-preservation, design-decision, responsive, accessibility, functional QA, and reporting guidance. These additions are this repository's operational synthesis, not claims made by the upstream author.

The upstream SKILL.md references separate files such as signs, tokens, visuals, effects, references, and RTL guidance. Those reference files were not available at the paths inspected during this adaptation, so their detailed contents are not reproduced or attributed here. Consult the upstream repository for its current complete references and scripts.

## Classification

- Primary skill: AI Interface Design & Unslop Engineering
- Domain: Development / UI/UX
- Upstream source: Unslop by Damir Sokolovsky, CC BY 4.0
- Primary use cases: UI audit, visual direction, interface redesign, UI polish, responsive visual systems, and visual QA
- Related skills: Modern Web Navigation & Interaction Patterns; Micro-Interactions & UI Feedback Design
- Status: Adapted skill with attribution and additional Wealth Building operational framework

## Ownership and routing boundary

Follow [Skill Boundary & Routing Governance](../../orchestrator/skill-boundary-governance/SKILL.md). This skill owns product-specific AI-interface critique and removal of generic, interchangeable design patterns. Frontend Design owns the overall visual design direction; Apple HIG Review owns Apple-specific platform compliance review; Navigation and Micro-Interactions own their respective interaction domains. Return focused audit findings and design constraints rather than a second full visual specification.
