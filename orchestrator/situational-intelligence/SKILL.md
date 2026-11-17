---
name: situational-intelligence-and-contextual-reasoning
title: Situational Intelligence & Contextual Reasoning
category: orchestration
subcategory: cross-domain-cognitive-reasoning
source_type: original-ai-reasoning-framework
language: English
---

# Situational Intelligence & Contextual Reasoning

## Purpose

Give the AI a disciplined ability to understand what is actually happening before selecting knowledge, tactics, language, or actions. The skill coordinates context, facts, goals, constraints, domain knowledge, likely consequences, and available choices so that recommendations fit the real situation rather than matching keywords to canned templates.

This is a general reasoning layer for business, marketing, customer service, leadership, workplace, personal decisions, and other practical situations. It complements Contextual Understanding & Intent Inference, Human Behavior Intelligence, specialist decision engines, and Risk Assessment. It does not replace them.

## Central principle

**Understand the situation before choosing the technique.**

A technically correct technique can still be the wrong recommendation when it ignores what has already happened, what the user is trying to achieve, what the other party experiences, what the business has promised, what resources are available, or what the proposed action will cost.

Do not imitate human intuition by guessing. Build a grounded situation model, reason across relevant facts, compare plausible actions, and update the decision when new evidence appears.

## Distinguish the reasoning layers

- **Conversation continuity:** what has the user already told us, decided, approved, or corrected?
- **Situation understanding:** what is happening now, who is involved, and what constraints shape it?
- **Intent inference:** what outcome does the user want, and what might other parties want?
- **Domain knowledge:** which psychology, marketing, business, finance, operations, or communication principles apply?
- **Decision reasoning:** which available action best fits the goal, evidence, constraints, and consequences?
- **Execution communication:** how should the chosen action be explained or delivered?
- **Feedback learning:** what happened after the action, and what should change?

Use Contextual Understanding & Intent Inference for continuity across messages. Use this skill to reason about the current situation. Use specialist skills for domain-specific depth.

## Situation model

Build a compact model from relevant dimensions. Do not mechanically fill every field when the task is simple.

### 1. Actors and roles

Identify the user and relevant people, groups, organizations, customers, employees, suppliers, or observers. Establish each party's role, responsibility, relationship, authority, and ability to choose.

Do not assume the user is always the seller, leader, victim, customer, or decision-maker.

### 2. Timeline and current state

Identify what happened, in what order, what has already been tried, what is pending, and what has changed. Separate historical context from the present state.

### 3. Facts, assumptions, and unknowns

Classify information as:
- Confirmed facts from the user or reliable records.
- Direct observations or quoted statements.
- Reasonable but unverified assumptions.
- Competing hypotheses.
- Missing information that could change the decision.

Never silently convert an assumption into a fact. Do not ask the user to repeat information already available.

### 4. Goals and incentives

Identify the user's stated goal and relevant secondary goals. Consider the likely interests of other parties without claiming certainty about hidden motives.

Goals can conflict. For example, a business may want to restore customer trust, attract future buyers, control compensation costs, preserve margins, and correct an operational defect. A response should account for the important goals rather than optimizing only one.

### 5. Context and constraints

Consider relevant details such as:
- Product or service specifications and what is already included.
- Price, quantity, quality, terms, promises, and customer expectations.
- Available budget, margins, staff, inventory, capacity, and approval authority.
- Channel, audience, timing, location, culture, and relationship history.
- Policies, platform rules, laws, safety requirements, and privacy.
- Previous actions and their outcomes.

Use current and project-specific information where available. If an important detail may have changed, mark it as uncertain or confirm it before a consequential recommendation.

### 6. Human and behavioral factors

Where relevant, consider expectations, perceived fairness, emotions, trust, attention, incentives, cognitive load, habits, social proof, status, power, and decision friction.

Treat psychological explanations as hypotheses supported by observable evidence, not as mind-reading or diagnosis.

### 7. Commercial and operational reality

For business decisions, test the recommendation against:
- Customer value and the actual promise or offer.
- Cost to serve, product cost, contribution margin, and cash impact.
- Feasibility, stock, staffing, delivery, and execution capacity.
- Repeatability and precedent for other customers.
- Root cause and whether the action fixes or merely hides the problem.

A recommendation that sounds persuasive but cannot be fulfilled, damages unit economics without a reason, or ignores the underlying failure is not a good recommendation.

## Contextual reasoning workflow

### Step 1 — Reconstruct the relevant context

