---
name: application-delivery-orchestrator
title: Application Delivery Orchestrator
category: orchestration
subcategory: product-engineering
source_type: original-adaptation-from-replica-skill
language: English
description: "Use when a user wants to investigate, design, build, test, evaluate, launch, or deploy an application as a connected project; routes the smallest next stage and maintains project continuity."
triggers: ["buat aplikasi seperti","bangun aplikasi dari referensi","clone aplikasi","rebuild aplikasi","end-to-end app","deploy aplikasi"]
out_of_scope: "Owning specialist architecture, code implementation, security, legal clearance, pricing calculations, or production execution"
escalation: "Delegate specialist methods to their owners; invoke Risk Assessment for material security, privacy, legal, financial, or production risk; obtain explicit approval before public release or live-system changes."
---

# Application Delivery Orchestrator

## Purpose
Coordinate an application project from reference investigation through architecture, design, implementation, backend integration, testing, differentiation, launch, and deployment. Maintain one coherent project state and select only the next necessary specialist. This is a routing and continuity skill, not a substitute for engineering tools or specialist methods.

## Non-negotiable rules
1. Understand the user's goal, target users, platform, primary job, scope, project state, constraints, and commitment level before routing.
2. Work one stage at a time. Do not run every phase automatically.
3. Load no more than three skills per message: this orchestrator, one lead specialist, and at most one bounded supporting skill.
4. Reuse project artifacts and decisions; do not ask the user to repeat available context.
5. Separate observed facts, sourced claims, interpretations, hypotheses, and unknowns.
6. Rebuild general functionality and UX patterns independently. Never copy proprietary code, private APIs, protected assets, distinctive brand expression, or original copy.
7. Inspect the actual repository and preserve its stack and scope. Avoid unrelated refactors.
8. A plan is not execution. Never claim code, tests, or deployment succeeded without tool evidence.
9. Require explicit approval before public release, production changes, purchases, account creation, or irreversible actions.

## Project state packet
Maintain, when project storage is available: product goal/audience/platform; scope and exclusions; reference/source inventory; screen/flow map and feature matrix; stack/schema/API/access model; design tokens/components/brand; build log; test plan and reproduced bugs; parity report; customer feedback and launch plan; deployment preflight/rollback/monitoring; decisions, risks, assumptions, provenance, and next action. Never store credentials, passwords, payment details, or private keys.

## Stage routing
| Stage | Lead owner | Handoff |
|---|---|---|
| Reference investigation | Reverse Engineering & Reference-Based Reconstruction | evidence map, screens, flows, feature matrix |
| Architecture | Application Architecture Planning | stack, schema, APIs, access model, milestones |
| Visual system | Frontend Design | tokens, components, responsive and interaction specs |
| Brand | Professional Logo & Brand Identity | distinct name/identity/voice brief |
| Product implementation | Full-Stack Application Engineering | working vertical slice and build log |
| Server capabilities | Backend Engineering & Integrations | secure data/auth/integration implementation |
| QA | Software Testing & Quality Assurance | executed tests, defects, unresolved checks |
| Comparison | Application Parity Evaluation | evidence-based coverage and differences |
| User pain/differentiation | Business Opportunity Discovery | linked feedback themes and validated hypotheses |
| Market entry | Product Launch & Go-to-Market Planning | positioning, launch assets, channels, metrics |
| Release | Application Deployment & Release Engineering | preflight, rollback, monitoring, approval gate |

Pricing calculations remain with Finance. Channel experiments remain with Growth. Risk Assessment owns material risk screening.

## Lifecycle gates
- **Scope:** identify platform, audience, core user job, must-have scope, exclusions, and success criteria. Small feature requests do not require a full product lifecycle.
- **Evidence:** record inspected sources, observed states, coverage, and unknowns. Do not treat unobserved internals as facts.
- **Architecture/design:** define data, access, API, tokens, component states, responsive behavior, and acceptance criteria.
- **Build:** prove the core journey with a thin vertical slice; expand by priority and update the feature matrix honestly.
- **Quality:** test happy paths, negative paths, permissions, accessibility, responsive behavior, security, and recovery proportionately.
- **Differentiation/launch:** use verified customer feedback; keep identity distinct and claims supportable.
- **Release:** verify preflight, backup, rollback, and monitoring; obtain explicit approval before production action.

## Decision rules
- If no reference exists and the user wants a new product, skip recon and start with scope/architecture.
- If a project exists, inspect it before proposing a stack.
- If the user is exploring, do not treat interest as build or launch approval.
- If a credential, account, permission, dependency, or tool is missing, state the blocker and next user-controlled step.
- A difference from the reference may be a deliberate improvement, not a defect.

## Final quality gate
Confirm active stage, one lead owner, reuse of artifacts, evidence/assumption separation, scope/privacy/security/IP boundaries, concrete next action, and truthful reporting of tests and external actions.
