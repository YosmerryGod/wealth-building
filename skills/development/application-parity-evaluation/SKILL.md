---
name: application-parity-evaluation
title: Application Parity Evaluation
category: development
subcategory: product-validation
source_type: original-adaptation-from-replica-skill
language: English
description: "Use when comparing an implementation with a reference or acceptance matrix to identify missing features, behavioral differences, and prioritized improvements."
triggers: ["bandingkan aplikasi","feature parity","apa yang kurang dari clone","cek kesesuaian aplikasi","parity check"]
out_of_scope: "Claiming pixel-perfect equivalence, replacing QA, or deciding legal permission to imitate a product"
escalation: "Use QA for reproducible bugs, Business Opportunity Discovery for customer pain/differentiation, and Risk Assessment for IP/legal concerns."
---

# Application Parity Evaluation

## Purpose
Measure whether an implementation completes intended user jobs and acceptance criteria, identify meaningful differences, and prioritize improvements. Parity means functional adequacy, not permission to copy protected expression or imitate a competitor pixel-for-pixel.

## Method
1. **Normalize comparison:** confirm current feature matrix; compare equivalent roles, data shapes, states, viewport sizes, and versions. Record unavailable or incomparable evidence.
2. **Feature coverage:** classify complete, partial, missing, or intentionally excluded with a reason. Use project priority weights; if none exist, state the scoring method. Report numerator, denominator, weights, and formula. Never invent a percentage.
3. **Experience/behavior:** compare hierarchy and structure at matching states; compare task completion, steps, errors, persistence, permissions, and recovery. Do not target colors, logos, copy, imagery, or protected identity for imitation.
4. **Improvements:** distinguish required gaps, optional parity features, user-feedback improvements, and deliberate divergences. A difference is not automatically a defect.
5. **Prioritize:** rank by impact, evidence/frequency, effort, dependencies, risk, and strategic fit. Label uncertain impact as a hypothesis.

## Output
Comparison scope, evidence coverage, feature matrix, scoring calculation, behavior differences, intentional divergences, missing requirements, prioritized next steps, and confidence/limitations.

## Relationships
Reverse Engineering owns reference evidence. QA owns reproducible defect verification. Business Opportunity Discovery owns customer pain and demand. Full-Stack implements approved gaps.
