---
name: frontend-design
description: "Use when a request needs product-grounded visual and frontend design direction."
triggers:
  - "desain web"
  - "landing page"
  - "tampilan app"
  - "frontend"
out_of_scope: "Platform-specific compliance or reference reverse engineering"
escalation: "Hand off work involving Platform-specific compliance or reference reverse engineering to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# Frontend Design

## Purpose

Approach frontend work as the design lead of a studio that gives every product a distinct visual identity. The goal is not to decorate a generic interface or reproduce a fashionable template. Make deliberate choices about visual direction, typography, layout, content, and interaction based on the actual product brief.

Use this skill when creating a new website or application interface, redesigning an existing frontend, or substantially reshaping its visual language. Combine it with engineering, UI audit, navigation, and micro-interaction skills when those concerns are in scope.

## 1. Ground the design in the product

Before choosing colors or components, identify:

- **Product and subject:** What is being designed, and what domain language, materials, conventions, or context belong to it?
- **Audience:** Who will use it, what do they know, and what are they trying to accomplish?
- **Primary job:** What is the most important task the interface must help users complete?
- **Environment:** Desktop, mobile, tablet, kiosk, embedded view, or a combination?
- **Constraints:** Existing brand assets, technical stack, accessibility requirements, content, business rules, and user preferences.

If the brief omits essential context, propose one concrete interpretation and confirm it before committing to a visual direction. Use relevant known product context as a hint, not as permission to invent facts.

Keep real product content in the design. A communication app, merchant POS, trading terminal, and restaurant website should not receive the same layout merely because they are all web interfaces.

## 2. Establish a distinctive visual direction

Make a compact design plan before implementation.

### Color

Define a core palette of 4–6 named colors with hex values. Explain each role: background, surface, primary text, secondary text, accent, and status colors where needed. Check contrast and avoid choosing a palette solely because it is fashionable.

### Typography

Choose one or two type families with clear roles. Define a deliberate type scale, weights, widths, and spacing. Treat display typography as part of the visual identity rather than neutral text delivery. Avoid defaulting automatically to familiar font families or accenting a single word in every headline.

### Layout and alignment

Describe the composition in plain language and, when useful, compare compact ASCII wireframes. State whether content should be left-aligned, centered, or organized in another way, and why. Let hierarchy and task flow determine the structure.

### Distinctive principles

Name the one memorable visual idea and the supporting principles that make the interface specific to this product. Spend visual emphasis deliberately: one strong focal point is usually more effective than many competing decorations.

## 3. Treat visual structure as information

Every structural device should communicate something:

- Borders and outlines define meaningful grouping or boundaries.
- Dividers separate related areas or changes in context.
- Labels clarify status, category, ownership, or action.
- Numbering represents a real sequence, process, or ordered set.
- Spacing expresses hierarchy and relationship.
- Icons reinforce recognizable actions or concepts.

Do not add these elements merely to fill empty space. Avoid repeated eyebrow labels, decorative numbers, arbitrary metadata, and generic template chrome.

## 4. Choose the right first impression

For a web page, decide what users should understand first. The opening may be a headline, product image, live demonstration, interactive moment, key task, or another treatment that best represents the subject.

Do not automatically use a large centered headline, gradient accent, or oversized statistic. Select the opening based on the product's actual value and audience.

For application interfaces, prioritize the user's primary task and the most useful working context rather than forcing a marketing-style hero into a functional workspace.

## 5. Design motion and interaction with intent

Use non-user-triggered motion sparingly. A single orchestrated entrance or reveal is usually more effective than scattered animations on every section or card.

Motion triggered by a user action is useful when it clarifies what changed, such as opening a panel, expanding details, confirming a save, or moving between states. Ensure motion does not obscure content or make routine tasks slower.

For detailed interaction states and feedback patterns, consult [Micro-Interactions & UI Feedback Design](../micro-interactions-and-ui-feedback/SKILL.md). For navigation patterns, consult [Modern Web Navigation & Interaction Patterns](../modern-web-navigation-patterns/SKILL.md).

## 6. Write interface content as part of the design

Words should make the interface easier to understand and use, not act as decoration.

- Write from the end user's perspective.
- Use simple, specific names rather than internal implementation terms.
- Prefer active voice and concise sentence-case copy.
- Make each text element perform one clear job.
- Keep action names consistent throughout a flow: a button labeled "Save changes" should lead to a confirmation such as "Changes saved."
- Explain errors by stating what happened and how the user can fix it.
- Treat empty states as useful invitations to take the next action.
- Match the product's tone and audience without sacrificing clarity.

## 7. Review the plan against the brief

Before coding, challenge the design plan:

1. Would this same palette, type, layout, and component style appear if the product brief were replaced with an unrelated product?
2. Is the memorable visual idea genuinely connected to the subject?
3. Does the hierarchy support the user's primary task?
4. Are labels, borders, numbers, and decorative elements carrying information?
5. Is any element present only because it is a common AI-generated design habit?

