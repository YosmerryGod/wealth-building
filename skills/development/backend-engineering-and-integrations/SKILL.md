---
name: backend-engineering-and-integrations
title: Backend Engineering & Integrations
category: development
subcategory: backend-engineering
source_type: original-adaptation-from-replica-skill
language: English
description: "Use when implementing authentication, authorization, databases, migrations, payments, webhooks, email, jobs, storage, or third-party API integrations."
triggers: ["buat backend","login register","integrasi API","database aplikasi","payment gateway","webhook","backend engineering"]
out_of_scope: "Frontend visual design, overall product architecture, legal certification, or release approval"
escalation: "Use Application Architecture Planning for system contracts, Risk Assessment for security/privacy/legal risks, QA for verification, and Deployment & Release Engineering for production rollout."
---

# Backend Engineering & Integrations

## Purpose
Implement reliable server-side capabilities with explicit data ownership, authorization, secrets management, failure handling, and integration boundaries.

## Method
1. **Contracts:** read approved architecture, schema, route definitions, code, and provider documentation. Identify actors, data classification, permissions, expected traffic, and failure modes. Never use undocumented private APIs of a reference product.
2. **Authentication/authorization:** use maintained mechanisms; verify identity server-side; secure sessions; enforce authorization on every read/write; test cross-user and cross-tenant isolation; support safe recovery, revocation, and deletion where applicable.
3. **Database/lifecycle:** use versioned migrations, constraints and justified indexes; define transaction/consistency/delete behavior; use synthetic seed data; document retention, export, deletion, backup, and restoration.
4. **Payments/webhooks:** use official provider APIs and user's own accounts; start in sandbox; verify signatures; persist event IDs; make handlers idempotent; keep provider state authoritative where applicable; make cancellation/refunds clear. Never request live secrets in chat.
5. **Integrations/jobs:** document provider, API version, minimum scopes, rate limits, quotas, review needs, timeout, retry, fallback, and observability. Use fresh transactional copy and idempotent jobs.
6. **Security baseline:** secrets in environment/secret manager; server validation; per-operation authorization; abuse rate limits; signature/replay protection; upload limits; no sensitive values in URLs/logs; dependency audit; data minimization and processor/retention disclosure.

A checklist does not prove an application secure. High-risk systems require qualified review and appropriate testing.

## Output
Migrations, server implementation, env variable names without values, integration notes, security checklist, tests/gaps, and operational risks. Do not create accounts, purchase services, or switch live payment modes for the user.

## Relationships
Architecture Planning owns system contracts. Full-Stack integrates backend into product flows. Risk Assessment owns consequence screening. QA owns independent verification. Deployment owns production release.
