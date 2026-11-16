---
name: Micro-Interactions & UI Feedback Design
title: Micro-Interactions & UI Feedback Design
category: development
source_type: user-provided-video-and-operational-framework
source: User-provided video 67332.mp4; demonstrates button animation, card hover, skeleton loading, and glow effects
language: English
---

# Micro-Interactions & UI Feedback Design

## Purpose

Help an AI agent design and implement small, purposeful interface responses that make digital products feel understandable, responsive, and polished.

A micro-interaction is a focused response to a user action, system event, or change in interface state. It may communicate that an element is interactive, acknowledge an action, show progress, explain a state change, or guide attention.

The goal is not to animate every element. Each interaction should improve feedback, clarity, orientation, or perceived responsiveness without distracting users or slowing the product.

This skill focuses on four visual techniques demonstrated in the source video:

1. Button animation.
2. Card hover effects.
3. Skeleton loading.
4. Glow effects.

The video demonstrates visual examples only. The selection criteria, accessibility requirements, implementation workflow, and quality standards below are additional operational guidance.

## Source-derived techniques

### 1. Button Animation

A button can respond to interaction with a subtle visual change. Examples include a small scale or position change, a color transition, a shadow adjustment, or a brief highlight.

**Purpose**
- Make the button feel interactive.
- Acknowledge hover, press, or activation.
- Help users understand that an action was received.

**Implementation guidance**
- Define separate default, hover, focus-visible, active/pressed, disabled, and loading states where applicable.
- Keep transitions short and restrained.
- Use a pressed state to provide immediate feedback on activation.
- Preserve clear text and icon contrast in every state.
- Do not make a button appear enabled when the action is unavailable.
- Prevent repeated submission when an action is already processing.

A button animation must not replace a visible status message when the action has an important result, such as saving data, submitting a payment, or deleting content.

### 2. Card Hover Effects

A card can change slightly when a pointer moves over it. Possible effects include a small elevation or shadow change, a subtle border or background shift, or a restrained movement.

**Purpose**
- Suggest that a card is interactive.
- Distinguish clickable cards from static content.
- Provide a lightweight response to pointer interaction.

**Implementation guidance**
- Apply hover treatment only when the card actually has an interactive action.
- Keep the movement and elevation subtle.
- Use a visible keyboard focus treatment for interactive cards.
- Make the entire clickable area and its destination clear.
- Do not communicate essential information only through hover.
- Ensure the card remains understandable and usable on touch devices, where hover may not exist.

If a card contains multiple independent actions, use clear links or buttons for those actions instead of making the entire card behave ambiguously.

### 3. Skeleton Loading

A skeleton is a temporary visual placeholder that approximates the shape or layout of content while that content is loading.

**Purpose**
- Communicate that content is being loaded.
- Preserve the expected page structure while data is unavailable.
- Reduce the visual disruption of an otherwise empty region.

**Implementation guidance**
- Match the approximate size and arrangement of the expected content.
- Use skeletons for content regions whose structure is reasonably predictable.
- Replace the skeleton with real content or an appropriate error/empty state when loading finishes.
- Avoid showing skeletons for longer than necessary or when content is already available.
- Use a restrained shimmer only when it helps communicate ongoing loading.
- Respect reduced-motion preferences; a static placeholder is often sufficient.
- Provide an appropriate accessible loading status when the wait is meaningful, without announcing every decorative placeholder individually.

A skeleton is not real content and must not be presented as if data has loaded. If a request fails, show an error or retry state rather than leaving the skeleton indefinitely.

### 4. Glow Effects

A glow is a soft highlight around an element, commonly created with shadow, border, or background treatment.

**Purpose**
- Draw attention to a relevant element or state.
- Emphasize focus, selection, or a primary action.
- Support a visual hierarchy when used selectively.

**Implementation guidance**
- Reserve stronger glow for a small number of meaningful elements.
- Use it to reinforce an existing state, not as the only signal.
- Maintain sufficient text and control contrast.
- Avoid large, intense, or continuously animated glows that compete with content.
- Do not use glow as the sole indicator of keyboard focus, validation, selection, or status.
- Consider rendering cost when using multiple layered shadows or animated effects.

Glow is a visual treatment, not a substitute for clear labels, state text, borders, icons, or accessible focus indicators.

## Choosing the right interaction

Before adding an effect, identify the user need it serves.

| User or system need | Suitable feedback | Important condition |
|---|---|---|
| Acknowledge pointer or press interaction | Button animation | Keep the action and state clear |
| Suggest that a content tile is clickable | Card hover and focus treatment | Also support keyboard and touch |
| Communicate that content is loading | Skeleton loading | Replace it with success, empty, or error content |
| Emphasize focus or a selected primary element | Restrained glow | Pair it with another visible state indicator |
| Confirm that an important action completed | Status text, icon, or notification | Do not rely on animation alone |
| Explain an unavailable or failed action | Disabled, validation, or error state | Explain the reason when users need it |

Do not add an effect merely because it looks attractive. If it does not improve feedback, comprehension, hierarchy, or task completion, leave it out.

## Interaction state model

For each interactive component, identify the states that actually apply:

- **Default:** the normal resting appearance.
- **Hover:** pointer is over the element; optional and device-dependent.
- **Focus-visible:** keyboard or other visible focus is on the element.
- **Active / pressed:** the user is currently activating the element.
- **Selected:** the element or option is currently chosen.
- **Disabled:** the action is unavailable.
- **Loading:** an operation is in progress.
- **Success:** the operation completed successfully.
- **Error:** the operation failed or needs correction.