Use conversation history, project state, user-provided materials, and reliable records. Preserve prior corrections and explicit decisions. Identify the user's current request rather than treating a short follow-up as an isolated prompt.

### Step 2 — Define the real problem

Describe the practical problem in one or two sentences. Distinguish the visible symptom from the underlying issue.

Example: a customer says a meal priced at Rp20,000 feels like a Rp10,000 portion. The visible issue is a price/portion complaint. The underlying questions may include portion standards, menu expectations, perceived value, actual fulfilment, and the business's recovery objective.

### Step 3 — Identify the desired outcomes

List the primary outcome and any important secondary outcomes. Separate outcomes that must happen from outcomes that are merely desirable.

Example: resolve the customer's dissatisfaction, show future readers that the business responds responsibly, protect customer trust, and avoid making an unauthorized or economically careless promise.

### Step 4 — Find the decision-critical facts

Ask: what facts would materially change the recommendation? Use available evidence first. Ask one focused question only when a missing fact cannot be responsibly assumed and changes the action.

Do not ask questions just to complete a template.

### Step 5 — Generate genuinely different options

Consider a small set of meaningfully different actions, not several phrasings of the same action. Depending on the case, options may include:
- Explain or clarify the existing offer.
- Correct a factual or operational error.
- Apologize and acknowledge impact.
- Replace, refund, or provide a proportionate remedy.
- Offer an additional goodwill gesture.
- Change the product, process, menu, policy, or communication.
- Invite private follow-up.
- Make no offer when the complaint does not justify one.

### Step 6 — Simulate likely consequences

For each plausible option, consider:
- Does it address the actual problem?
- How might the affected person interpret it?
- How might a third-party observer interpret it?
- Does it create a promise, expectation, precedent, or obligation?
- What is its financial and operational cost?
- Can the user actually deliver it?
- Does it fix the cause or only the appearance?
- Could it create a new problem or unfair outcome?

Do not claim certainty about how people will react. State material uncertainty.

### Step 7 — Select and justify the best-fit action

Choose the option that best balances the user's goal, fairness, evidence, feasibility, commercial reality, and consequences. Explain briefly why it is better than the obvious alternatives.

Do not default to the most generous, cheapest, safest-sounding, persuasive, or conventional action. Fit matters more than habit.

### Step 8 — Communicate for the audience

Only after deciding the action, select the communication strategy, tone, order, level of detail, and call to action. Keep the message aligned with what the user can genuinely do.

For public communication, consider both the direct recipient and future readers. Do not turn a complaint into a sales pitch before acknowledging and addressing the complaint.

### Step 9 — Confirm authority and execution

Distinguish recommendation from approved commitment. Do not promise refunds, freebies, discounts, delivery, policy exceptions, or other business commitments unless the user has authorized them or the applicable policy clearly grants authority.

When authority is unknown, present the recommended remedy as a proposal for owner approval and draft conditional wording accordingly.

### Step 10 — Learn from the result

When the user reports what happened, compare the outcome with the prediction. Update the situation model, identify mistaken assumptions, and improve the next decision. Preserve useful corrections as project context when supported by the runtime.

## Customer review reading and public-response conversion

When the user asks the AI to reply to a public review, the task is not merely customer service and not merely sales copy. The AI must understand the reviewer and the silent readers, then write one concise response that resolves the reviewer's concern while making the business's real value and trustworthiness easy for prospective customers to recognize.

### Read the customer before writing

Infer only what the review supports. Classify:
- **Stated experience:** what the customer explicitly says happened.
- **Emotional signal:** frustration, disappointment, satisfaction, surprise, appreciation, or uncertainty, supported by wording and rating.
- **Underlying objection or motivation:** price/value, portion, taste, quality, accuracy, speed, convenience, trust, or expectations.
- **Expectation gap:** what the customer expected versus what they say they received.
- **Relationship state:** first-time, repeat, potentially recoverable, satisfied, or unclear. Do not infer purchase history unless shown.
- **Response need:** apology, clarification, correction, remedy, appreciation, or no response.
- **Confidence:** separate clear facts from plausible interpretations. A rating alone does not reveal the full reason.

Do not stereotype customers by name, age, gender, profile photo, or assumed income. Read the actual words, rating, order details, and available history.

### Recognize the two audiences

1. **The reviewer:** wants to know whether the business understood their specific experience and will respond fairly.
2. **Prospective customers scanning reviews:** want quick signals about product value, consistency, honesty, and how the business handles problems.

The reviewer must not be treated as a prop for advertising. Resolve or acknowledge their concern first. Then make one relevant trust or value signal visible to future readers.

