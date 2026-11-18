---
name: application-deployment-and-release-engineering
title: Application Deployment & Release Engineering
category: development
subcategory: release-engineering
source_type: original-adaptation-from-replica-skill
language: English
description: "Use when preparing an application for staging or production, configuring hosting and domains, running release preflight, or planning rollback and monitoring."
triggers: ["deploy aplikasi","publish aplikasi","go production","hubungkan domain","rilis aplikasi","release engineering"]
out_of_scope: "Buying domains, creating accounts, entering credentials, changing live payment modes, or approving release on the user's behalf"
escalation: "Require explicit approval for production changes; use Risk Assessment for legal/privacy/security/financial risks and QA evidence as a release gate."
---

# Application Deployment & Release Engineering

## Purpose
Prepare a verified release with reproducible builds, safe environment configuration, rollback capability, and post-release monitoring.

## Method
1. **Preflight:** verify required tests/build, critical defects, reviewed migrations, environment variable documentation, secret storage, backup/restore, privacy/terms/deletion, domain/HTTPS/email/OAuth/webhooks, logging/error tracking/uptime, and truthful product identity/claims. Mark each pass, fail, not run, or N/A; missing is not pass.
2. **Staging:** deploy preview/staging first and smoke-test core flows, auth, permissions, sandbox payments, email, and integrations.
3. **Production plan:** document host, deployment method, migrations, environment variables, DNS, webhook/OAuth callbacks, backups, downtime, and rollback triggers. Use current provider documentation; do not assume DNS targets.
4. **Approval:** present results, risks, impact, and rollback. Never publish, switch live credentials, change DNS, purchase services, or make irreversible production changes without explicit user approval.
5. **Verify/monitor:** after approved release, verify public URL and critical journeys, inspect errors/latency, confirm alerts, and record release ID/time/outcome and first-week monitoring.

## Output
Evidence-backed release checklist, exact commands/results, deployment plan, rollback steps, user-owned actions, and monitoring plan. Never claim deployment succeeded without confirmation from the target environment.

## Relationships
QA owns test evidence. Backend owns backend security/integrations. Risk Assessment owns consequence screening. Application Delivery Orchestrator maintains project continuity and approval gates.
