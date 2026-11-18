---
name: full-stack-application-engineering
title: Full-Stack Application Engineering
category: development
subcategory: application-implementation
source_type: original-adaptation-from-replica-skill
language: English
description: "Use when implementing application screens, routes, components, and end-to-end user flows from approved requirements and architecture."
triggers: ["bangun aplikasi","implementasi frontend backend","buat halaman aplikasi","coding fitur","build application"]
out_of_scope: "Product discovery, architecture decisions without context, specialist backend security, or production release approval"
escalation: "Use Application Architecture Planning for unresolved architecture, Backend Engineering for auth/data/integrations, Frontend Design for visual direction, QA for verification, and Risk Assessment for high-consequence changes."
---

# Full-Stack Application Engineering

## Purpose
Implement a working product from approved requirements, architecture, and design contracts. Prioritize complete user outcomes over isolated mockups or disconnected code.

## Preconditions
Read the actual project and relevant files before editing. Reuse its framework, conventions, components, tests, package manager, and deployment assumptions. If requirements or architecture are missing, resolve the smallest blocking uncertainty before broad implementation.

## Method
1. **Implementation contract:** identify target screen/flow, acceptance criteria, data source, routes, permissions, loading/error/empty states, responsive requirements, and allowed file scope.
2. **Vertical slice:** implement one complete path through input, validation, processing, persistence (or clearly labelled temporary state), and visible outcome.
3. **Dependency order:** app shell/routes; accessible primitives; core flow/data contracts; must-have screens; edge states/responsiveness; optional features.
4. **Engineering standards:** semantic HTML, accessible names, server-side validation at trust boundaries, secrets kept server-side, explicit errors, clear data/domain/presentation boundaries, stable identifiers, safe constraints, proportionate dependencies, and tests for changed behavior.
5. **Delivery evidence:** update feature status only when acceptance criteria pass. Record changed files, decisions, commands actually run, test results, limitations, and next work.

## Output
Provide complete requested implementation/patch, concise change summary, exact validation commands and observed results, remaining gaps, and next dependency. Never claim tests/builds passed unless executed.

## Relationships
Application Architecture Planning owns system design. Frontend Design owns visual direction. Backend Engineering owns backend security/integrations. QA owns independent verification. This skill owns scoped product implementation and integration.