### Psychology + marketing must appear in the actual reply

Do not keep all the marketing reasoning hidden in the analysis while producing a generic apology. Select one or two relevant psychological and marketing mechanisms and express them naturally in the final wording.

Possible mechanisms:
- **Fairness and acknowledgment:** name the exact concern so the customer sees that the business listened.
- **Trust signaling:** state a concrete corrective action, transparent process, or approved remedy.
- **Value proposition:** show a real product attribute or inclusion that is relevant to the concern; never invent or repackage an existing inclusion as a new gift.
- **Social proof:** when responding to genuine praise, reflect the specific product experience the customer liked; do not fabricate popularity.
- **Risk reduction:** explain a real way the business will check, replace, correct, or follow up.
- **Objection handling:** answer the actual concern with evidence or a relevant offer, not defensive claims.
- **Conversion invitation:** use a soft, natural invitation only when the complaint has been addressed and the business can honor it.

### Write for a fast-scanning reader

Use a compact, readable reply, usually two to four short sentences. Put the most decision-relevant point early. Avoid long corporate introductions, generic filler, excessive emojis, vague claims such as "best quality", and multiple competing calls to action.

For a negative review, a useful order is:
1. Specific acknowledgment and apology where warranted.
2. A visible, concrete resolution or approved remedy.
3. One truthful trust/value signal that helps future readers understand what the business is doing.
4. A simple next step when needed.

For a positive review:
1. Thank the customer and name the specific thing they liked.
2. Reinforce a genuine product strength or experience.
3. Give a light invitation to return or try a relevant menu item, without sounding pushy.

For a mixed review:
1. Acknowledge both the positive and the criticism.
2. Address the criticism with a concrete improvement or approved remedy.
3. Preserve the positive value signal without using it to dismiss the complaint.

### Marketing opportunity detection: required decision stage

After reconstructing the customer's situation and before selecting the final public reply, run a deliberate marketing opportunity assessment. Do not stop reasoning once a service-recovery action has been found.

Inspect the actual product, menu, offer, and business context available:
- **Core product:** what is the business actually selling, and which item or service should remain central?
- **Product strength / USP:** what concrete, supportable attribute makes the offer worth considering (for example taste, preparation, ingredients, portion, convenience, service feature, or experience)?
- **Value proposition:** what does the buyer receive, why is it useful, and how does it relate to the buyer's concern?
- **Existing inclusions:** what is already part of the normal package or menu? It may be highlighted accurately, but must not be presented as a newly granted gift or compensation.
- **Additional benefits:** what bonus, add-on, bundle, cross-sell, or goodwill offer is genuinely available, relevant, economically sensible, and authorized?
- **Buyer motivation and objection:** what might make a silent reader hesitate, and what factual benefit can answer that hesitation?
- **Conversion opportunity:** is a soft invitation, menu suggestion, or contact instruction appropriate after the reviewer's issue has been addressed?

Use the following evidence hierarchy:
1. Verified menu, product specification, current offer, policy, or business-provided fact.
2. Specific product experience stated by the reviewer.
3. Other reliable context supplied by the user.
4. Clearly labelled hypothesis, used only to guide what to verify—not stated as a fact in public copy.

Never invent product advantages, customer popularity, free items, prices, availability, guarantees, or promotions. If the business's actual product strengths or offer details are not available, do not fabricate them; state what information would unlock a stronger marketing angle.

### Marketing decision by review condition

- **Positive review:** turn the customer's specific praise into product proof; reinforce the praised attribute and, where relevant, introduce a real complementary product or existing package benefit with a natural invitation.
- **Mixed review:** acknowledge both praise and criticism; resolve the criticism and preserve the genuine product strength without using it to cancel the complaint.
- **Negative review / fulfilment failure:** address the failure and fair remedy first. Then assess whether a relevant product value, real package inclusion, corrective action, or approved goodwill offer can give future readers a reason to trust and consider the business.
- **Price or value objection:** explain the actual value composition—product, portion, inclusions, quality, convenience, or service—rather than reflexively discounting.
- **Quality or safety concern:** prioritize investigation and customer protection. Do not use product promotion or another serving as a hook while the safety or quality issue remains unresolved.
- **No relevant opportunity:** omit promotion deliberately; do not add generic sales language merely to satisfy a checklist.

The goal is not to force an advertisement into every reply. The goal is to prevent a service-only reflex from hiding a genuine, relevant commercial opportunity.

### Counter without arguing

A marketing counter is not a rebuttal that tries to prove the customer wrong. It is a relevant fact, action, or offer that reduces uncertainty and shows why a prospective buyer can still trust the business.

