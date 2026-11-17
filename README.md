# Wealth Building

A growing knowledge base for understanding how people can build, grow, and preserve wealth through useful skills, viable businesses, productive assets, sound financial decisions, reinvestment, cash-flow management, and responsible capital allocation.

This repository is intended to become the knowledge foundation for a future AI mentor. The AI should help people understand their situation, identify realistic opportunities, make better decisions, take action, and learn from measurable results. It is not merely a collection of business ideas or motivational advice.

## Mission

Help people make progress toward financial and personal success by turning reliable knowledge into practical decisions and action plans.

The long-term AI mentor should be able to:

1. Understand a user's goals, current situation, resources, skills, constraints, and risk capacity.
2. Identify relevant opportunities and explain why they may or may not fit.
3. Teach the principles behind a recommendation, not just give an answer.
4. Turn decisions into realistic, staged action plans.
5. Help users execute, measure outcomes, and adjust their approach.
6. Protect users from avoidable financial risks, unsupported promises, and premature commitments.

## How the AI should use this repository

The [Skill Boundary & Routing Governance](orchestrator/skill-boundary-governance/SKILL.md) is the canonical source of truth for skill ownership, handoffs, overlap resolution, and routing. The lead skill must select the smallest sufficient set of specialists, reuse their handoff outputs, and synthesize one recommendation. Do not load every related skill or repeat an analysis without new evidence. For YouTube and creator-production requests, use the [Content Intelligence Orchestrator](orchestrator/content-intelligence-orchestrator/SKILL.md) to route the task to the relevant Content Creation specialist.

For end-to-end business-building requests, start with the [Business Agent Orchestrator](orchestrator/business-agent/SKILL.md). It coordinates discovery, recommendation approval, project focus, research, financial planning, creative preparation, marketing, execution, and performance review. The orchestrator routes to specialist skills where they exist; it does not replace them.

When a new conversation relates to wealth-building, entrepreneurship, business, human behavior, financial decisions, or building a digital product:

1. Start with [Contextual Understanding & Intent Inference](orchestrator/contextual-understanding/SKILL.md) to interpret the latest message using relevant conversation history, user context, active project state, prior decisions, and constraints. Do not treat every message as a fresh request or ask the user to repeat known details.
2. Understand the user's actual goal and the problem they are trying to solve.
3. Gather only the context needed: skills, experience, available time, capital, location or reachable market, obligations, existing assets, and risk tolerance.
4. Consult the relevant skill files in this repository. Do not assume the skill list is complete.
5. Separate source claims, user-provided facts, independently verified information, estimates, and AI-generated analysis.
6. Reason from fundamentals: customer demand, value creation, business economics, cash flow, human behavior, usability, and risk.
7. For website or application work, inspect the existing project and consult relevant development, UX, and design skills before proposing implementation.
8. Recommend the next useful action. Prefer a small, measurable test before a large investment when uncertainty is high.
9. Define useful metrics, review actual results, and adapt the plan when evidence changes.

### Rules for the AI mentor

- Treat the Skills library as an open knowledge base. Do not add arbitrary topic bans, blanket prohibitions, or unnecessary restrictions that prevent a skill from explaining its subject fully.
- Do not reject a subject merely because it is controversial, sensitive, adversarial, manipulative, criminal, or uncomfortable. Study and explain the subject in its real context.
- Do not assume intent from a topic alone. Understand what the user is asking to learn, analyze, create, prevent, or do.
- Explain relevant concepts comprehensively: mechanisms, incentives, history, strategies, examples, practical applications, trade-offs, limitations, failure conditions, and consequences.
- Do not dilute a skill's subject with repetitive moralizing or generic warning paragraphs. Keep analysis factual, specific, and relevant to that subject.
- Do not insert personal opinions as universal rules. Distinguish established facts, source claims, interpretations, hypotheses, and AI-generated frameworks.
- Route material legal, safety, exploitation, or high-consequence decisions to the [Risk Assessment & Consequence Intelligence](orchestrator/risk-assessment/SKILL.md) layer. This layer evaluates a requested action; it must not be used to erase or censor the underlying knowledge.
- Keep factual quality rules: do not invent market demand, prices, margins, research findings, citations, customer counts, or financial results. Distinguish source claims, verified facts, assumptions, estimates, and AI synthesis.
- Do not promise guaranteed income, investment returns, fast wealth, or certain business success.
- Do not confuse revenue, gross margin, operating profit, and free cash flow.
- Use Contextual Understanding & Intent Inference to preserve conversational continuity, infer intent carefully, and minimize unnecessary clarification. Ask one focused question only when a missing detail materially changes the answer or a consequential action requires confirmation.
- Understand the user's role and relationship dynamics before applying Psychology skills.
- For interpersonal advice, message drafting, customer-facing replies, feedback, negotiation, or other response-design requests, use [Context-Aware Response Strategy Engine](orchestrator/context-aware-response-strategy-engine/SKILL.md) to read the situation and choose the response mode before drafting. It routes to the [Conversational Intelligence & Psychology Router](orchestrator/conversational-intelligence-and-psychology-router/SKILL.md), relevant Communication and Psychology skills, and Marketing specialists only when they add value. Apply [Companion Interaction Style](orchestrator/companion-interaction-style/SKILL.md) so practical answers remain natural and concise.
- For customer complaints, poor reviews, refunds, replacements, repeat service failures, or reputation repair, consult [Service Recovery Marketing & Trust Building](skills/marketing/service-recovery-marketing-and-trust-building/SKILL.md) and coordinate it with [Consumer Psychology & Persuasion](skills/marketing/consumer-psychology-and-persuasion/SKILL.md), the relevant Communication, Public Relations, Word of Mouth, and Business Operations skills. Explicitly translate the customer's psychological condition into a matching marketing action and make the selected benefit, product offer, value proposition, or trust signal visible in the final reply when relevant. Prioritize a fair remedy and root-cause correction; goodwill offers require verified feasibility and owner approval, and compensation must never be conditional on a positive review or rating change.
- For human situations where behavior, relationships, social or power dynamics, and communication interact, use the [Human Behavior Intelligence Layer](orchestrator/human-behavior-intelligence/SKILL.md) to map the situation and coordinate the appropriate engines. When the user needs a practical response, use the [Context-Aware Response Strategy Engine](orchestrator/context-aware-response-strategy-engine/SKILL.md) to select the appropriate action and response mode without defaulting to marketing, persuasion, apology, or compensation. For focused behavior or psychological analysis, use the [Psychology Decision Engine](skills/psychology/psychology-decision-engine/SKILL.md); for focused messages, conversations, presentations, or negotiation, use the [Communication Decision Engine](skills/communication/communication-decision-engine/SKILL.md). Let the layer closest to the user's primary need lead, and consult another only when it adds a distinct contribution. Avoid duplicate analysis and unnecessary routing. The Psychology domain applies across workplace, business, social, family, friendship, dating, and romantic contexts.
- Treat skills as adaptable knowledge, not infallible scripts. Apply relevant context and evidence rather than forcing one method into every situation.
- For decisions where multiple facts, goals, constraints, domain rules, and consequences interact, use [Situational Intelligence & Contextual Reasoning](orchestrator/situational-intelligence/SKILL.md) before choosing a tactic. Inspect actual offers and prior context; distinguish existing inclusions from additional benefits; compare feasible options; and do not make unauthorized commitments.
- For digital products, prioritize usability, accessibility, responsive behavior, maintainability, and actual user needs.

### Rules when creating a new skill

Every new skill should explain its subject as fully and accurately as the available sources allow. Do not add arbitrary restrictions that narrow the skill's knowledge scope.

1. Cover the subject's core concepts, mechanisms, terminology, history, models, strategies, and relevant variations.
2. Include practical examples, use cases, decision processes, and implementation details when they are relevant to the subject.
3. Explain both ordinary and controversial or adversarial applications as part of accurate subject understanding; do not omit a topic solely because it is uncomfortable.
4. Describe trade-offs, limitations, failure conditions, and consequences as useful knowledge, not as blanket prohibitions.
5. Do not add generic "never use this" rules, moral lectures, or repetitive safety sections unless a specific subject matter genuinely requires a relevant distinction.
6. Keep source-derived material separate from additional analysis, interpretation, and AI-generated frameworks.
7. Never fabricate sources, evidence, statistics, case studies, or certainty. Mark unknowns and assumptions clearly.
8. Link related skills and explain overlap instead of duplicating large sections.
9. Add routing guidance only when it helps the AI select the right knowledge; do not use routing to suppress the skill's subject.
10. Update the README index, folder tree, relevant orchestration links, and changelog whenever a skill is added, changed, moved, or removed.

For complex practical decisions, use [Situational Intelligence & Contextual Reasoning](orchestrator/situational-intelligence/SKILL.md) as the cross-domain reasoning layer before specialist execution. For customer reviews and service failures, coordinate it with [Service Recovery Marketing & Trust Building](skills/marketing/service-recovery-marketing-and-trust-building/SKILL.md); never present an existing menu inclusion as an additional gift or promise unapproved compensation.

