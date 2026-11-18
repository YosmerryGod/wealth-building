---
name: software-testing-and-quality-assurance
title: Software Testing & Quality Assurance
category: development
subcategory: software-quality
source_type: original-adaptation-from-replica-skill
language: English
description: "Use when creating a test plan, reproducing bugs, testing application flows, writing automated tests, or assessing release quality."
triggers: ["test aplikasi","QA aplikasi","cari bug","buat e2e test","uji semua fitur","software testing"]
out_of_scope: "Implementing product features, approving legal compliance, or authorizing production release"
escalation: "Return reproducible defects to implementation owners; route security/privacy risks to Risk Assessment and release decisions to Deployment & Release Engineering."
---

# Software Testing & Quality Assurance

## Purpose
Verify that an application meets stated acceptance criteria through reproducible evidence. Test the user's product and authorized environments, not third-party production systems.

## Method
1. **Derive cases:** for each important flow define happy path, validation/negative cases, empty/loading/success/error states, permissions, cross-user isolation, persistence, duplicate submission, concurrency, keyboard/mobile/accessibility, and network recovery where relevant.
2. **Test levels:** use unit tests for deterministic logic, integration tests for service/data contracts, and end-to-end tests for critical journeys. Add visual regression or accessibility checks when useful. Prefer role/label selectors over brittle CSS selectors.
3. **Safe execution:** use local/staging or explicitly authorized environments with synthetic data. Never load-test, fuzz, scrape, or automate a third-party production service without authorization. Use sandbox modes for payments.
4. **Evidence:** confirmed bugs need ID, severity, exact build/environment, reproducible steps, expected/actual result, evidence with secrets removed, affected flow, and workaround. Keep unverified concerns in a separate investigation list.
5. **Fix loop:** fix critical/major defects first, add regression coverage, rerun affected tests and relevant broader suites, and state what remains untested.

## Output
Test plan, tests actually executed, pass/fail counts, reproducible defects by severity, unresolved checks, and release blockers. Do not report proposed or unexecuted tests as passed.

## Relationships
Full-Stack and Backend own implementation. Application Parity Evaluation compares requirement coverage. Deployment uses QA evidence as a release gate. Risk Assessment owns material security/privacy consequence analysis.