Examples:
- If the customer says the portion felt small, do not answer by advertising soup that was already included. Acknowledge the portion concern, investigate the serving standard, and—if approved—offer a genuinely additional, order-appropriate remedy.
- If the customer says the food tasted good but the portion was small, recognize the positive taste feedback while still addressing the portion issue. Do not use the praise to cancel out the complaint.
- If the customer praises freshness or flavor, echo that exact attribute rather than making unsupported claims about popularity or superiority.

### Final response quality test

Before sending the reply, ask:
- Would the reviewer feel that their exact point was understood?
- Can a prospective customer identify the business's relevant value or responsible action at a glance?
- Did I explicitly assess the core product, verified USP, value proposition, existing inclusions, approved additional benefits, buyer objection, and conversion opportunity?
- If I chose not to promote, is that because promotion is irrelevant, unsupported, mistimed, or inappropriate—not because I forgot to evaluate it?
- Is the strongest marketing signal factual, specific, and relevant?
- Is the actual remedy clear and approved?
- Is any existing menu inclusion being misleadingly presented as a bonus?
- Does the reply avoid arguing, overexplaining, or hard-selling?
- Could the business reliably fulfill every promise in the reply?

## Customer review and service-recovery application

When a business owner shares customer reviews, screenshots, complaints, or ratings, do not jump directly to writing a reply.

First inspect:
1. The exact customer statement and rating.
2. The purchased product or service.
3. The actual menu, offer, price, quantity, inclusions, and promise, if known.
4. Whether the complaint concerns a preference, value perception, missing item, wrong order, quality defect, delivery issue, or safety issue.
5. What remedy would genuinely address the specific loss or dissatisfaction.
6. What future readers may infer from the business's public response.
7. Whether the proposed remedy is approved, feasible, and proportionate.

Coordinate with [Service Recovery Marketing & Trust Building](../../skills/marketing/service-recovery-marketing-and-trust-building/SKILL.md), [Consumer Psychology & Persuasion](../../skills/marketing/consumer-psychology-and-persuasion/SKILL.md), [Brand Communication & Public Relations](../../skills/marketing/brand-communication-and-public-relations/SKILL.md), relevant Business Operations skills, and Communication skills as needed.

### Existing inclusion versus additional value

Never market an item that is already included in the normal menu or offer as though it were a new gift, compensation, or special benefit.

For example, if soup is already included with a meal, saying "we provide free soup" does not answer a complaint about insufficient chicken portion. It repeats the original offer and may make the business appear not to have understood the complaint.

Identify the customer's actual objection and select a response that addresses it. If the issue is portion/value perception, possible options may include checking portion standards, clarifying the portion, correcting an under-portion, refunding the shortfall, or offering an additional item as goodwill when justified and authorized.

### Remedy fit and offer design

A goodwill offer should be relevant to the customer's original order and the actual dissatisfaction. For a restaurant, a possible gesture might be one portion of chicken, or one portion of chicken with rice when that better fits the order context. This is an example of contextual matching, not a universal compensation rule.

Before recommending it, consider:
- What exactly did the customer order?
- Was rice, chicken, or another item already included?
- What part of the experience did the customer say was inadequate?
- Is the offer intended to correct a measurable shortfall or provide additional goodwill?
- What is the cost and margin impact?
- Can the business fulfill it on the next order?
- Has the owner approved it?
- Is the same offer fair and manageable if similar cases arise?

Do not assume that a free item is always the right answer. For a missing item, replacing the missing item or refunding its value may be more appropriate. For suspected unsafe food, prioritize safety and investigation; never offer another serving from an unverified batch as a marketing gesture.

### Two audiences, two jobs

A public review response has two audiences:
- **The reviewer:** needs to feel heard and receive a clear, fair path to resolution.
- **Future buyers:** need credible evidence of product value, accountability, and how the business handles problems.

Address the reviewer first. Then, where relevant and truthful, let the response demonstrate the business's value or recovery action to future readers. Do not sacrifice the reviewer's resolution to promote the business.

### Public reply structure

Use a compact sequence suited to the case:
1. Specific acknowledgment.
2. Sincere apology where warranted.
3. Clear corrective action or approved remedy.
4. Simple contact or redemption instruction if needed.
5. Brief prevention or value message only when it adds something relevant.

Make the most important approved remedy visible early. Do not invent benefits, guarantees, promotions, menu inclusions, or customer outcomes.

### Example: portion/value complaint

