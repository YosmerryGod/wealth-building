---
name: reverse-engineering-and-reference-based-reconstruction
description: Investigate existing websites, applications, products, and software behavior as references; extract evidence-backed structure, user journeys, interaction patterns, and reusable principles; then adapt them into an original solution for a different product or business.
---

# Reverse Engineering & Reference-Based Reconstruction

## Purpose

Help an AI understand how an existing digital product works and why its experience is structured as it is, then use those findings to design or build a distinct solution that serves the user's goal.

This skill treats reverse engineering as a disciplined investigation and learning process. It applies to websites, web applications, mobile applications, desktop software, digital services, and other observable products. It can be used when the user says "make something like this", supplies a URL, screenshot, recording, application, or product name, or asks how an existing feature works.

The goal is not to copy a product blindly. The goal is to discover the underlying patterns, decisions, flows, and mechanisms that can be adapted to a new context.

## 1. Decide what is being investigated

First identify the reference and the actual question.

Classify the target:

- Live website or web application.
- Mobile or desktop application.
- Static screenshot, mockup, or design reference.
- Screen recording or observed user journey.
- Public source repository or documentation.
- Packaged application, binary, firmware, or other shipped artifact.
- API behavior, network exchange, or integration.
- A named product without a directly supplied artifact.

Clarify the investigation objective only when it materially changes the work:

- Understand the overall product experience.
- Reconstruct a page or visual layout.
- Understand a particular feature or interaction.
- Map navigation and user journeys.
- Identify reusable design or product patterns.
- Compare two versions or competing products.
- Explain implementation behavior.
- Create an original adaptation for a different audience, domain, or business.

Do not assume that a request to build "like X" means the user wants a pixel-perfect clone. Interpret the reference as a source of patterns unless the user explicitly defines a narrower scope.

## 2. Choose the right evidence method

Select the lightest method that can answer the question.

| Available evidence | Suitable investigation |
|---|---|
| Screenshot or image | Inspect visible hierarchy, layout, typography, color, spacing, imagery, and visible controls; do not infer hidden behavior as fact |
| Screen recording | Reconstruct the observed sequence, state changes, timing, and visible feedback |
| Live public website | Inspect pages, navigation, responsive states, content, links, and interactions available to the browser |
| Public source code | Read architecture, components, styles, routes, data flow, and tests; distinguish source intent from deployed behavior |
| API documentation or captured traffic | Map requests, responses, state transitions, and integration contracts within the evidence available |
| Installed app or shipped binary | Use suitable reverse-engineering tools when available and authorized; inspect package structure, resources, metadata, and code where supported |
| No direct artifact | Use documented public information and clearly mark the analysis as indirect |

A browser inspection can reveal observable behavior but usually cannot establish the complete internal architecture. A screenshot cannot prove how a control behaves. Source code does not by itself prove that the deployed application behaves identically.

For deeper binary, package, firmware, or runtime investigations, consult a dedicated reverse-engineering toolchain such as REA only when it is actually connected and available. The REA project provides its own skill, MCP server, CLI, and specialized integrations; this knowledge skill does not install or reproduce those tools.

Do not claim to have opened, tested, decompiled, or executed a target unless the relevant tool actually did so.

## 3. Build an evidence map before drawing conclusions

Record findings in four distinct classes:

1. **Observed:** directly visible or returned by an inspected artifact or tool.
2. **Supported interpretation:** a reasonable explanation grounded in one or more observations.
3. **Hypothesis:** a plausible explanation that still needs testing.
4. **Unknown:** information not available from the current evidence.

For each important finding, retain where it came from: URL and page, screenshot, timestamp in a recording, source file, route, request, tool result, or other reference.

Assess evidence coverage:

- Which pages, screens, states, and flows were inspected?
- Which viewport sizes or device types were covered?
- Which interactions were actually exercised?
- What requires login, payment, location, a real account, or unavailable permissions?
- What could not be inspected?
- Are there multiple plausible explanations?

A few sampled pages are not proof of the whole product. A missing result in a limited search is not proof that a feature does not exist.

## 4. Investigate the product in layers

Use the layers relevant to the user's goal rather than forcing every investigation to cover everything.

### A. Product and business intent

Identify:

- What value the product appears to provide.
- Who the likely users are.
- The primary user problem or job.
- The product's positioning and differentiation.
- Its main conversion or success action.
- Important business constraints visible in the experience.