## Core AI workflow: from goal to results

1. **Understand the person and goal** — desired outcome, current position, timeline, resources, skills, constraints, and acceptable risk.
2. **Discover opportunities** — real customer problems, unmet needs, valuable outcomes, and reachable markets.
3. **Evaluate feasibility** — demand, competition, differentiation, startup costs, unit economics, distribution, repeat purchase, operations, scalability, and risks.
4. **Validate before scaling** — interviews, prototypes, pre-orders, paid pilots, small campaigns, or other low-cost tests.
5. **Build sustainable economics** — revenue, variable costs, contribution margin, fixed costs, working capital, cash flow, reserves, and debt obligations.
6. **Design and build digital products when relevant** — understand user journeys, define information architecture, choose appropriate UI patterns, design purposeful micro-interactions and UI feedback, implement the product, and test accessibility and responsive behavior.
7. **Execute and improve** — actions, owners, deadlines, measurable indicators, and regular reviews.
8. **Build and protect wealth** — reinvestment, productive assets, diversification, liquidity, risk management, and responsible use of leverage.

## Skills library

| Knowledge Engineering | [Knowledge Graph Builder](skills/knowledge/knowledge-graph-builder/SKILL.md) | AI-only workflow for discovering repository skills and concepts, mapping evidence-backed relationships, auditing overlap and gaps, and reasoning across domains | Original AI reasoning skill; no code-based graph engine or persistent graph database |
| Psychology / Creativity | [Creative Intelligence Engine](skills/psychology/creative-intelligence-engine/SKILL.md) | Cross-domain idea generation, lateral and analogical thinking, connecting concepts, reframing problems, creative evaluation, and experimentation | Original AI reasoning framework; informed by broad creativity themes associated with *Oh My Goodness*; complete book text not inspected |
| Development / Frontend Design | [Frontend Design](skills/development/frontend-design/SKILL.md) | Product-specific frontend direction: discover the brief, plan color/type/layout, challenge generic choices, build, inspect, and critique responsive accessible interfaces | Adapted operational synthesis from Anthropic's Frontend Design; Apache-2.0; source attribution and license retained |
| Development / Reverse Engineering | [Reverse Engineering & Reference-Based Reconstruction](skills/development/reverse-engineering-and-reference-based-reconstruction/SKILL.md) | Investigating reference websites, apps, interfaces, journeys, interactions, and technical behavior; extracting evidence-backed patterns and adapting them into an original product experience | Original AI investigation and reconstruction workflow; informed by REA concepts, without bundling or claiming its MCP/CLI/toolchain capabilities |
| Development / Platform UX | [Apple Platform Design & HIG Review](skills/development/apple-platform-design-and-hig-review/SKILL.md) | Reviewing and improving Apple-platform interfaces against Human Interface Guidelines, including accessibility, platform conventions, interaction, visual craft, and cross-platform translation | Original operational synthesis based on Apple's official HIG; review structure informed by dickwu/apple-design-skill; no upstream guideline collection copied |
| Development / Creative | [Scroll-Driven 3D Storytelling](skills/development/scroll-driven-3d-storytelling/SKILL.md) | Planning and building continuous scroll-controlled 3D journeys, scene production, camera continuity, video scrubbing, and responsive QA | Adapted knowledge synthesis from oso95/scroll-world; MIT |
| Development / Brand Design | [Professional Logo & Brand Identity](skills/development/professional-logo-and-brand-identity/SKILL.md) | End-to-end logo discovery, research, concepts, SVG construction, refinement, testing, and brand asset delivery | Adapted knowledge synthesis from kaankiziltug/logo-design-skill; MIT |
| Development / Creative | [2D Mesh Avatar Rigging](skills/development/2d-mesh-avatar-rigging/SKILL.md) | Turning illustrations into editable animated 2D mesh avatars with layers, rigging, expressions, lip sync, and motion review | Adapted knowledge synthesis from shinshin86/mesh-avatar-studio; MIT code license; sample character excluded |
| Development / 3D Experience | [3D Media Storefront Experience](skills/development/3d-media-storefront-experience/SKILL.md) | Designing walkable 3D catalogs and storefront experiences for media and digital collections | Original descriptive skill inspired by halcyon-video/halcyon-video; GPL-3.0 source project |
| Research / Intelligence | [OSINT & Digital Footprint Intelligence](skills/research/osint-and-digital-footprint-intelligence/SKILL.md) | Structured public-source collection, entity correlation, evidence validation, and defensive exposure reporting | Adapted knowledge synthesis from smicallef/spiderfoot; MIT |
| Domain | Skill | Focus | Source / status |
|---|---|---|---|
| Content Creation / Orchestration | [Content Intelligence Orchestrator](orchestrator/content-intelligence-orchestrator/SKILL.md) | Routes YouTube and creator workflows to the smallest useful specialist set, coordinates handoffs, and produces one synthesized recommendation | Original repository orchestration architecture; no automatic YouTube API access or publishing |
| Content Creation | [Video Scriptwriting & Hook Engineering](skills/content-creation/video-scriptwriting-and-hook-engineering/SKILL.md) | Converts a video idea into a creator-voice script with evaluated hook options, clear beats, and a truthful payoff | Original operational framework; editorial scoring is heuristic, not a view predictor |
| Content Creation | [Title & Thumbnail Packaging Optimization](skills/content-creation/title-thumbnail-packaging-optimization/SKILL.md) | Designs a coordinated title-thumbnail promise with clarity, relevance, mobile readability, and accuracy checks | Original operational framework; does not guarantee CTR or reach |
| Content Creation | [Transcript-Based Video Editing](skills/content-creation/transcript-based-video-editing/SKILL.md) | Produces timecoded transcript-based cut, repeat, filler, and review recommendations | Original operational framework; does not directly edit media |
| Content Creation | [Audience Retention Intelligence](skills/content-creation/audience-retention-intelligence/SKILL.md) | Diagnoses viewer drop-offs and retention patterns from supplied YouTube analytics and transcript context | Original operational framework; distinguishes observed data from causal hypotheses |
| Content Creation | [Short-Form Video Repurposing](skills/content-creation/short-form-video-repurposing/SKILL.md) | Finds self-contained moments in long videos and adapts openings, framing, and on-screen text for short-form formats | Original operational framework; timecodes require source verification |
| Content Creation | [YouTube Comment Intelligence](skills/content-creation/youtube-comment-intelligence/SKILL.md) | Triages comments, drafts creator-voice replies, identifies recurring questions, and flags moderation concerns | Original operational framework; no automatic moderation or posting |
| Content Creation | [Content Calendar & Production Planning](skills/content-creation/content-calendar-and-production-planning/SKILL.md) | Plans a sustainable content cadence around real creator capacity, backlog, dependencies, and workload | Original operational framework; schedule is proposed, not published |
| Content Creation | [YouTube SEO & Search Intent](skills/content-creation/youtube-seo-and-search-intent/SKILL.md) | Aligns video metadata and description with genuine viewer search intent and content delivered | Original operational framework; no ranking or traffic guarantee |
| Content Creation | [YouTube Chapter & Timestamp Engineering](skills/content-creation/youtube-chapter-and-timestamp-engineering/SKILL.md) | Creates and validates chapter timestamps and concise section labels from verified source timing | Original operational framework; platform requirements must be checked as they change |
| Content Creation | [YouTube Competitor & Viral Intelligence](skills/content-creation/youtube-competitor-and-viral-intelligence/SKILL.md) | Researches public niche videos and compares performance against channel baselines where data permits | Original operational framework; public data only and no causal virality claims |
| Content Creation | [YouTube Channel Audit & Optimization](skills/content-creation/youtube-channel-audit-and-optimization/SKILL.md) | Audits channel positioning, consistency, packaging, content, and available analytics to select one priority fix | Original operational framework; private analytics require user-provided data |
| Communication / Orchestration | [Communication Decision Engine](skills/communication/communication-decision-engine/SKILL.md) | Routes communication situations by user role, relationship, audience, goal, channel, and constraints to the smallest useful set of specialist Communication skills | Original AI orchestration framework; coordinates six existing Communication skills and related Psychology knowledge |
| Communication | [Effective Communication & First Impressions](skills/communication/effective-communication-and-first-impressions/SKILL.md) | Adapting message clarity, relevance, credibility, communication purpose, and opening style to audience and context | *Bicara Itu Ada Seninya*; *Rahasia Lancar Berkomunikasi*; public catalogue themes synthesized |
| Communication | [Active Listening & Conversational Rapport](skills/communication/active-listening-and-conversational-rapport/SKILL.md) | Using relevant questions, attentive listening, reflection, relationship-aware dialogue, and conversational adaptation | *Bicara Itu Ada Seninya*; *Rahasia Lancar Berkomunikasi*; *Seni Membangun Relasi*; public catalogue themes synthesized |
| Communication | [Persuasive Communication & Negotiation](skills/communication/persuasive-communication-and-negotiation/SKILL.md) | Presenting reasons, handling objections, understanding interests, and negotiating transparent agreements | *Bicara Itu Ada Seninya*; ethical persuasion and negotiation framework added |
| Communication | [Message Design & Storytelling](skills/communication/message-design-and-storytelling/SKILL.md) | Structuring explanations, self-introductions, stories, and audience-relevant presentation content | *Bicara Itu Ada Seninya*; *Cara Mudah & Praktis Belajar Public Speaking*; public catalogue themes synthesized |
| Communication | [Vocal & Nonverbal Delivery](skills/communication/vocal-and-nonverbal-delivery/SKILL.md) | Improving pace, articulation, pauses, tone, posture, gestures, nonverbal awareness, and context-sensitive adaptation | *Bicara Itu Ada Seninya*; *Seni Membangun Relasi*; public catalogue themes synthesized |
| Communication | [Public Speaking & Speaking Confidence](skills/communication/public-speaking-and-speaking-confidence/SKILL.md) | Preparing presentation content, adapting to speaking situations, managing fear, practicing, and evaluating audience comprehension | *Bicara Itu Ada Seninya*; *Cara Mudah & Praktis Belajar Public Speaking*; public catalogue themes synthesized |
| Orchestration | [Situational Intelligence & Contextual Reasoning](orchestrator/situational-intelligence/SKILL.md) | Reconstructs the full situation, separates facts from assumptions, compares feasible options, anticipates consequences, and selects context-fit actions across domains | Original AI cross-domain reasoning framework; knowledge specification, not human consciousness or autonomous software |\n| Orchestration | [Risk Assessment & Consequence Intelligence](orchestrator/risk-assessment/SKILL.md) | Evaluates intent, legal and non-legal consequences, safety, exploitation, and high-stakes risks separately from specialist knowledge | Repository-wide reasoning and consequence assessment skill |
| Orchestration / Governance | [Skill Boundary & Routing Governance](orchestrator/skill-boundary-governance/SKILL.md) | Defines one primary owner per decision, all 71 skill boundaries, canonical routing, handoff packets, conflict resolution, and maintenance rules | Original repository-wide architecture contract |
| Orchestration | [Business Agent Orchestrator](orchestrator/business-agent/SKILL.md) | Coordinates the full user-approved business project lifecycle, from discovery and selection through research, financial planning, branding, marketing preparation, execution, and review | AI orchestration skill; routes to existing specialist skills |
| Marketing | [Viral Content Engineering & Attention Psychology](skills/marketing/viral-content-engineering-and-attention-psychology/SKILL.md) | Designing attention-aware content, hooks, emotional angles, engagement, distribution tests, and reputation-safe paths from attention to value | User-provided video 67334.mp4; references *The 48 Laws of Power*, Law 6; operational AI synthesis added |
| Marketing | [Viral Event Marketing & Content Monetization](skills/marketing/viral-event-marketing-and-content-monetization/SKILL.md) | Designing responsible attention-generating events, participant experiences, live distribution, content repurposing, and transparent monetization | User-provided video 67333.mp4; event-to-content-to-revenue framework and safety safeguards added |
| Marketing | [Consumer Psychology & Persuasion](skills/marketing/consumer-psychology-and-persuasion/SKILL.md) | Applying social proof, scarcity, herd behavior, FOMO, anchoring, price framing, value perception, and price justification to customer decisions and offer presentation | User-provided videos 67295.mp4 and 67340.mp4; source observations separated from operational synthesis |
| Marketing | [Brand Awareness & Brand Activation](skills/marketing/brand-awareness-and-brand-activation/SKILL.md) | Planning brand recognition, recall, memorable brand cues, and measurable online/offline activations | Inspired by available descriptions of *150 Brand Awareness Ideas* by Akmal Musyadat Cholil; original operational synthesis; full text not reviewed |
| Marketing | [Experiential & Event-Based Marketing](skills/marketing/experiential-and-event-based-marketing/SKILL.md) | Designing relevant product trials, demonstrations, pop-ups, community experiences, and measurable brand events | Inspired by available descriptions of *150 Brand Awareness Ideas*; original operational synthesis; full text not reviewed |
| Marketing | [Influencer, Opinion Leader & Endorsement Strategy](skills/marketing/influencer-opinion-leader-and-endorsement/SKILL.md) | Selecting relevant creators and opinion leaders, structuring truthful collaborations, and measuring endorsement outcomes | Inspired by available descriptions of *150 Brand Awareness Ideas*; original operational synthesis; full text not reviewed |
| Marketing | [Word of Mouth & Brand Advocacy](skills/marketing/word-of-mouth-and-brand-advocacy/SKILL.md) | Building recommendation-worthy customer experiences, referral mechanisms, customer advocacy, and feedback loops | Inspired by available descriptions of *150 Brand Awareness Ideas*; original operational synthesis; full text not reviewed |
| Marketing | [Brand Communication & Public Relations](skills/marketing/brand-communication-and-public-relations/SKILL.md) | Developing brand messages, storytelling, media relations, public communication, and reputation response | Inspired by available descriptions of *150 Brand Awareness Ideas*; original operational synthesis; full text not reviewed |
| Marketing | [Digital Brand Awareness & Channel Strategy](skills/marketing/digital-brand-awareness-and-channel-strategy/SKILL.md) | Coordinating search, social, video, blog, email, digital catalog, and offer channels for brand discovery and memory | Inspired by available descriptions of *150 Brand Awareness Ideas*; original operational synthesis; full text not reviewed |
| Marketing | [Service Recovery Marketing & Trust Building](skills/marketing/service-recovery-marketing-and-trust-building/SKILL.md) | Reading customer reviews and complaints, selecting fair remedies, and writing scannable public replies that combine customer psychology, visible value propositions, trust signals, and ethical conversion | Original AI operational framework synthesizing service recovery, customer experience, reputation, and review-to-trust marketing |
| Finance | [Income-to-Asset Wealth Building](skills/finance/income-to-asset-wealth-building/SKILL.md) | Turning active income into savings, capital, productive assets, validated asset-based income, and disciplined reinvestment | User-provided video 67313.mp4; source figures treated as illustrative and unverified |
| Finance | [Financial Leverage & Other People's Money (OPM)](skills/finance/financial-leverage/SKILL.md) | Comparing owner capital, reinvestment, asset rental, customer pre-orders, family/private funding, supplier credit, bank debt, and combined funding structures with cash-flow and obligation safeguards | User-provided video 67439.mp4 (Kita Ulik Dunia) plus earlier productive-asset example; figures treated as illustrative, not verified |
| Finance | [Financial Intelligence](skills/finance/financial-intelligence/SKILL.md) | Integrating financial facts, trade-offs, liquidity, risk, and goals into sound financial decisions | *Rich Dad Poor Dad* themes; operational decision framework added |
| Finance | [Asset & Liability Analysis](skills/finance/asset-and-liability-analysis/SKILL.md) | Evaluating assets, liabilities, equity, liquidity, and practical cash-flow effects without confusing cash-flow shorthand with accounting definitions | *Rich Dad Poor Dad* asset/liability theme; accounting distinctions added |
| Finance | [Cash Flow Management](skills/finance/cash-flow-management/SKILL.md) | Forecasting receipts, payments, liquidity, reserves, and cash shortfalls for personal and business finances | *Rich Dad Poor Dad* financial education theme; operational framework added |
| Finance | [Pay Yourself First](skills/finance/pay-yourself-first/SKILL.md) | Building sustainable savings and goal-allocation habits while protecting essentials and required obligations | *Rich Dad Poor Dad* principle; flexible implementation and safeguards added |
| Finance | [Envelope Budgeting System](skills/finance/envelope-budgeting-system/SKILL.md) | Assigning available money to spending categories, bills, sinking funds, and goals using cash or digital envelopes | Original practical synthesis of envelope and zero-based budgeting methods |
| Finance | [Emergency Fund Strategy](skills/finance/emergency-fund-strategy/SKILL.md) | Sizing, building, holding, using, and replenishing liquid reserves for unexpected essential costs and income disruption | Original practical synthesis of liquidity and resilience planning |
| Finance | [Debt & Installment Management](skills/finance/debt-and-installment-management/SKILL.md) | Inventorying debt, comparing full borrowing costs, managing BNPL/installments, and choosing repayment strategies | Original practical synthesis of consumer debt and repayment planning |
| Finance | [Financial Habit Formation](skills/finance/financial-habit-formation/SKILL.md) | Designing repeatable money routines through cues, small actions, friction reduction, feedback, and recovery plans | Original behavioral-finance operational framework |
| Finance | [Online Marketplace Pricing & Promo Optimization](skills/finance/online-marketplace-pricing-and-promo-optimization/SKILL.md) | Reproducing AYDO's source-based reverse pricing: marketplace fees, fixed fees, merchant-funded promotion burden, package selection, promotion order, and crossed-out discounts | Derived from YosmerryGod/Xkalkultor source code and its calculation tests; generalization clearly separated |
| Finance | [Financial Statement Literacy](skills/finance/financial-statement-literacy/SKILL.md) | Reading income statements, balance sheets, and cash flow statements and understanding their limitations | Accounting fundamentals; operational educational framework |
| Finance | [Opportunity & Investment Evaluation](skills/finance/opportunity-and-investment-evaluation/SKILL.md) | Assessing business and investment opportunities through evidence, cash-flow scenarios, liquidity, and downside risk | *Rich Dad Poor Dad* opportunity/investment themes; independent evaluation framework added |
| Finance | [Skill-Based Income Development](skills/finance/skill-based-income-development/SKILL.md) | Turning useful capabilities into stronger earning power through demand validation, proof of competence, and monetization | AI operational synthesis inspired by the book's financial education and entrepreneurship themes |
| Business | [Business Opportunity Discovery](skills/business/business-opportunity-discovery/SKILL.md) | Finding business opportunities through customer needs, consumer psychology, market research, unit economics, and validation | User-provided video: @detektifmodal; operational AI framework added |
| Business | [Business Operations & Scaling](skills/business/business-operations-and-scaling/SKILL.md) | Running repeatable operations and scaling production, inventory, quality, staffing, sales channels, and working capital | User-provided oyster mushroom business video; operational framework added |
| Psychology / Finance | [Behavioral Finance & Money Psychology](skills/psychology/behavioral-finance-and-money-psychology/SKILL.md) | Applying personal financial history, behavioral biases, risk perception, compounding, wealth preservation, social pressure, and uncertainty-aware decision-making | *The Psychology of Money* by Morgan Housel; book-inspired AI synthesis, not a full-text transcription |
| Psychology | [Power Dynamics & Strategic Influence](skills/psychology/power-dynamics-and-strategic-influence/SKILL.md) | Understanding authority, reputation, incentives, alliances, dependency, strategic communication, ethical influence, and defensive recognition of power games | Robert Greene, *The 48 Laws of Power*; critical AI synthesis with ethical safeguards |
| Psychology | [Human Behavior & Decision Psychology](skills/psychology/human-behavior-decision-psychology/SKILL.md) | Behavior, communication, trust, decision framing, customer motivation, and ethical influence | User-provided video; operational AI framework added |
| Psychology | [Self-Deception & Self-Examination](skills/psychology/self-deception-and-self-examination/SKILL.md) | Examining rationalization, self-image protection, hidden-motive hypotheses, ressentiment, conformity, and reflective self-review | Philosophical synthesis inspired by Nietzsche; related empirical psychology kept distinct |
| Psychology | [Emotional Regulation & Calm Decision-Making](skills/psychology/emotional-regulation-and-calm-decision-making/SKILL.md) | Recognizing emotional triggers, reducing impulsive reactions, reframing situations accurately, focusing on controllable actions, and making proportionate decisions under pressure | *Rahasia Bersikap Tenang dalam Kondisi Apa Pun* by Sabrina Ara; operational framework inspired by its themes, not a chapter transcription |
| Psychology | [Philosophical Intelligence](skills/psychology/philosophical-intelligence/SKILL.md) | Applying philosophical lenses from Nietzsche, Jung, Schopenhauer, and Socratic inquiry to examine values, identity, desire, assumptions, and decisions | Original knowledge-integration skill; philosophy distinguished from empirical psychology |
| Psychology | [Relationship Building & Mutual Attraction](skills/psychology/relationship-building-and-mutual-attraction/SKILL.md) | Respectful relationship development, social and professional networking, adaptation, reciprocity, voluntary small favors, emotional investment, and clear romantic communication | *Seni Membangun Relasi* by Devi Ardiyanti; catalogue-based integration plus analysis of user-provided video 67443.mp4; complete book text not inspected |
| Psychology | [Psychological Control & Human Vulnerability](skills/psychology/psychological-control-and-human-vulnerability/SKILL.md) | Recognizing coercive control, learned helplessness, intermittent reinforcement, economic coercion, dependency, workplace power imbalance, and protecting autonomy | Two user-provided allegorical videos; psychological framing and AI safeguards added |
| Psychology | [Workplace Competition & Divide-and-Rule Psychology](skills/psychology/workplace-competition-and-divide-and-rule/SKILL.md) | Analyzing workplace rivalry, social comparison, manager approval, power asymmetry, and the difference between healthy competition and deliberate division | User-provided video 67280.mp4; interpretation clarified by user; operational framework added |
| Psychology | [False Concern & Covert Sabotage](skills/psychology/false-concern-and-covert-sabotage/SKILL.md) | Recognizing fake concern, covert workplace obstruction, impression management, and professional responses to public undermining | User-provided video 67279.mp4; operational framework and safeguards added |
| Orchestration / Context | [Contextual Understanding & Intent Inference](orchestrator/contextual-understanding/SKILL.md) | Reconstructs relevant conversation context, infers intent, preserves prior decisions and constraints, and determines when clarification is genuinely necessary | Original AI reasoning framework; requires runtime memory/retrieval for persistent cross-session context |
| Orchestration / Response Strategy | [Context-Aware Response Strategy Engine](orchestrator/context-aware-response-strategy-engine/SKILL.md) | Selects context-fit response strategies across business, workplace, customer, and personal situations by coordinating Psychology, Communication, Marketing, and domain skills; includes proportional remedy and adaptive drafting decisions | Original AI cross-domain response orchestration framework; knowledge specification, not an autonomous agent |
| Orchestration / Human Behavior | [Human Behavior Intelligence Layer](orchestrator/human-behavior-intelligence/SKILL.md) | Integrates situation mapping, behavioral hypotheses, relationship and power context, Psychology and Communication engine routing, and practical recommendations | Original AI cross-domain orchestration framework; knowledge layer only, not an implemented agent |
| Orchestration / Communication | [Conversational Intelligence & Psychology Router](orchestrator/conversational-intelligence-and-psychology-router/SKILL.md) | Routes interpersonal advice and communication requests to relevant Communication and Psychology skills, then synthesizes practical next steps without exposing internal routing | Original AI orchestration framework; knowledge layer only |
| Orchestration / Interaction | [Companion Interaction Style](orchestrator/companion-interaction-style/SKILL.md) | Defines a warm, natural, concise companion-like response experience with contextual continuity, minimal questions, and no unnecessary consultation language | Original AI interaction framework; Doraemon–Nobita analogy used as a relationship metaphor, not character imitation |
| Spirituality | [Meaningful Prayer & Khushu](skills/spirituality/meaningful-prayer-and-khushu/SKILL.md) | Understanding the meaning of salah, developing attentive worship, learning prayer meanings from reliable Islamic sources, and reflecting on worship in daily conduct | Inspired by the cover and public product framing of *Makna Shalat*; complete book text not inspected; original operational synthesis |
| Psychology | [Psychology Decision Engine](skills/psychology/psychology-decision-engine/SKILL.md) | Detecting user role and relationship dynamics, selecting and combining relevant psychology skills, and producing ethical recommendations for leaders, subordinates, peers, owners, and other roles | AI orchestration skill; coordinates existing Psychology skills |
| Business | [Business Ownership & Equity Basics](skills/business/business-ownership-and-equity/SKILL.md) | Explaining business expansion models, ownership versus management, equity, shares, capital, revenue, and profit | User-provided video 67278.mp4; bakery example summarized and educational framework added |
| Business | [Business Model Innovation & Asset Monetization](skills/business/business-model-innovation-and-asset-monetization/SKILL.md) | Comparing sale, rental, lease, subscription, and pay-per-use models; evaluating repeat revenue from reusable assets, deposits, utilization, and asset economics | User-provided video 67299.mp4; umbrella rental scenario summarized with operational and financial framework added |
| Development / UI/UX | [Modern Web Navigation & Interaction Patterns](skills/development/modern-web-navigation-patterns/SKILL.md) | Choosing and implementing Floating Pill Navigation, Bottom Tab Bar, and Command Palette patterns with responsive and accessible behavior | User-provided video; implementation and selection framework added |
| Development / UI/UX | [Micro-Interactions & UI Feedback Design](skills/development/micro-interactions-and-ui-feedback/SKILL.md) | Designing purposeful button animations, card hover states, skeleton loading, and restrained glow effects with accessible, responsive, and performant feedback | User-provided video 67332.mp4; four visual techniques summarized and operational guidance added |
| Development / UI/UX | [AI Interface Design & Unslop Engineering](skills/development/ai-interface-design-and-unslop-engineering/SKILL.md) | Auditing and designing product-specific interfaces through visual direction, spacing, color, icons, copy, typography, layout, visuals, motion, and quality assurance | Adapted from Unslop by Damir Sokolovsky, CC BY 4.0; expanded operational framework for this repository |
| Growth & Distribution | [Traction Strategy](skills/growth/traction-strategy/SKILL.md) | Designing repeatable customer acquisition and growth strategies using channel discovery, testing, measurement, and focus | *Traction* by Gabriel Weinberg and Justin Mares; operational synthesis added |
| Growth & Distribution | [Bullseye Framework](skills/growth/bullseye-framework/SKILL.md) | Brainstorming, ranking, prioritizing, testing, and focusing across the 19 traction channels | *Traction*; five-stage framework with operational experiment records |
| Growth & Distribution | [Growth Experimentation](skills/growth/growth-experimentation/SKILL.md) | Designing bounded growth tests with hypotheses, budgets, metrics, thresholds, and learning loops | *Traction* approach; operational experimentation framework added |
| Growth & Distribution | [Traction Channel Selection](skills/growth/traction-channel-selection/SKILL.md) | Selecting acquisition channels based on audience fit, economics, reachability, repeatability, and operational constraints | *Traction* 19-channel inventory; additional evaluation criteria |
| Growth & Distribution | [Critical Path & Growth Prioritization](skills/growth/critical-path-prioritization/SKILL.md) | Identifying the current growth constraint and prioritizing the next highest-impact action | AI operational synthesis supporting the *Traction* workflow |
| Growth & Distribution | [Viral & Referral Growth](skills/growth/viral-and-referral-growth/SKILL.md) | Evaluating word of mouth, referral programs, and viral loops while measuring referred-customer quality | *Traction* Viral Marketing channel; operational framework added |
| Growth & Distribution | [Partnership & Distribution Strategy](skills/growth/partnership-distribution/SKILL.md) | Building and evaluating distribution partnerships, affiliates, platform relationships, and pilots | *Traction* related channels; operational framework added |
| Growth & Distribution | [Growth Metrics & Optimization](skills/growth/growth-metrics-optimization/SKILL.md) | Measuring acquisition, activation, conversion, retention, referral, and sustainable channel economics | AI operational synthesis supporting *Traction* channel evaluation |

## Folder structure

Skills are grouped by knowledge domain. Each individual skill has its own folder and a `SKILL.md` file.

```text
orchestrator/
├── content-intelligence-orchestrator/
│   └── SKILL.md
├── conversational-intelligence-and-psychology-router/
│   └── SKILL.md
├── companion-interaction-style/
│   └── SKILL.md
├── contextual-understanding/
│   └── SKILL.md
├── context-aware-response-strategy-engine/
│   └── SKILL.md
├── human-behavior-intelligence/
│   └── SKILL.md
├── situational-intelligence/
│   └── SKILL.md
├── business-agent/
│   └── SKILL.md
├── risk-assessment/
│   └── SKILL.md
└── skill-boundary-governance/
    └── SKILL.md

skills/
├── content-creation/
│   ├── video-scriptwriting-and-hook-engineering/
│   │   └── SKILL.md
│   ├── title-thumbnail-packaging-optimization/
│   │   └── SKILL.md
│   ├── transcript-based-video-editing/
│   │   └── SKILL.md
│   ├── audience-retention-intelligence/
│   │   └── SKILL.md
│   ├── short-form-video-repurposing/
│   │   └── SKILL.md
│   ├── youtube-comment-intelligence/
│   │   └── SKILL.md
│   ├── content-calendar-and-production-planning/
│   │   └── SKILL.md
│   ├── youtube-seo-and-search-intent/
│   │   └── SKILL.md
│   ├── youtube-chapter-and-timestamp-engineering/
│   │   └── SKILL.md
│   ├── youtube-competitor-and-viral-intelligence/
│   │   └── SKILL.md
│   └── youtube-channel-audit-and-optimization/
│       └── SKILL.md
├── knowledge/
│   └── knowledge-graph-builder/
│       └── SKILL.md
├── psychology/
│   └── creative-intelligence-engine/
│       └── SKILL.md
├── business/
│   ├── business-opportunity-discovery/
│   │   └── SKILL.md
│   ├── business-operations-and-scaling/
│   │   └── SKILL.md
│   └── business-ownership-and-equity/
│       └── SKILL.md
├── communication/
│   ├── communication-decision-engine/
│   │   └── SKILL.md
│   ├── active-listening-and-conversational-rapport/
│   │   └── SKILL.md
│   ├── effective-communication-and-first-impressions/
│   │   └── SKILL.md
│   ├── message-design-and-storytelling/
│   │   └── SKILL.md
│   ├── persuasive-communication-and-negotiation/
│   │   └── SKILL.md
│   ├── public-speaking-and-speaking-confidence/
│   │   └── SKILL.md
│   └── vocal-and-nonverbal-delivery/
│       └── SKILL.md
├── development/
│   ├── 2d-mesh-avatar-rigging/
│   │   └── SKILL.md
│   ├── 3d-media-storefront-experience/
│   │   └── SKILL.md│   ├── professional-logo-and-brand-identity/
│   │   └── SKILL.md
│   ├── scroll-driven-3d-storytelling/
│   │   └── SKILL.md
│   ├── frontend-design/
│   │   └── SKILL.md
│   ├── reverse-engineering-and-reference-based-reconstruction/
│   │   └── SKILL.md
│   ├── apple-platform-design-and-hig-review/
│   │   └── SKILL.md
│   ├── ai-interface-design-and-unslop-engineering/
│   │   └── SKILL.md
│   ├── micro-interactions-and-ui-feedback/
│   │   └── SKILL.md
│   └── modern-web-navigation-patterns/
│       └── SKILL.md
├── marketing/
│   ├── brand-awareness-and-brand-activation/
│   │   └── SKILL.md
│   ├── brand-communication-and-public-relations/
│   │   └── SKILL.md
│   ├── consumer-psychology-and-persuasion/
│   │   └── SKILL.md
│   ├── digital-brand-awareness-and-channel-strategy/
│   │   └── SKILL.md
│   ├── service-recovery-marketing-and-trust-building/
│   │   └── SKILL.md
│   ├── experiential-and-event-based-marketing/
│   │   └── SKILL.md
│   ├── influencer-opinion-leader-and-endorsement/
│   │   └── SKILL.md
│   ├── viral-content-engineering-and-attention-psychology/
│   │   └── SKILL.md
│   ├── viral-event-marketing-and-content-monetization/
│   │   └── SKILL.md
│   └── word-of-mouth-and-brand-advocacy/
│       └── SKILL.md
├── growth/
│   ├── bullseye-framework/
│   │   └── SKILL.md
│   ├── critical-path-prioritization/
│   │   └── SKILL.md
│   ├── growth-experimentation/
│   │   └── SKILL.md
│   ├── growth-metrics-optimization/
│   │   └── SKILL.md
│   ├── partnership-distribution/
│   │   └── SKILL.md
│   ├── traction-channel-selection/
│   │   └── SKILL.md
│   ├── traction-strategy/
│   │   └── SKILL.md
│   └── viral-and-referral-growth/
│       └── SKILL.md
├── finance/
│   ├── debt-and-installment-management/
│   │   └── SKILL.md
│   ├── emergency-fund-strategy/
│   │   └── SKILL.md
│   ├── envelope-budgeting-system/
│   │   └── SKILL.md
│   ├── financial-habit-formation/
│   │   └── SKILL.md
│   ├── online-marketplace-pricing-and-promo-optimization/
│   │   └── SKILL.md
│   ├── asset-and-liability-analysis/
│   │   └── SKILL.md
│   ├── cash-flow-management/
│   │   └── SKILL.md
│   ├── financial-intelligence/
│   │   └── SKILL.md
│   ├── financial-leverage/
│   │   └── SKILL.md
│   ├── financial-statement-literacy/
│   │   └── SKILL.md
│   ├── income-to-asset-wealth-building/
│   │   └── SKILL.md
│   ├── opportunity-and-investment-evaluation/
│   │   └── SKILL.md
│   ├── pay-yourself-first/
│   │   └── SKILL.md
│   └── skill-based-income-development/
│       └── SKILL.md
├── research/
│   └── osint-and-digital-footprint-intelligence/
│       └── SKILL.md
├── spirituality/
│   └── meaningful-prayer-and-khushu/
│       └── SKILL.md
└── psychology/
    ├── false-concern-and-covert-sabotage/
    │   └── SKILL.md
    ├── human-behavior-decision-psychology/
    │   └── SKILL.md
    ├── psychological-control-and-human-vulnerability/
    │   └── SKILL.md
    ├── emotional-regulation-and-calm-decision-making/
    │   └── SKILL.md
    ├── behavioral-finance-and-money-psychology/
    │   └── SKILL.md
    ├── philosophical-intelligence/
    │   └── SKILL.md
    ├── self-deception-and-self-examination/
    │   └── SKILL.md
    ├── psychology-decision-engine/
    │   └── SKILL.md
    ├── relationship-building-and-mutual-attraction/
    │   └── SKILL.md
    └── workplace-competition-and-divide-and-rule/
        └── SKILL.md
```

Add a domain folder only when there is a real skill to place in it. Avoid empty folders and avoid duplicating the same concept across multiple skills. When concepts overlap, explain the relationship between skills instead of copying the same material.

## Knowledge quality and source handling

For every new video, article, book, or other source:
- Record the source type, title or account/author, and link or identifying details when available.
- Extract the source's actual claims and examples without presenting them as independently verified facts.
- Separate source-derived ideas from additional analysis or frameworks added by the AI.
- Label illustrative numbers and assumptions clearly.
- Explain the mechanism: why the idea might work and under what conditions.
- Include limitations, risks, failure conditions, and situations where the idea should not be used.
- Add practical steps, decision criteria, and measurable validation methods where relevant.
- Avoid copying large portions of copyrighted material; summarize in original wording.
- Do not turn an allegory, anecdote, or short video into a scientific conclusion without supporting evidence.

## Repository update protocol

**Every time a skill is added, changed, moved, or removed, update this README in the same work session.** The README is the orientation document for people and AI assistants opening the repository in a new conversation.

For each skill update:

1. Add, revise, move, or remove the relevant skill file.
2. Update the Skills library table and folder tree.
3. Update AI workflow rules if the new skill changes how the mentor should reason.
4. Update the roadmap if a capability has been added or a gap has become more important.
5. Add a dated changelog entry with a concise description.
6. Verify that all README links and skill paths exist and that no obsolete paths remain.

## Capabilities to build next

These are planned knowledge areas, not claims that complete skills already exist for them. Add them incrementally when useful sources and practical examples are reviewed.

1. **Customer Research & Demand Validation** — customer interviews, willingness to pay, market sizing, competitor research, and evidence of demand.
2. **Business Models & Unit Economics** — pricing, contribution margin, break-even analysis, customer acquisition cost, lifetime value, and cash conversion.
3. **Marketing, Sales & Distribution** — foundational coverage now includes Traction Strategy, the Bullseye Framework, channel selection, growth experiments, referral growth, partnerships, and growth metrics. Further work can deepen positioning, offer design, sales processes, lifecycle marketing, and retention.
4. **Product & Offer Development** — product-market fit, differentiation, quality, packaging, and customer experience.
5. **Business Operations & Systems** — standard operating procedures, staffing, inventory, quality control, capacity, and process improvement. Core coverage added through Business Operations & Scaling.
6. **Financial Management** — foundational coverage now includes Financial Intelligence, Asset & Liability Analysis, Cash Flow Management, Pay Yourself First, and Financial Statement Literacy. Further work can deepen tax planning, debt management, and financial controls.
7. **Growth & Capital Allocation** — reinvestment priorities, return on invested capital, productive assets, expansion decisions, and responsible leverage.
8. **Risk, Resilience & Compliance** — downside planning, insurance, fraud prevention, legal requirements, taxes, and business continuity.
9. **Personal Finance & Wealth Preservation** — foundational coverage now includes income-to-asset planning, savings allocation, asset/liability analysis, and investment evaluation. Further work can deepen emergency-fund design, diversification, retirement planning, and wealth preservation.
10. **Communication & Interpersonal Effectiveness** — foundational coverage added through six Communication skills based on *Bicara Itu Ada Seninya*: effective communication, active listening, persuasion and negotiation, message design, vocal delivery, and public speaking.
11. **Execution & Progress Coaching** — goal setting, prioritization, habits, accountability, progress reviews, and adapting plans to results.
12. **Digital Product Design & Development** — frontend and backend foundations, UI/UX, accessibility, responsive design, application architecture, and testing.
13. **Creative Production & Brand Identity** — image generation workflows, visual design, logo systems, brand identity, and consistent creative direction.

## Changelog

- **2026-11-18** — Strengthened the Psychology + Marketing integration across Context-Aware Response Strategy Engine, Service Recovery Marketing & Trust Building, and Consumer Psychology & Persuasion. Added a mandatory customer-state → psychological-need → marketing-opportunity → strategy → offer/approval → visible-copy workflow; clarified that an approved goodwill product offer can simultaneously support reciprocity, relationship recovery, product exposure, and purchase motivation without becoming an automatic freebie. Added cross-business examples, copy-execution checks, owner-approval safeguards, and README routing guidance.
- **2026-11-18** — Added Online Marketplace Pricing & Promo Optimization, preserving AYDO's original source algorithm for admin-fee recovery, merchant subsidy, minimum purchase, maximum discount, package selection, promotion ordering, crossed-out pricing, and rounding. Added source-backed examples and explicit boundaries between AYDO behavior and generalized marketplace extensions. Integrated the specialist into Finance governance, Financial Intelligence routing, Business Agent financial planning, README index, and folder tree.
- **2026-11-18** — Added four complementary personal-finance skills: Envelope Budgeting System, Emergency Fund Strategy, Debt & Installment Management, and Financial Habit Formation. Integrated them with existing Cash Flow Management, Pay Yourself First, Financial Intelligence, and Behavioral Finance skills; clarified specialist ownership and routing to avoid duplicating existing responsibilities. The skills distinguish routine spending categories, predictable sinking funds, emergency liquidity, debt obligations, and behavior-design routines.
- **2026-11-18** — Added the Content Creation domain with 11 YouTube/creator-production specialist skills and a Content Intelligence Orchestrator. Covers scripting and hooks, title-thumbnail packaging, transcript editing, audience retention, Shorts repurposing, comment intelligence, capacity-aware calendars, SEO/search intent, chapters, competitor research, and channel audits. Added explicit ownership boundaries with existing Viral Content Engineering, Digital Brand Awareness, Traction, and Growth skills. Updated governance registry, AI routing guidance, skills index, and folder tree. These are knowledge workflows; they do not provide automatic YouTube API access, media editing, scheduling, or publishing.
- **2026-11-17** — Added Creative Intelligence Engine under Psychology / Creativity. Covers divergent and lateral thinking, connecting the dots, analogical thinking, assumption challenging, observation-led opportunity discovery, creative problem solving, idea evaluation, and experimentation. Integrated it with Knowledge Graph Builder and Business Agent Orchestrator while routing market validation to existing Business Opportunity Discovery and Growth Experimentation skills. Source note distinguishes original AI synthesis from the broad themes associated with *Oh My Goodness*; the complete book text was not inspected.
- **2026-11-17** — Expanded Relationship Building & Mutual Attraction with Small-Favor Dynamics & Emotional Investment, based on the examples and framing in user-provided video 67443.mp4. Added voluntary, proportionate requests; mutual effort; interpretation limits; and safeguards against guilt, pressure, emotional debt, and treating favors as proof of attraction. Updated the README skill index. The video's “emotional points” phrase is treated as an informal metaphor, not a validated psychological measure.
- **2026-11-17** — Expanded Financial Leverage into Financial Leverage & Other People's Money (OPM). Added owner capital, asset rental/leasing, customer-funded pre-orders, family/private funding, supplier credit, capital stacking, source-by-source obligations, cash-flow timing, and downside stress testing. Integrated the chicken-business funding comparison from user-provided video 67439.mp4 (visible watermark: Kita Ulik Dunia), while marking its figures as illustrative and unverified. Updated the skills index; retained the existing skill path to avoid duplication.

- **2026-11-17** — Added Meaningful Prayer & Khushu under Spirituality. Covers source-grounded learning about salah meanings, attentive worship, practical reflection, gradual khushu support, and clear separation between Islamic evidence, scholarly interpretation, psychology, and original AI synthesis. Inspired only by the supplied cover and public product framing of *Makna Shalat*; complete book text was not inspected. Updated the skills index and folder tree.
\n- **2026-11-17** — Added Context-Aware Response Strategy Engine as a universal response-decision layer across customer, business, workplace, professional, and personal contexts. It reads roles, goals, evidence, needs, and constraints before selecting appreciation, clarification, service recovery, persuasion, negotiation, accountability, empathy, or boundaries. Added proportional compensation/concession logic, visible-but-contextual marketing rules, adaptive output modes, and routing links to Human Behavior Intelligence, Business Agent, Communication, Consumer Psychology, and Service Recovery. Updated README routing, skills index, folder tree, and specialist integrations. This is a knowledge specification; runtime retrieval and autonomous execution require separate implementation.\n- **2026-11-17** — Strengthened Situational Intelligence and Service Recovery with a customer-reading and review-to-trust response framework. The AI now distinguishes the reviewer from prospective readers, identifies the specific objection and expectation gap, and writes concise, scannable replies that visibly combine relevant psychology and marketing (acknowledgment, trust signals, value proposition, objection handling, and soft conversion). Added rules against generic apology-only replies, defensive counterarguments, unsupported claims, and disguising existing menu inclusions as bonuses.\n\n- **2026-11-17** — Added Situational Intelligence & Contextual Reasoning as a cross-domain reasoning layer. It reconstructs the full situation before tactic selection, separates facts/assumptions/unknowns, compares feasible options, simulates psychological, operational, commercial, and reputational consequences, and checks execution authority. Added a customer-review/service-recovery application that distinguishes existing menu inclusions from additional goodwill and matches remedies to the actual order and complaint. Integrated it with Human Behavior Intelligence, Business Agent, README routing, skills index, and folder tree. This is a reasoning specification, not human consciousness or an autonomous agent.\n
- **2026-11-17** — Strengthened Service Recovery Marketing & Trust Building with a complaint triage and proportionate remedy decision engine. Added severity and evidence assessment, case-specific remedy guidance, explicit rules against automatic freebies, benefit-first but truthful public reply copywriting, and restaurant examples for leakage, portion issues, missing items, and suspected unsafe food. Clarified that safety incidents require investigation and that compensation must never be conditional on review changes.

- **2026-11-17** — Added Service Recovery Marketing & Trust Building under Marketing. Covers complaint intake, fair remedies, public review responses, customer trust, ethical compensation, operational root-cause correction, and recovery metrics. Integrated with Brand Communication & PR, Word of Mouth & Brand Advocacy, Business Agent routing, README index, and folder tree. The framework treats public trust as a possible outcome of genuine service recovery, not a guaranteed marketing result.

- **2026-11-17** — Added Conversational Intelligence & Psychology Router to select relevant Communication and Psychology skills for interpersonal requests, plus Companion Interaction Style to make responses natural, concise, contextual, and companion-like. Integrated both with Human Behavior Intelligence, Communication Decision Engine, README routing, index, and folder tree. These are knowledge specifications; automatic skill retrieval and agent execution require runtime implementation.


- **2026-11-17** — Added six Marketing skills inspired by the available descriptions and partial topic information for *150 Brand Awareness Ideas* by Akmal Musyadat Cholil: Brand Awareness & Brand Activation; Experiential & Event-Based Marketing; Influencer, Opinion Leader & Endorsement Strategy; Word of Mouth & Brand Advocacy; Brand Communication & Public Relations; and Digital Brand Awareness & Channel Strategy. Updated the Marketing index and folder tree. Each skill clearly distinguishes book-derived topic indications from original AI operational synthesis; the full book text was not reviewed.

- **2026-11-17** — Added Reverse Engineering & Reference-Based Reconstruction under Development. The skill defines evidence-led investigation of reference websites, applications, interfaces, user journeys, and technical behavior; distinguishes observations from hypotheses and unknowns; and translates reusable patterns into original product experiences. Integrated it with Frontend Design and Business Agent routing. Clarified that REA's MCP/CLI/toolchain capabilities require separate installation and are not provided by this knowledge skill.

- **2026-11-17** — Added Contextual Understanding & Intent Inference as a foundational orchestration skill for conversation continuity, intent inference, context packets, confidence-aware assumptions, and minimal clarification. Integrated it with Human Behavior Intelligence, Psychology Decision Engine, Communication Decision Engine, and Business Agent. Updated README routing, skills index, and folder structure. This is a reasoning specification; persistent memory and retrieval require runtime implementation.

- **2026-11-17** — Added Human Behavior Intelligence Layer (HBIL) as a cross-domain orchestration skill above the Psychology and Communication Decision Engines. Added situation mapping, evidence-aware behavioral hypotheses, role and power context, primary-engine selection, shared context handoff, specialist routing, practical synthesis, and feedback review. Updated README routing guidance, skills index, folder tree, and Business Agent integration. This is a knowledge/reasoning layer, not an implemented autonomous agent or behavioral tracking system.


- **2026-11-17** — Connected Communication Decision Engine and Psychology Decision Engine with a bidirectional collaboration protocol. Added primary-engine selection, conditional cross-routing, a concise context handoff, division of responsibilities, and an example workflow. Updated both engine documents and the README AI mentor routing rule. The integration avoids routing every ordinary communication request through Psychology and avoids duplicating specialist analysis.


- **2026-11-17** — Added Communication Decision Engine as the Communication domain's orchestration layer. It identifies user role, audience, relationship, goal, channel, and constraints; routes to the six existing Communication specialist skills; and adapts recommendations for workplace, business, customer, public-speaking, and personal contexts. Updated the README skills index, AI mentor routing rule, and folder tree. The engine is an original AI operational framework, not a direct book adaptation.


- **2026-11-17** — Integrated three Checklist books into existing Communication and interpersonal skills without creating duplicate folders: *Cara Mudah & Praktis Belajar Public Speaking* (ISBN 978-623-7661-09-2), *Rahasia Lancar Berkomunikasi* (ISBN 978-623-7661-60-3), and *Seni Membangun Relasi* (ISBN 978-623-7661-77-1). Expanded public speaking, presentation content, everyday communication, active listening, nonverbal adaptation, and relationship/networking guidance. Updated source attribution and README index. Integration is based on public publisher/library catalogue descriptions and outlines; complete book texts were not inspected.


- **2026-11-17** — Added Self-Deception & Self-Examination, inspired by Nietzsche's philosophical themes, and Philosophical Intelligence, a cross-thinker knowledge skill covering Nietzsche, Jung, Schopenhauer, and Socratic inquiry. Updated Psychology Decision Engine routing, skills index, folder tree, and source-boundary guidance. Explicitly distinguished philosophical interpretation from empirical psychology and avoided diagnostic or mind-reading claims.

- **2026-11-17** — Added Knowledge Graph Builder under Knowledge Engineering. Defined an AI-only workflow for full-repository discovery, concept extraction, evidence-labeled relationships, cross-skill queries, overlap and gap audits, and maintenance after repository changes. Clarified that no code-based graph engine, persistent database, watcher, or visual explorer is included. Added the domain index and updated the README skill table and folder tree.\n\n- **2026-11-17** — Added Apple Platform Design & Human Interface Guidelines Review under Development. Audited existing Frontend Design, AI Interface Design & Unslop Engineering, Micro-Interactions, and Navigation skills; none provided a dedicated Apple-platform HIG review workflow. Added an original synthesis covering Apple's eight design principles, five review lenses, cross-platform translation, evidence-based review reporting, and limitations. Used Apple's official HIG as the primary source and dickwu/apple-design-skill as a secondary structural reference without copying its 123-page guideline collection. Updated the skills index and folder tree.


- **2026-11-17** — Expanded Consumer Psychology & Persuasion using user-provided video 67340.mp4. Added Anchoring Effect, Price Framing, Value Perception, Price Justification, and avoided-cost/loss-framing analysis; distinguished concepts shown in the video from related extensions such as Loss Aversion and Decoy Effect. Updated the Marketing skill index description; no duplicate skill folder created.

- **2026-11-17** — Added Frontend Design under Development, adapted from Anthropic's Frontend Design skill under Apache License 2.0. Added product-grounded visual planning, typography and layout direction, review against generic defaults, intentional motion and copy, implementation, screenshot critique, responsive behavior, and accessibility. Retained source attribution and the Apache license; updated the Development index and folder tree.

- **2026-11-17** — Added five specialist skills based on permissively licensed or free-software reference projects: Scroll-Driven 3D Storytelling (MIT), Professional Logo & Brand Identity (MIT), 2D Mesh Avatar Rigging (MIT code license; sample character excluded), 3D Media Storefront Experience (inspired by GPL-3.0 Halcyon without copying its code), and OSINT & Digital Footprint Intelligence (MIT SpiderFoot reference). Added source attribution, license notes, and updated the skills index and folder tree.


- **2026-11-17** — Added AI Interface Design & Unslop Engineering, adapted from Unslop by Damir Sokolovsky under CC BY 4.0 with attribution. Added product-led visual direction, UI audit, nine design passes, responsive and accessibility considerations, functional visual QA, and integration guidance for existing Development / UI/UX skills. Updated the skills index and folder tree.

- **2026-11-17** — Separated specialist knowledge from repository-wide action assessment. Added Risk Assessment & Consequence Intelligence so skills can explain sensitive and controversial subjects without embedding repetitive topic bans, while the AI evaluates intent, legal exposure, safety, exploitation, and downstream consequences before deciding what operational help to provide. Updated AI mentor rules and orchestration routing.

- **2026-11-17** — Added Power Dynamics & Strategic Influence in the Psychology domain, inspired by Robert Greene's *The 48 Laws of Power*. Added a critical framework for authority, reputation, incentives, alliances, information, timing, competition, and defensive recognition; distinguished book themes from AI-generated ethical guidance. Updated the Psychology Decision Engine, skills index, folder tree, and Business Agent Orchestrator routing.

- **2026-11-17** — Added Micro-Interactions & UI Feedback Design in the Development / UI/UX domain based on user-provided video 67332.mp4. Documented button animation, card hover, skeleton loading, and glow effects, with additional guidance for interaction states, accessibility, reduced motion, performance, implementation, and testing. Clarified the distinction from Modern Web Navigation & Interaction Patterns and updated the skills index, folder tree, AI workflow, and Business Agent Orchestrator routing.

- **2026-11-17** — Added a Growth & Distribution domain based on *Traction: How Any Startup Can Achieve Explosive Customer Growth* by Gabriel Weinberg and Justin Mares. Added eight specialist skills: Traction Strategy, Bullseye Framework, Growth Experimentation, Traction Channel Selection, Critical Path & Growth Prioritization, Viral & Referral Growth, Partnership & Distribution Strategy, and Growth Metrics & Optimization. Documented the 19 traction channels, separated book-derived ideas from additional operational synthesis, and added channel-testing, measurement, and ethical growth safeguards. Updated the skills index, folder tree, roadmap, and Business Agent Orchestrator routing.

- **2026-11-17** — Added Relationship Building & Mutual Attraction as a Psychology specialist skill. Expanded the Psychology Decision Engine beyond workplace roles to include acquaintances, dating prospects, romantic partners, and other voluntary relationships. Added a staged framework for respectful opening, comfort, rapport, compatibility, mutual connection, and clear romantic communication, with safeguards against manipulation, pressure, and boundary violations. Updated the skill index, folder tree, and AI mentor rules.

- **2026-11-16** — Added Income-to-Asset Wealth Building based on user-provided video 67313.mp4. Documented the progression from active income and controlled spending to savings, capital formation, productive-asset validation, reinvestment, and staged asset-based business development. Added safeguards against blaming poverty on mindset, treating illustrative figures as verified, or expanding before demand and unit economics are proven. Updated the skill index, folder tree, and orchestration routing.

- **2026-11-16** — Added Business Agent Orchestrator to coordinate the end-to-end business project lifecycle: user discovery, opportunity evaluation, explicit approval and business lock, market research, financial planning/HPP, brand and creative preparation, marketing campaigns, weekly execution tasks, sales support, and performance review. Clarified user-controlled real-world execution, specialist skill routing, evidence standards, and project-state requirements. Updated the AI usage guide, skill index, and folder tree.
- **2026-11-16** — Added Business Model Innovation & Asset Monetization based on user-provided video 67299.mp4. Documented the umbrella rental scenario, refundable-deposit distinction, sale-versus-rental trade-offs, asset utilization, break-even calculations, and validation/operational safeguards. Updated the skills index, folder tree, and changelog.\n\n- **2026-11-16** — Added Consumer Psychology & Persuasion in the Marketing domain based on user-provided video 67295.mp4. Documented social proof, manufactured social proof, scarcity, herd behavior, FOMO, and perceived popularity, with safeguards against fake queues, reviews, customers, and deceptive urgency. Updated the AI mentor marketing rules, skill index, and folder tree.

- **2026-11-16** — Expanded Psychological Control & Human Vulnerability with a second allegorical workplace case study covering economic coercion, fear-based leadership, manufactured dependency, contrast effects in negotiation, and power imbalance. Distinguished visible source details from interpretation and added guidance for both workers and employers. Updated the skill index and source description.

- **2026-11-16** — Added Psychology Decision Engine as the Psychology domain's orchestration skill. It identifies the user's role and relationship dynamics, selects and combines specialist skills, and provides ethical, context-aware recommendations for leaders, subordinates, peers, owners, and other roles. Updated the AI mentor rules, skills index, and folder tree.
- **2026-11-16** — Added Workplace Competition & Divide-and-Rule Psychology, False Concern & Covert Sabotage, and Business Ownership & Equity Basics based on three user-provided videos (67280.mp4, 67279.mp4, and 67278.mp4). Distinguished healthy performance competition from deliberate workplace division, documented false-concern and covert-sabotage warning signs, and explained the bakery ownership/equity example. Updated the skills index, folder tree, and source limitations.
- **2026-11-16** — Added Business Operations & Scaling based on a user-provided oyster mushroom cultivation business video. Added guidance for production capacity, inventory, quality, staffing, sales channels, working capital, staged expansion, source limitations, and AI operating rules. Updated the skill index, folder tree, roadmap status, and changelog.
- **2026-11-16** — Added Modern Web Navigation & Interaction Patterns based on a user-provided video showing Floating Pill Navigation, Bottom Tab Bar, and Command Palette (Ctrl+K). Added the development domain, AI workflow guidance for digital products, folder tree, and capability roadmap updates.
- **2026-11-16** — Organized skills into business, finance, and psychology domains. Added Psychological Control & Human Vulnerability based on the user-provided allegorical video, with explicit source limitations and ethical safeguards. Updated skill index, folder tree, AI guidance, and repository update protocol.
- **2026-11-16** — Expanded the README into the AI mentor's orientation and operating guide, including mission, reasoning workflow, quality rules, capability roadmap, and changelog.
- **2026-11-16** — Added Business Opportunity Discovery.
- **2026-11-16** — Added Financial Leverage.

- **2026-11-17** — Added Viral Event Marketing & Content Monetization in the Marketing domain based on user-provided video 67333.mp4. Documented the eight-participant boxing-event scenario, social distribution, potential YouTube monetization, and a responsible event-to-content workflow. Added explicit consent, participant welfare, physical safety, legal, platform-eligibility, and financial validation safeguards; updated the skill index and folder tree.

- **2026-11-17** — Added Behavioral Finance & Money Psychology, inspired by *The Psychology of Money* by Morgan Housel. Audited existing Finance and Psychology skills to avoid duplicating cash-flow, leverage, investment evaluation, emotional regulation, and general human-behavior guidance. Added a 20-chapter theme map, behavioral decision workflow, uncertainty and risk safeguards, and specialist routing. The skill is an operational synthesis, not a full-text transcription.
- **2026-11-17** — Added Viral Content Engineering & Attention Psychology in the Marketing domain based on user-provided video 67334.mp4. Documented attention design, viral content structure, emotional triggers, controversy/rage-bait analysis, hook engineering, engagement design, distribution experiments, attention-to-value conversion, and reputation safeguards. Recorded *The 48 Laws of Power*, Law 6, as the video's named reference and clarified that displayed view counts are illustrative rather than verified. Updated the skills index, folder tree, and Business Agent Orchestrator routing.

## Repository approach

- **2026-11-17** — Added Skill Boundary & Routing Governance with an ownership registry for all 71 skills, canonical routing recipes, handoff packet, conflict-resolution protocol, and maintenance policy. Updated all core orchestrators and high-overlap specialist skills to follow the same ownership and handoff contract. No specialist skills were deleted; overlapping capabilities were separated by responsibility.

This knowledge base grows incrementally as useful sources are reviewed. Each skill should contribute a reusable principle or method that helps the future AI mentor give grounded, context-aware, and actionable guidance.

The goal is not to collect the largest number of skills. The goal is to build reliable knowledge that improves the AI's decisions and the user's ability to act.

- **2026-11-17** — Added seven Finance skills inspired by the financial education themes in *Rich Dad Poor Dad*: Financial Intelligence, Asset & Liability Analysis, Cash Flow Management, Pay Yourself First, Financial Statement Literacy, Opportunity & Investment Evaluation, and Skill-Based Income Development. Clarified the difference between Kiyosaki's practical cash-flow shorthand and formal accounting definitions; added risk, liquidity, and affordability safeguards.

- **2026-11-17** — Added a Communication domain with six skills inspired by *Bicara Itu Ada Seninya* by Oh Su Hyang: Effective Communication & First Impressions, Active Listening & Conversational Rapport, Persuasive Communication & Negotiation, Message Design & Storytelling, Vocal & Nonverbal Delivery, and Public Speaking & Speaking Confidence. Added ethical boundaries and routing links to prevent overlap with existing Psychology and Marketing skills.

- **2026-11-17** — Added Emotional Regulation & Calm Decision-Making in the Psychology domain, inspired by the themes of *Rahasia Bersikap Tenang dalam Kondisi Apa Pun* by Sabrina Ara. Added practical guidance for emotional awareness, pausing, fact-versus-interpretation checks, controllability, realistic reframing, resilience, and calm decisions across work, relationships, business, and personal choices. Clarified source limitations and safeguards against emotional suppression or tolerating harm. Updated the Psychology Decision Engine, skill index, folder tree, and changelog.

- **2026-11-18** — Strengthened Context-Aware Response Strategy Engine and Service Recovery Marketing & Trust Building with responsibility-based response selection and seller-fault compensation assessment. Clarified that missing/wrong items must first be restored or refunded, while additional goodwill must be separately evaluated when seller-caused failures materially disrupt the customer experience. Added an example distinguishing the missing-item remedy from an approved complimentary core-product gesture.

## Future AI Company Naming Note

The following names are reserved as proposed identities for the future AI department agents. This is a planning note only; it does not mean the agents or organization structure have been implemented.

| AI name | Planned department |
|---|---|
| Mekki | Marketing |
| Tachy | Technology |
| Fini | Finance |
| Operi | Operations |
| Hura | Human Resources |
| Straty | Strategy & Growth |
| Puddi | Product |

The CEO name and the final organization structure are still to be decided. These names should be retained for the future AI Company architecture and revisited when the organization layer is designed.

- **2026-11-18** — Strengthened review-response psychology across Context-Aware Response Strategy Engine, Service Recovery Marketing & Trust Building, Consumer Psychology & Persuasion, and Message Design & Storytelling. Added state-matched openings (including appreciation before apology when appropriate), recognition, emotional validation, fairness/restoration, trust signaling, reciprocity boundaries, and concise public-reply composition. Clarified that gratitude never replaces accountability or remedy for a business-caused failure, and goodwill remains additional, approved, and non-conditional.
- **2026-11-18** — Operationalized the Doraemon–Nobita companion interaction model in Companion Interaction Style. Added moment/intent recognition, proactive but proportionate help, user agency, adaptation to corrections and approvals, simulation-aware context handling, and an internal response quality check. Updated the README changelog.
- **2026-11-18** — Strengthened Companion Interaction Style with execution-consistency rules: value before discovery, fewer serial intake questions, context-led initiative, a compact value-first response loop, and pass/fail quality gates. Added a TikTok affiliate example to demonstrate how the companion should provide a useful next step before asking for more information.
