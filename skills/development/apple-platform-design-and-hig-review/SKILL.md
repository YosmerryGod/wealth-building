---
name: apple-platform-design-and-hig-review
title: Apple Platform Design & Human Interface Guidelines Review
category: development
subcategory: platform-ux-and-design-review
source_type: official-guideline-based-operational-synthesis
sources:
  - Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
  - Apple Design Skill reference: https://github.com/dickwu/apple-design-skill
language: English
description: "Use when a request needs Apple platform convention and HIG review."
triggers:
  - "iOS"
  - "iPhone app"
  - "HIG"
  - "apple design"
out_of_scope: "Universal visual design or implementation ownership"
escalation: "Hand off work involving Universal visual design or implementation ownership to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# Apple Platform Design & Human Interface Guidelines Review

## Purpose

Help an AI agent design, review, and improve interfaces for Apple-platform experiences while preserving platform conventions, accessibility, product identity, and the user's actual task.

Use this skill when a user asks to:
- Review an iOS, iPadOS, macOS, watchOS, or visionOS interface against Apple design guidance.
- Build or refine an Apple-oriented interface in SwiftUI, UIKit, AppKit, Flutter, React Native, Tauri, or Electron.
- Evaluate navigation, toolbars, tab bars, sheets, dialogs, forms, settings, onboarding, notifications, widgets, or other platform-sensitive components.
- Improve an interface that should feel at home on Apple platforms without blindly copying Apple's visual style.

This is a focused platform-review skill. It complements the repository's general Frontend Design and AI Interface Design skills; it does not replace product discovery, implementation engineering, or direct consultation of the current official guideline for a specific component.

## Core design principles

Use these eight principles as a high-level review lens. Interpret them in the context of the product and the relevant current platform guidance.

1. **Purpose** — Make the product's purpose and the current task clear. Prioritize the work people came to do.
2. **Agency** — Keep people in control. Make actions understandable, reversible where practical, and free from unnecessary obstruction.
3. **Responsibility** — Respect privacy, security, accessibility, user data, and the consequences of system behavior.
4. **Familiarity** — Use recognizable platform conventions and mental models when they help people understand the interface.
5. **Flexibility** — Support different contexts, preferences, input methods, display sizes, and levels of experience.
6. **Simplicity** — Reduce unnecessary complexity without hiding important choices or removing useful capabilities.
7. **Craft** — Pay attention to typography, hierarchy, alignment, materials, transitions, content, and implementation details.
8. **Delight** — Add moments of personality or satisfaction when they reinforce the product rather than interrupting the task.

These principles are a review framework, not a substitute for component-specific rules. When a current Apple guideline conflicts with a broad interpretation of a principle, follow the current relevant guideline and explain the context.

## Review lenses

Evaluate the interface through these lenses, in order:

### 1. Accessibility

Check:
- Dynamic Type or equivalent text scaling and layout resilience.
- Contrast, color-independent meaning, and legibility in light and dark appearances.
- Screen-reader names, roles, grouping, and reading order.
- Keyboard navigation, focus visibility, and pointer alternatives where relevant.
- Adequate interactive target sizes and spacing.
- Reduced Motion, transparency, and other relevant accessibility preferences.
- Forms, validation, errors, and status feedback that can be understood without relying on color or animation alone.

Do not claim a measured contrast ratio, accessibility pass, or standards compliance unless the relevant implementation has actually been tested. Distinguish a design inspection from automated or assistive-technology testing.

### 2. Platform conventions

For mobile and tablet, inspect:
- Navigation hierarchy and appropriate use of tab bars, navigation bars, toolbars, and sidebars.
- Safe areas, system bars, keyboard avoidance, orientation, and size adaptation.
- Sheets, popovers, alerts, confirmation, destructive actions, and dismissal behavior.
- Touch gestures and whether important actions also have discoverable alternatives.

For desktop, inspect:
- Window behavior, resizing, multiple windows, menu bar, toolbars, sidebars, context menus, and keyboard shortcuts.
- Pointer hover, focus, drag-and-drop, and contextual actions.
- Whether settings and commands appear where users of that platform expect them.

For cross-platform products, decide deliberately which conventions should be native to each platform and which should remain consistent across the product. Do not assume that one shared layout is automatically the best cross-platform experience.

### 3. Visual design and craft

Review:
- Semantic color roles and appearance adaptation.
- Typography hierarchy, text scaling, density, and readable line lengths.
- Spacing, alignment, grouping, and visual hierarchy.
- Icon consistency, meaning, weight, and platform-appropriate usage.
- Materials, translucency, depth, and layering only when they improve context or hierarchy.
- Motion that communicates state, spatial relationships, or feedback.
- Brand expression that remains distinctive without undermining platform usability.

Do not imitate a native material or visual effect merely because it is fashionable. Confirm that it is appropriate for the platform version, content layer, and interaction.

### 4. Interaction

Inspect:
- Loading, progress, success, error, empty, offline, and partial states.
- Immediate feedback after actions.
- Modality, interruption, alerts, confirmation, and ways to cancel or undo.
- Destructive actions and recovery paths.
- Data entry, validation timing, focus movement, and keyboard behavior.
- Whether controls behave consistently with their visual affordances.

### 5. Content and writing

Check:
- Labels that accurately describe the action or destination.
- Clear, concise instructions and meaningful empty states.
- Error messages that explain what happened and how to recover.
- Platform-appropriate terminology and capitalization.
- Permission prompts that explain the value and timing of the request.
- No misleading system-like wording or false claims about platform behavior.