Separate explicit claims from inferred strategy.

### B. Information architecture

Map:

- Main sections and page hierarchy.
- Navigation model and destinations.
- Content grouping and naming.
- Search, filtering, sorting, and discovery patterns.
- Important page-to-page relationships.
- Entry points and exit points.

Represent the structure as a concise sitemap or flow when useful.

### C. Visual system

Inspect:

- Layout composition and grid.
- Content width and alignment.
- Typography hierarchy.
- Color roles and contrast.
- Spacing rhythm.
- Image and media treatment.
- Borders, surfaces, icons, and component shapes.
- Responsive changes where observable.
- Distinctive visual principles that make the product recognizable.

Describe reusable design decisions rather than merely listing colors and pixels.

### D. Interaction and state

For each important control, determine where possible:

- Initial state.
- User action.
- Resulting state.
- Feedback or animation.
- Loading, empty, error, success, and disabled states.
- Persistence after navigation or refresh.
- Keyboard, touch, and accessibility behavior.

Do not invent states that were not observed. Mark untested states as unknown or recommended design requirements.

### E. User journeys

Trace the important tasks from entry to completion, such as:

- Discovering a product or service.
- Comparing alternatives.
- Viewing product details.
- Adding to cart or saving an item.
- Registering or signing in.
- Booking, ordering, or paying.
- Tracking an order or managing an account.

For each journey, record user intent, steps, decision points, friction, feedback, and completion condition. Focus on the journeys that matter to the user's requested outcome.

### F. Content and conversion

Inspect:

- Headline and value proposition.
- Product naming and descriptions.
- Calls to action.
- Trust signals and proof.
- Pricing and offer presentation.
- Objection handling and FAQs.
- Checkout friction and reassurance.
- Cross-sell, upsell, retention, or repeat-use prompts.

Treat conversion explanations as hypotheses unless supported by analytics, experiments, or direct evidence.

### G. Technical behavior, when in scope

If source code, developer tools, API documentation, or authorized runtime tooling is available, inspect relevant:

- Routes and page composition.
- Component boundaries and reusable patterns.
- Data sources and state ownership.
- API requests and response handling.
- Authentication and authorization boundaries.
- Persistence and session behavior.
- Third-party integrations.
- Performance and accessibility implications.

Do not infer a framework, database, backend, or hosting provider from visual appearance alone.

## 5. Convert findings into reusable patterns

Do not transfer every observed detail. Classify each finding:

- **Keep as a principle:** a general solution to a user problem, such as clear product discovery.
- **Adapt:** a pattern that is useful but needs a different form for the new audience or business.
- **Replace:** a choice that conflicts with the new product, customer, brand, or operating model.
- **Ignore:** a detail that is irrelevant to the requested outcome.
- **Investigate further:** a finding whose uncertainty could change the design or implementation.

For every important pattern, explain:

- The problem it solves.
- How the reference appears to solve it.
- The evidence supporting that interpretation.
- Why it may or may not fit the new product.
- The adaptation proposed.
- Any trade-off or unanswered question.

The best reconstruction preserves useful product logic while changing the expression to fit the new context.

## 6. Adapt the reference to the new product

Before proposing the solution, establish:

- New product or business and its actual offer.
- Target customers and their purchase or usage context.
- Primary task and desired conversion.
- Content, products, services, and business rules.
- Brand identity and available assets.
- Device and channel priorities.
- Operational constraints such as delivery, stock, booking, payment, or service area.

Create a translation map:

| Reference pattern | Original purpose | New-context adaptation |
|---|---|---|
| Large editorial product imagery | Make products immediately understandable and desirable | Use authentic food photography and clear portion or menu context for a restaurant |
| Category-led product discovery | Help users find relevant items | Organize menu categories around meal type, portion, package, or occasion |
| Product detail and variants | Explain choice and price | Show portion size, side dishes, add-ons, availability, and price |
| Cart and checkout | Convert intent into an order | Adapt to pickup, delivery, address, time, payment, and order confirmation |
| Brand storytelling | Explain product identity and value | Tell the actual business story, preparation approach, ingredients, and differentiators |

This table is illustrative, not a mandatory design. Adapt the structure to the real product.

## 7. Produce an actionable reconstruction brief

A useful output should contain the sections relevant to the task:

