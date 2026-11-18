# Repository Maintenance Notes

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

### Source audit: habit formation and competitive advantage

- **Wendy Wood, *Good Habits, Bad Habits: The Science of Making Positive Changes That Stick* (2019).** Publisher overview and publicly available excerpt reviewed. Source-supported themes used: habit formation is not reducible to willpower; context, repetition, and reward matter; environmental friction and cues influence repeated behavior. The new skill is an original coaching synthesis, not a full-text extraction or clinical protocol. [Publisher overview](https://us.macmillan.com/books/9781250159083/goodhabitsbadhabits/).
- **Peter Thiel with Blake Masters, *Zero to One: Notes on Startups, or How to Build the Future* (2014).** Publisher description and source text reviewed. Source-supported themes used: creating something meaningfully new, focused initial markets, distinctive market positions, and proprietary technology, network effects, economies of scale, and brand as potential sources of durability. The new skill is an original strategy synthesis; the 10x statement is treated as a heuristic, and monopoly language is bounded by lawful, customer-beneficial competition. [Publisher page](https://www.penguinrandomhouse.com/books/234730/zero-to-one-by-peter-thiel-with-blake-masters/).

The sources were not treated as proof that any habit method works for every person or that any business can or should achieve monopoly. No long copyrighted passages were copied.

### Source audit: pagination patterns

- **User-provided video 67567.mp4** (creator watermark visible as @kodebin; no public source URL supplied). Direct frame review identified three demonstrated patterns: Jump Input, Page Preview, and Sliding Pagination. The video recommends considering advanced pagination for very large page counts or visual content that benefits from a preview, while retaining simple pagination when page counts are small and function is the priority. The skill's accessibility, backend, performance, edge-case, and testing guidance is additional operational synthesis; the video does not supply implementation code or usability measurements.

### Source audit: expressive navigation patterns

- **User-provided video 67562.mp4** (creator watermark visible as @kodebin; no public source URL supplied). Direct frame review identified Radial Sidebar, Vertical Typography Navigation, and Scroll Progress Navigation. The video explicitly presents Radial Sidebar as suitable for creative portfolios and experimental landing pages; it shows vertical typographic section labels and a scroll-progress rail whose active marker follows scrolling and can be clicked to jump to a section. The video does not provide usability research, implementation code, or measured outcomes. Responsive, accessibility, selection, and implementation guidance in the expanded skill is operational synthesis.

### Source audit: Replica Skill application lifecycle

- **Jakeschincariol/replica-skill** (MIT-licensed repository; README and all eleven `replica-*/SKILL.md` files reviewed on 2026-11-18): source workflows cover reference reconnaissance, architecture planning, design-system reconstruction, screen-by-screen implementation, backend integrations, QA, feature/layout comparison, public user-review analysis, rebranding, launch preparation, and deployment.
- Wealth Building additions are original adaptations of workflow concepts and boundaries, not copied skill text, scripts, templates, or proprietary implementation. Existing owners were reused for recon/design/brand/customer discovery; new skills were added only for distinct architecture, implementation, backend, QA, parity, release, orchestration, and launch-planning responsibilities.
- Clean-room, privacy, authorized-access, no-fabrication, user-approval, and legal-review boundaries were retained and aligned with Wealth Building governance and Risk Assessment. Source repository tools are not installed or implied to be available here.

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
2. **Business Models & Unit Economics** — pricing, contribution margin, break-even analysis, customer acquisition cost, lifetime value, and cash conversion. Strategic differentiation and defensibility are now covered by Innovation & Competitive Advantage Strategy.
3. **Marketing, Sales & Distribution** — foundational coverage now includes Product Launch & Go-to-Market Planning alongside Traction Strategy, the Bullseye Framework, channel selection, growth experiments, referral growth, partnerships, and growth metrics. Further work can deepen positioning, offer design, sales processes, lifecycle marketing, and retention.
4. **Product & Offer Development** — product-market fit, differentiation, quality, packaging, and customer experience.
5. **Business Operations & Systems** — standard operating procedures, staffing, inventory, quality control, capacity, and process improvement. Core coverage added through Business Operations & Scaling.
6. **Financial Management** — foundational coverage now includes Financial Intelligence, Asset & Liability Analysis, Cash Flow Management, Pay Yourself First, and Financial Statement Literacy. Further work can deepen tax planning, debt management, and financial controls.
7. **Growth & Capital Allocation** — reinvestment priorities, return on invested capital, productive assets, expansion decisions, and responsible leverage.
8. **Risk, Resilience & Compliance** — downside planning, insurance, fraud prevention, legal requirements, taxes, and business continuity.
9. **Personal Finance & Wealth Preservation** — foundational coverage now includes income-to-asset planning, savings allocation, asset/liability analysis, and investment evaluation. Further work can deepen emergency-fund design, diversification, retirement planning, and wealth preservation.
10. **Communication & Interpersonal Effectiveness** — foundational coverage added through six Communication skills based on *Bicara Itu Ada Seninya*: effective communication, active listening, persuasion and negotiation, message design, vocal delivery, and public speaking.
11. **Execution & Progress Coaching** — goal setting, prioritization, accountability, progress reviews, and adapting plans to results. General non-financial habit design is now covered by General Habit Formation & Behavior Change; financial routines remain covered by Financial Habit Formation.
12. **Digital Product Design & Development** — expanded through Application Delivery Orchestrator, Application Architecture Planning, Full-Stack Application Engineering, Backend Engineering & Integrations, Software Testing & QA, Application Parity Evaluation, and Application Deployment & Release Engineering.
13. **Creative Production & Brand Identity** — image generation workflows, visual design, logo systems, brand identity, and consistent creative direction.

## Repository approach

This knowledge base grows incrementally as useful sources are reviewed. Each skill should contribute a reusable principle or method that helps the future AI mentor give grounded, context-aware, and actionable guidance.

The goal is not to collect the largest number of skills. The goal is to build reliable knowledge that improves the AI's decisions and the user's ability to act.

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