## Review workflow

1. **Establish context.** Identify platform, OS version when known, framework, device class, product purpose, audience, and primary task.
2. **Inspect the actual surface.** Review the screenshot, design file, rendered application, or relevant source code. State which evidence is available.
3. **Select relevant official guidance.** Read the current Apple Human Interface Guidelines pages for the components and technologies visible in the interface. Do not infer detailed rules from a general principle alone.
4. **Audit in order.** Use the five review lenses above. Separate platform mismatches from general usability or visual preferences.
5. **Prioritize findings.** Mark issues as Critical (blocks access or core task), High (major platform or usability mismatch), Medium (inconsistent or confusing), or Polish (craft refinement).
6. **Propose concrete fixes.** Explain the issue, why it matters, the relevant guideline or principle, and an implementation direction appropriate to the user's framework.
7. **Verify the result.** Inspect the updated render at relevant sizes and appearances. Test interaction states and accessibility behavior where tools and environment allow.
8. **Report honestly.** Separate observed evidence, guideline-based interpretation, unverified assumptions, and tests that were not performed.

## Required review report

Use this structure:

### Summary
One concise assessment of the interface and the most important issue.

### Critical
List only findings that block accessibility, safety, or a core task. If none were observed, say so.

### Improvements
For each finding include:
- **What:** the observed issue.
- **Why:** its effect on the user or platform consistency.
- **Guidance:** the relevant official Apple guideline page or principle. Link the page when available.
- **Fix:** a concrete change in the target framework.

### Craft notes
Discuss visual hierarchy, typography, spacing, motion, and brand expression where useful.

### What works
Identify decisions worth preserving so that refinement does not erase successful product-specific choices.

### Verification
State tested platforms, viewports, appearances, interaction states, tools used, and anything not verified.

## Cross-platform translation

Translate platform concepts into the user's framework rather than assuming the app is written in Apple's native frameworks.

| Apple concept | Flutter | React Native | Web / Tauri / Electron |
|---|---|---|---|
| Dynamic Type | Text scaling and MediaQuery | Font scaling and accessibility props | Browser zoom and scalable typography |
| VoiceOver | Semantics | accessibilityLabel / accessibilityRole | ARIA and screen-reader semantics |
| Safe areas | SafeArea / MediaQuery insets | Safe-area context | Insets and window chrome |
| Size classes | LayoutBuilder / constraints | Dimensions and responsive layout | Media and container queries |
| Tab bar | NavigationBar / BottomNavigationBar | Tab navigator | Platform-appropriate navigation |
| Sheet or popover | Modal bottom sheet / dialog | Modal / popover pattern | Dialog / popover / panel |
| Semantic colors | ThemeData roles | Theme tokens | CSS custom properties |

This table is a translation aid, not a claim that the frameworks implement identical platform behavior. Check the actual platform and framework documentation before relying on a native behavior.

## Specialized review topics

Load the relevant current official guidance when reviewing:
- App icons and brand marks.
- Navigation, tab bars, toolbars, sidebars, and split views.
- Forms, onboarding, permissions, and privacy prompts.
- Dark mode, semantic colors, and system materials.
- Notifications, widgets, and Live Activities.
- Charts and data presentation.
- Apple Pay buttons, payment marks, and checkout.
- Generative AI and machine-learning features.
- Foldable or multi-display layouts.
- App Store review-sensitive behavior.

Do not invent policy requirements or App Review outcomes. When compliance is in question, cite the current official guideline and distinguish design advice from formal review requirements.

## Relationship to other Wealth Building skills

- **Frontend Design:** Establishes the product-specific visual direction and frontend plan. Use this skill when Apple platform conventions or HIG review are specifically relevant.
- **AI Interface Design & Unslop Engineering:** Provides broad interface inspection, anti-generic design review, implementation QA, and refinement across product types.
- **Micro-Interactions & UI Feedback Design:** Provides focused interaction-state and feedback patterns; this skill checks whether those patterns fit the Apple platform context.
- **Modern Web Navigation & Interaction Patterns:** Covers navigation patterns for web products; use this skill to evaluate their suitability when a product targets Apple platforms.
- **Product-specific engineering skills:** Implement the approved changes in the actual framework and codebase.

## Source and limitations

- Primary source: Apple's official Human Interface Guidelines at https://developer.apple.com/design/human-interface-guidelines/.
- Secondary reference for review organization and cross-platform framing: https://github.com/dickwu/apple-design-skill.
- This document is an original operational synthesis for Wealth Building. It does not copy the upstream repository's 123-page guideline collection or claim to reproduce Apple's full documentation.
- The eight-principle summary and five-lens review structure are attributed as a framework reference; detailed component decisions must be checked against the current official Apple pages.
- Apple's guidance changes over time. Recheck the official source when platform behavior, OS versions, or review requirements may have changed.
- A screenshot-only review cannot verify runtime behavior, accessibility tree, actual touch targets, keyboard operation, or App Store compliance.
- Automated checks do not replace testing with assistive technologies and on real target devices.

## Classification

- Domain: Development
- Category: Platform UX / Design Review
- Type: Specialist design-review skill
- Primary use: Apple-platform UI design, audit, and improvement
- Related skills: Frontend Design; AI Interface Design & Unslop Engineering; Micro-Interactions & UI Feedback Design; Modern Web Navigation & Interaction Patterns
