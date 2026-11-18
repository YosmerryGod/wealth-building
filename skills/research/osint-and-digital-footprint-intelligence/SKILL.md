---
name: osint-and-digital-footprint-intelligence
description: "Use when a request needs lawful open-source research and evidence collection."
triggers:
  - "jejak digital"
  - "OSINT"
  - "cek informasi publik"
  - "verifikasi identitas"
out_of_scope: "Unauthorized access, stalking, or unverified identity claims"
escalation: "Hand off work involving Unauthorized access, stalking, or unverified identity claims to its owning skill; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions; obtain user approval before external or irreversible actions."
---

# OSINT & Digital Footprint Intelligence

## Purpose

Organize public-source research into a traceable picture of an internet-facing entity, its infrastructure, public references, and observable exposure.

## Core concepts

- **Collection:** gather information from public records, DNS, certificates, search indexes, web pages, code repositories, and supported intelligence providers.
- **Normalization:** standardize domains, IP addresses, hostnames, emails, timestamps, and source metadata.
- **Correlation:** connect observations that may refer to the same entity while preserving confidence and provenance.
- **Enrichment:** add context such as hosting, technology fingerprints, reputation, and historical observations.
- **Validation:** distinguish direct observations from provider-derived claims, stale data, inference, and false positives.
- **Reporting:** summarize findings with evidence, confidence, timestamps, and recommended remediation.

## Workflow

1. Define the authorized research objective and exact scope.
2. Record target identifiers and the reason each is in scope.
3. Select collection methods and data sources appropriate to the question.
4. Collect passively where possible; record source, timestamp, query, and result.
5. Normalize and correlate entities, retaining links to original evidence.
6. Validate important findings independently and identify contradictions.
7. Prioritize exposure by likelihood, impact, and confidence.
8. Produce a report separating confirmed observations, provider claims, hypotheses, and unknowns.
9. Recommend defensive remediation and follow-up checks.

## SpiderFoot as an implementation reference

[SpiderFoot](https://github.com/smicallef/spiderfoot) is an open-source OSINT automation platform with a web UI, CLI, more than 200 modules, configurable correlation rules, visualizations, and CSV/JSON/GEXF export. It can serve as an implementation reference for modular collection and correlation workflows.

Before using it, inspect the current installation instructions, supported Python version, module configuration, API-key requirements, and data-source terms. Do not assume every module is free or works without credentials.

## Evidence quality

- Preserve the original source and collection time.
- Avoid treating a single provider result as proof of identity or ownership.
- Label confidence and explain how a relationship was inferred.
- Watch for shared hosting, recycled IPs, privacy services, stale DNS, and similarly named entities.
- Minimize collection of personal information unrelated to the stated objective.

## Source and attribution

Original knowledge synthesis based on the public documentation and feature descriptions of [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot), licensed MIT. This document does not reproduce SpiderFoot source code or modules.
