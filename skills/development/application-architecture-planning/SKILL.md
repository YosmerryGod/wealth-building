---
name: application-architecture-planning
title: Application Architecture Planning
category: development
subcategory: software-architecture
source_type: original-adaptation-from-replica-skill
language: English
description: "Use when planning an application's technology stack, database schema, API contracts, access model, integrations, and implementation sequence."
triggers: ["arsitektur aplikasi","stack aplikasi","rancang database","schema database","desain API","application architecture"]
out_of_scope: "Visual design, detailed feature implementation, penetration testing, or production deployment"
escalation: "Hand off visual direction to Frontend Design, implementation to Full-Stack or Backend Engineering, security risk to Risk Assessment, and release to Deployment & Release Engineering."
---

# Application Architecture Planning

## Purpose
Turn approved product requirements and evidence into a practical architecture that can be built, operated, secured, and evolved without unnecessary complexity.

## Inputs
Use the recon map, feature matrix, actual repository, existing stack, team capability, budget/hosting constraints, data sensitivity, and integrations. Inspect manifests, routes, data access, migrations, and deployment config before proposing changes. Preserve working technology unless a documented constraint justifies change.

## Method
1. **System boundaries:** identify actors, roles, tenants, workflows, trust boundaries, and required quality attributes (availability, latency, accessibility, privacy, retention, backup, recovery, cost).
2. **Stack selection:** compare familiarity, ecosystem maturity, hosting fit, security support, operating cost, and exit difficulty. Prefer the simplest suitable managed architecture; avoid microservices or infrastructure without a concrete need.
3. **Data model:** define entities, fields, ownership, relationships, lifecycle, retention, keys, delete behavior, constraints, indexes, time zones, currency precision, tenant isolation, migrations, seed data, and backups.
4. **API contracts:** specify method/event, purpose, authorization, validated input, output/error contract, idempotency, rate limits, and owning flow for routes, webhooks, and jobs. Use official public APIs only.
5. **Operational risks:** assess relevant concurrency, retries, time zones, rate limits, file constraints, search, real-time/offline, email, multi-tenancy, deletion, observability, backup, and recovery.
6. **Build sequence:** prioritize a thin vertical slice, then must-haves, dependencies, integrations, and optional work. Give every milestone acceptance criteria.

## Output
Architecture document with scope, stack rationale, service boundaries, schema/ERD, API/webhook/job contracts, auth/access model, privacy/backup/observability risks, milestones, assumptions, and unresolved decisions. Do not modify the project unless implementation is requested.

## Relationships
Reverse Engineering owns evidence and feature mapping. Frontend Design owns visual system. Full-Stack and Backend Engineering own implementation. Risk Assessment owns high-consequence risk screening. Deployment & Release Engineering owns production rollout.