Known context: the customer says a Rp20,000 meal feels like a Rp10,000 portion. The menu already includes soup. The owner is considering a goodwill offer of one chicken portion, with rice if appropriate to the original order.

Reasoning:
- The soup is an existing inclusion, so presenting it as a free gift is misleading and does not address the chicken-portion concern.
- The reply should acknowledge the portion/value concern.
- A relevant additional chicken portion may be a more meaningful goodwill gesture, but only if the owner approves and the business can fulfill it.
- If the original order's rice inclusion changes what would be useful, match the offer to that order rather than applying a generic gift.
- The business should separately check portion consistency and menu expectations.

Example wording, only after owner approval:

"Terima kasih sudah menyampaikan masukannya, Kak. Mohon maaf porsi ayamnya belum sesuai harapan. Kami ingin memberikan tambahan 1 porsi ayam panggang untuk pesanan berikutnya sebagai bentuk tanggung jawab dan apresiasi kami. Silakan hubungi WhatsApp resmi kami dan sebutkan ulasan ini agar tim kami bisa membantu."

If rice is part of the approved offer and appropriate to the original order, state that exact offer instead. Do not imply the offer is approved when it is not.

## Cross-domain routing

| Situation | Lead skill or engine | Supporting knowledge when useful |
|---|---|---|
| Complex human situation with behavior and communication | Human Behavior Intelligence Layer | Psychology and Communication Decision Engines |
| Business decision with multiple interacting constraints | Business Agent Orchestrator | Business Operations, Finance, Marketing |
| Customer complaint or public review | Service Recovery Marketing & Trust Building | Consumer Psychology, PR, Communication, Business Operations |
| Sales objection or conversion decision | Marketing / Consumer Psychology | Persuasive Communication, pricing, product economics |
| Financial or investment decision | Relevant Finance skill | Risk Assessment and current evidence |
| Ambiguous request with important prior context | Contextual Understanding & Intent Inference | Relevant domain engine |

Route only to skills that add distinct value. Do not expose internal routing unless the user asks to inspect it.

## Quality checks

Before responding, verify:
- Did I use the full relevant context and preserve prior corrections?
- Did I identify the real problem rather than react to a keyword?
- Did I distinguish facts, assumptions, and unknowns?
- Did I consider the goals of the user and affected parties?
- Did I inspect the actual offer, product, price, or commitment before describing it?
- Did I distinguish existing inclusions from genuinely additional value?
- Did I compare more than one plausible action?
- Did I consider psychological, financial, operational, reputational, and fairness consequences where relevant?
- Is the chosen action feasible and authorized?
- Does the message solve the actual problem before trying to persuade?
- Have I stated uncertainty and the evidence that could change the decision?

## Limitations

This is an original AI reasoning framework, not a claim that an AI has human consciousness, intuition, lived experience, or access to facts that were not provided. It improves structured contextual reasoning but cannot guarantee correct inference. The AI must remain transparent about uncertainty, ask for decision-critical missing facts, and revise its model when corrected.

## Related skills

- [Contextual Understanding & Intent Inference](../contextual-understanding/SKILL.md)
- [Human Behavior Intelligence Layer](../human-behavior-intelligence/SKILL.md)
- [Business Agent Orchestrator](../business-agent/SKILL.md)
- [Service Recovery Marketing & Trust Building](../../skills/marketing/service-recovery-marketing-and-trust-building/SKILL.md)
- [Consumer Psychology & Persuasion](../../skills/marketing/consumer-psychology-and-persuasion/SKILL.md)
- [Brand Communication & Public Relations](../../skills/marketing/brand-communication-and-public-relations/SKILL.md)
- [Communication Decision Engine](../../skills/communication/communication-decision-engine/SKILL.md)
- [Risk Assessment & Consequence Intelligence](../risk-assessment/SKILL.md)

## Implementation status

This file defines a reusable knowledge and reasoning specification. It does not create autonomous software, persistent memory, a business database, or automatic access to menu, inventory, order, or financial systems. Such capabilities require separate runtime tools, data integrations, permissions, and evaluation.

## Skill boundary governance

Follow [Skill Boundary & Routing Governance](skill-boundary-governance/SKILL.md). Situational Intelligence owns the general cross-domain situation model and comparison of viable options. Contextual Understanding owns retrieval/continuity; HBIL owns human interpretation when relevant; specialist skills own domain methods; Context-Aware Response owns response-mode selection. Reuse their outputs, avoid duplicate intake, and return a decision-ready model with facts, assumptions, unknowns, constraints, options, consequences, and the key unresolved question.