Revise generic choices and record what changed and why. Build only after the direction has a clear reason to exist for this product.

## 8. Build carefully

Translate the approved plan into maintainable frontend code.

- Respect the existing framework, component conventions, and project architecture.
- Use reusable components where they improve consistency, not to force every section into an identical card.
- Keep CSS selectors and specificity deliberate; avoid rules that unexpectedly cancel one another.
- Use semantic HTML and accessible interaction patterns.
- Preserve the product's real functionality and content requirements.
- Avoid unnecessary dependencies and decorative effects that increase complexity without improving the experience.

This skill defines design reasoning; it does not replace frontend engineering, security, data modeling, or application testing.

## 9. Critique the implementation

Review the built interface against the original brief and plan. If the environment supports screenshots, inspect the actual rendered result rather than relying only on source code.

Evaluate:

- Product specificity and visual distinctiveness.
- Visual hierarchy, typography, alignment, spacing, and content clarity.
- Consistency without monotonous repetition.
- Primary task completion and functional states.
- Responsive behavior down to mobile.
- Visible keyboard focus and keyboard usability.
- Color contrast and readable text.
- Reduced-motion preferences.
- Loading, empty, error, success, and disabled states where relevant.

Remove at least one unnecessary visual element during critique when it does not contribute to understanding, identity, or task completion. Record remaining issues rather than claiming a complete review when the interface has not been rendered or tested.

## 10. Practical workflow

1. **Discover:** Understand the product, audience, primary task, environment, and constraints.
2. **Plan:** Define the palette, typography, layout, alignment, and distinctive principles.
3. **Compare:** Sketch alternatives when the direction is uncertain.
4. **Review:** Challenge generic choices against the actual brief and revise them.
5. **Build:** Implement the approved design using the existing stack and maintainable components.
6. **Inspect:** Review rendered screenshots or the live interface when available.
7. **Critique:** Test hierarchy, usability, responsiveness, accessibility, and functional states.
8. **Refine:** Remove unnecessary decoration and correct the highest-impact issues.

## 11. Relationship to other Development skills

- **[Reverse Engineering & Reference-Based Reconstruction](../reverse-engineering-and-reference-based-reconstruction/SKILL.md):** investigates reference products and extracts evidence-backed patterns before this skill establishes the new product's distinct visual direction.
- [AI Interface Design & Unslop Engineering](../ai-interface-design-and-unslop-engineering/SKILL.md) provides a broader UI audit and quality-review framework. Use Frontend Design to establish the visual direction and design plan; use the audit skill to inspect and improve the resulting interface.
- [Micro-Interactions & UI Feedback Design](../micro-interactions-and-ui-feedback/SKILL.md) provides detailed interaction-state and feedback patterns.
- [Modern Web Navigation & Interaction Patterns](../modern-web-navigation-patterns/SKILL.md) provides navigation structures and interaction models.
- [Professional Logo & Brand Identity](../professional-logo-and-brand-identity/SKILL.md) covers logo and identity-system development. Frontend Design applies the approved identity to a usable interface.

## Source and adaptation

This skill is an original operational synthesis adapted from Anthropic's **Frontend Design** skill:

- Source: https://github.com/anthropics/skills/tree/main/skills/frontend-design
- Original author/publisher: Anthropic
- Source license: Apache License 2.0
- The source's design principles and workflow have been reorganized and rewritten for the Wealth Building repository. Additional implementation, review, and cross-skill routing guidance is repository-specific synthesis.
- The Apache License 2.0 text is retained in this directory as required for redistribution.

## Ownership and routing boundary

Follow [Skill Boundary & Routing Governance](../../../orchestrator/skill-boundary-governance/SKILL.md). Frontend Design owns product-grounded visual direction and the overall interface design brief. AI Interface Design audits product specificity and generic-pattern quality; Apple HIG Review owns Apple-platform convention review; Modern Web Navigation owns navigation patterns; Micro-Interactions owns interaction feedback; Reverse Engineering owns evidence gathered from supplied references; Professional Logo owns brand identity assets. Invoke those specialists only when their scope is present, and do not treat their audits as replacements for frontend implementation or testing.


## Design-system handoff for application delivery

For multi-screen products, make visual direction implementable and testable: semantic design-token roles, typography and spacing scales, layout/breakpoint rules, component variants, interaction states, focus behavior, responsive rules, and examples of use. Keep tokens separate from component code so identity can evolve without rewriting every component.

When adapting a reference, retain general usability principles but create distinct brand expression, copy, assets, and visual composition. Screenshot similarity is not the definition of design quality. Coordinate with Application Architecture Planning for technical constraints and Full-Stack Application Engineering for implementation.