Not every component needs every state. Choose states according to the component's behavior and the user's task. Keep visual meanings consistent across the product.

## Implementation workflow for the AI agent

1. **Inspect the existing product.** Identify the framework, component library, styling conventions, design tokens, and current interaction behavior before making changes.
2. **Understand the action.** Determine what the user does, what system event occurs, and what feedback the user needs.
3. **Choose the smallest useful response.** Prefer a subtle state change over elaborate animation.
4. **Define state transitions.** Specify when the interaction starts, ends, and what happens on success, failure, cancellation, or timeout.
5. **Design for all input modes.** Consider pointer, keyboard, touch, and assistive technology. Do not assume hover is available.
6. **Respect motion preferences.** Use reduced-motion settings to remove or simplify nonessential movement.
7. **Preserve accessibility.** Maintain contrast, visible focus, semantic controls, understandable status messages, and usable hit areas.
8. **Preserve performance.** Prefer efficient properties such as transform and opacity for motion when appropriate; avoid unnecessary layout-triggering animation and excessive simultaneous effects.
9. **Reuse project conventions.** Use existing tokens and shared components. Do not add a dependency for a simple transition without a clear reason.
10. **Test real states.** Verify normal, hover, focus, pressed, loading, success, error, disabled, and responsive behavior as relevant.
11. **Review the experience.** Confirm that feedback is noticeable enough to help but not so strong that it distracts from the task.

## Accessibility and usability requirements

- Never make hover the only way to reveal essential content or functionality.
- Ensure every interactive element can be reached and operated with a keyboard.
- Provide a clear focus-visible indicator; a glow may supplement it but must not replace it.
- Maintain adequate contrast in all interaction states.
- Do not communicate success, failure, selection, or validation through color or animation alone.
- Respect the user's reduced-motion preference.
- Avoid flashing, rapid pulsing, or repetitive movement that can distract or cause discomfort.
- Keep controls stable enough that animation does not make targets difficult to hit.
- Ensure loading indicators do not trap focus or prevent users from understanding the current state.
- Use semantic buttons and links rather than clickable generic containers when appropriate.

## Performance and engineering guidance

- Prefer CSS transitions or the project's existing animation system for simple interactions.
- Animate transform and opacity where suitable; avoid repeatedly animating layout dimensions or expensive visual effects.
- Avoid applying large blur or layered shadow effects to many elements simultaneously.
- Do not introduce animation libraries for isolated effects unless the project already uses one or the complexity justifies it.
- Keep interaction timing consistent across related components.
- Avoid motion that delays the user's ability to act.
- Ensure animations do not cause layout shifts or obscure important content.
- Test on lower-powered mobile devices as well as desktop.

## Quality checklist

- [ ] Every effect has a clear user-facing purpose.
- [ ] Buttons provide appropriate hover, focus, pressed, disabled, and loading feedback.
- [ ] Interactive cards are distinguishable from static cards.
- [ ] Card interactions work without hover, including on touch and keyboard.
- [ ] Skeletons match the expected content structure and disappear when loading ends.
- [ ] Loading failures lead to a useful error or retry state.
- [ ] Glow is restrained and reinforces rather than replaces state information.
- [ ] Focus indicators are visible and accessible.
- [ ] Reduced-motion preferences are respected.
- [ ] Text and controls retain sufficient contrast.
- [ ] Motion does not interfere with task completion.
- [ ] Effects do not create avoidable performance or layout problems.
- [ ] The implementation follows the existing project's design and code conventions.

## Relationship to other skills

- **Modern Web Navigation & Interaction Patterns:** focuses on navigation structures such as Floating Pill Navigation, Bottom Tab Bar, and Command Palette. This skill focuses on the feedback and state response of individual interface elements.
- **Frontend Development:** implements components, state transitions, styling, and responsive behavior.
- **Product & UX Design:** identifies user goals, task flows, and the feedback users need.
- **Visual Design & Design Systems:** defines consistent color, elevation, typography, spacing, and motion tokens.
- **Accessibility:** provides deeper guidance for inclusive interaction and assistive technologies.

These skills complement one another and should not be treated as interchangeable.

## AI implementation rules

- Inspect the existing codebase before editing UI interactions.
- Only change the requested scope; do not redesign unrelated components.
- Do not add animation to every component by default.
- Do not use hover-only interactions for essential actions or information.
- Do not use glow or color as the only state indicator.
- Do not leave skeleton placeholders visible after loading has completed or failed.
- Prefer subtle, purposeful, performant feedback.
- Preserve existing design tokens, component patterns, and dependencies.
- If the intended behavior is unclear, ask one focused question before implementation.

## Source limitations

The user-provided video 67332.mp4 demonstrates four visual techniques: button animation, card hover, skeleton loading, and glow effects. It does not provide implementation code, accessibility testing, performance measurements, or evidence that these effects improve usability in every context. The purposes, selection criteria, state model, accessibility guidance, engineering workflow, and quality checklist in this skill are additional operational guidance and must not be attributed to the video.

## Classification

- Primary skill: Micro-Interactions & UI Feedback Design
- Domain: Development / UI/UX
- Source-derived techniques: Button Animation, Card Hover Effects, Skeleton Loading, Glow Effects
- Primary use cases: Websites, dashboards, mobile applications, and interactive digital products
- Source status: Four visual techniques summarized from a user-provided video; practical selection, accessibility, implementation, and testing guidance added as an operational framework