1. **Reference summary:** what was inspected and why it matters.
2. **Evidence and coverage:** what was observed, what was inferred, and what remains unknown.
3. **Product structure:** sitemap, key pages, or feature map.
4. **Important journeys:** task steps and interaction states.
5. **Reusable patterns:** keep, adapt, replace, ignore, or investigate.
6. **New product direction:** audience, goals, content, brand, and conversion.
7. **Proposed experience:** page structure, components, behavior, and responsive priorities.
8. **Implementation notes:** only when the user requests implementation or technical planning.
9. **Validation checklist:** how to verify the reconstructed experience.

For a small request, provide a concise version. Do not produce a large report when the user only needs one page or one feature understood.

## 8. Validate the adaptation

Review the result against both the evidence and the new product requirements.

- Does it solve the same underlying user problem?
- Is the adaptation appropriate for the new audience and business?
- Are the most useful reference patterns retained?
- Have irrelevant reference conventions been removed?
- Are key journeys complete and understandable?
- Are interaction states defined and tested where possible?
- Does the new identity feel distinct rather than like a reskinned copy?
- Are responsive behavior, accessibility, and performance considered?
- Are claims about the reference and implementation supported by evidence?

If a live implementation exists, inspect the rendered product and test the important journeys. Do not mark validation complete based only on a design brief or source-code review.

## 9. Intellectual property and differentiation

Reverse engineering can be used to learn from observable products and understand general ideas, methods, workflows, and functional patterns. The resulting work should be independently expressed for the user's context.

Distinguish reusable functional ideas from protected expression, including distinctive branding, logos, copy, photography, illustrations, proprietary assets, and source code. Do not present another company's identity or assets as the user's. When the user requests a close imitation, explain which general experience principles can be adapted and create a distinct visual and content direction.

## 10. Practical workflow

1. **Frame:** identify the reference, target product, user goal, and scope.
2. **Select evidence:** choose browser, image, recording, source, API, or specialist tooling according to what is available.
3. **Inspect:** investigate only the relevant product, visual, interaction, journey, and technical layers.
4. **Record:** separate observations, interpretations, hypotheses, and unknowns.
5. **Map:** summarize architecture, pages, states, and important user journeys.
6. **Extract:** identify principles and patterns worth retaining.
7. **Translate:** adapt those patterns to the new audience, business, brand, and constraints.
8. **Specify:** produce a usable design or implementation brief.
9. **Build and validate:** use the relevant design and engineering skills when implementation is requested.
10. **Report:** state what was inspected, what was not, and how confident the conclusions are.

## 11. Relationship to other skills

- **[Frontend Design](../frontend-design/SKILL.md):** establishes the original visual direction and designs the new interface. This skill investigates the reference and translates its useful patterns; Frontend Design decides how the new product should look.
- **[AI Interface Design & Unslop Engineering](../ai-interface-design-and-unslop-engineering/SKILL.md):** audits the quality and specificity of the resulting interface.
- **[Modern Web Navigation & Interaction Patterns](../modern-web-navigation-patterns/SKILL.md):** helps select navigation structures for the adapted product.
- **[Micro-Interactions & UI Feedback Design](../micro-interactions-and-ui-feedback/SKILL.md):** defines detailed feedback and state transitions.
- **[Professional Logo & Brand Identity](../professional-logo-and-brand-identity/SKILL.md):** creates a distinct identity rather than copying the reference brand.
- **[Business Agent Orchestrator](../../../orchestrator/business-agent/SKILL.md):** coordinates business discovery, customer and competitor research, brand preparation, and approved execution when the reconstruction serves a business project.
- **[Contextual Understanding & Intent Inference](../../../orchestrator/contextual-understanding/SKILL.md):** interprets what the user means by "like this", preserves prior constraints, and avoids asking for information already known.
- **REA (Reverse Engineer Anything):** a separate external toolchain for supported native, managed, packaged, browser, and runtime investigations. Use only when its MCP/CLI and required engines are actually available. This skill remains useful without REA for ordinary browser, screenshot, recording, and source-based analysis.

## Scope and capability boundary

This file defines an AI reasoning and investigation workflow. It does not itself browse websites, operate a browser, capture network traffic, decompile binaries, run applications, install REA, or provide persistent evidence storage. Those capabilities depend on tools and access available in the execution environment.
