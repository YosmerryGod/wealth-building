---
name: online-marketplace-pricing-and-promo-optimization
title: Online Marketplace Pricing & Promo Optimization
category: finance
subcategory: pricing-strategy
source_type: source-code-derived-method-and-generalized-operational-synthesis
source: AYDO – Kalkulator Merchant, YosmerryGod/Xkalkultor, src/utils/calculatePrice.js; src/utils/calculatePrice.test.js; src/utils/homeContent.test.js; src/constants/defaults.js
language: English
---

# Online Marketplace Pricing & Promo Optimization

## Purpose

Calculate the selling price required to preserve a merchant's target net receipt after marketplace fees and merchant-funded promotions. The source-derived calculation method in this skill is the AYDO implementation, not a replacement pricing formula invented for this repository.

The original source implementation is available at:
- https://github.com/YosmerryGod/Xkalkultor/blob/main/src/utils/calculatePrice.js
- https://github.com/YosmerryGod/Xkalkultor/blob/main/src/utils/calculatePrice.test.js
- https://github.com/YosmerryGod/Xkalkultor/blob/main/src/utils/homeContent.test.js
- https://github.com/YosmerryGod/Xkalkultor/blob/main/src/constants/defaults.js

## Ownership and routing boundary

Follow [Skill Boundary & Routing Governance](../../orchestrator/skill-boundary-governance/SKILL.md).

This skill owns reverse pricing for marketplace merchant net targets, marketplace fee recovery, promotion-burden calculations, promotion sequencing, and transparent price breakdowns based on the AYDO source algorithm.

It does not own full product HPP costing, general business viability, cash-flow forecasting, accounting profit interpretation, tax treatment, or marketplace policy verification. Obtain HPP/target net from the business or user; use Cash Flow Management for liquidity, Financial Intelligence for framing, and Business Operations for operational cost inputs when needed.

## 1. Source fidelity and evidence levels

Keep three layers distinct:

1. **AYDO source behavior:** the exact rules and formulas documented below, as implemented in the referenced source files.
2. **Configurable inputs:** marketplace fee percentages, fixed fees, promotion values, subsidies, caps, minimum purchases, merchant applicability, and enabled status. AYDO stores marketplace defaults in settings; these values are not universal or permanent platform facts.
3. **Generalized extensions:** additional costs, taxes, discounts, bundles, delivery, payment fees, or other platform rules not represented by the source algorithm. Do not silently insert them into the AYDO calculation. Model them separately and label the extension.

Do not claim to have executed the AYDO application or its tests unless that execution actually occurred. The repository's test file documents expected behavior and example results.

## 2. Required inputs

Collect or confirm the values needed for the requested calculation:

- Target net price per item (AYDO input `netPrice` / UI label `Harga Net`).
- Selected marketplace identifier and its configured fee percentage.
- Marketplace fixed fee, if any.
- Enabled promotions that apply to the selected marketplace.
- For each promotion: type (percentage or nominal), discount value, merchant subsidy percentage, minimum purchase, maximum discount, category/legacy fake flag, and whether it belongs to a promotion package.
- Promotion package contents and each item's own parameters.
- Whether a promotion is marketplace-funded, merchant-funded, or otherwise classified in the source configuration.

If a value is unknown, ask for it or mark it unknown. Do not assume a platform's current fee from old defaults.

## 3. AYDO algorithm — exact calculation sequence

### Stage A: marketplace administration fee

The source reads the selected marketplace setting:
- `fee`: percentage fee.
- `fixed`: fixed nominal fee.
- `name`: display name.

Let (N) be target net price, (f) be fee percentage expressed as a decimal, and (F) be fixed fee.

[
P_{admin} = \frac{N}{1-f} + F
]

The administration burden added to the current price is:

[
B_{admin} = P_{admin} - N
]

AYDO source defaults (configuration examples only):
- ShopeeFood: fee 20%, fixed Rp0.
- GrabFood: fee 25%, fixed Rp0.
- GoFood: fee 20%, fixed Rp1,000.

These defaults are application configuration, not verified current marketplace tariffs. A fee of 100% or above makes the reverse percentage calculation invalid or non-finite; flag invalid settings instead of presenting a usable result.

### Stage B: calculate one promotion's burden

For each promotion, read:
- (d): discount value.
- (s): merchant subsidy fraction (percentage divided by 100; defaults to 100% in source parsing).
- (M): maximum discount; zero means no cap in this implementation.
- (T): minimum purchase; zero means no minimum.

If the promotion is percentage-based, define (r = (d/100) 	imes s).

[
B_{percentage}(X) = \frac{Xr}{1-r}
]

If a maximum discount exists, the cap burden is:

[
C = M \times s
]

The source returns the smaller of the uncapped burden and cap burden. If (r) is at least 1, the uncapped branch is infinite and a finite cap can still constrain it; without a finite cap, the source returns zero because the final burden is non-finite.

For a nominal promotion:

[
D = \min(d,M) \quad \text{when } M>0
]
[
D = d \quad \text{when } M=0
]
[
B_{nominal}(X) = D \times s
]

The nominal burden does not use the percentage reverse-pricing formula.

### Stage C: minimum purchase adjustment

Let (X) be the current price before this promotion.

If (T > X), AYDO calculates the burden at the minimum-purchase amount, then divides it by the ratio (a=T/X):

[
a = \frac{T}{X}
]
[
B_{adjusted} = \frac{B(T)}{a}
]

If (T \le X), use the ordinary burden (B(X)).

This is the source's per-item adjustment behavior. Do not replace it with a different basket-allocation rule without clearly labeling that as an extension.

A missing promotion, non-positive current price, non-positive discount, or non-positive subsidy produces zero burden in the source method.

## 4. Promotion applicability, packages, and ordering

### Applicability

A promotion applies when:
- its merchant field is absent, or
- merchant is `all`, or
- merchant exactly matches the selected marketplace identifier.

Disabled promotions are excluded.

### Identify discount-crossed promotions

The source treats a promotion as a crossed-out/list-price promotion when `category === 'fake'` or its legacy `fake` flag is true. These promotions are separated and processed after normal promotions.

### Packages

For each enabled, applicable package:
- Split its sub-promotions into normal and crossed-out groups.
- Treat each non-empty group as its own stage.
- Within a stage, calculate every candidate's burden against the same current price.
- Select only the candidate with the greatest monetary burden in that stage.
- Add that one selected burden; do not sum all alternatives in the same package stage.

Separate package stages are processed sequentially. A package may therefore contribute one normal-stage item and one crossed-out-stage item when it contains both kinds.

### Normal promotion order

The source assigns stage rank:
1. Package stages: rank 0.
2. Standalone promotions whose category is `mandiri`: rank 2.
3. Other standalone normal promotions: rank 1.

Normal stages are sorted by this rank and then applied sequentially. Thus package stages precede standalone marketplace-category promotions, which precede standalone `mandiri` promotions. Within each stage, only the greatest calculated burden is added.

### Crossed-out promotion order

All crossed-out stages are applied after all normal stages, regardless of their original position in the settings list. They also use the greatest-burden candidate selection inside each stage.

Every stage uses the latest current price as the base for its burden calculation. Add the selected burden to that current price before moving to the next stage.

## 5. Final output and rounding

AYDO returns:
- `finalPricePerItem`: final current price rounded with JavaScript `Math.round`.
- `breakdown`: base net price, admin burden, and each selected promotion burden, with displayed values rounded individually.
- `merchantName`: selected marketplace display name.
- `hasCoret`: whether a crossed-out promotion was actually applied.
- `coretDiscountPercent`: selected crossed-out percentage value when applicable, otherwise null.

Important: the internal calculation carries unrounded numeric values through the sequence. Rounding is applied to the final price and each displayed breakdown value at the return stage. Do not round after every intermediate stage when reproducing AYDO.

## 6. Worked source-backed examples

These examples are from the assertions/comments in AYDO's `calculatePrice.test.js` and `homeContent.test.js`; they are not new platform tariff claims.

### Example A — admin fee only

Target net Rp10,000; fee 20%; fixed fee Rp0:

[
10,000/(1-0.20)=12,500
]

Expected final price: **Rp12,500**.

For GoFood's test configuration (20% + Rp1,000):

[
10,000/0.8 + 1,000 = 13,500
]

Expected final price: **Rp13,500**.

### Example B — percentage promotion

Target net Rp10,000; admin fee 20%; promotion 10%; subsidy 100%; no cap/minimum:

- After admin: Rp12,500.
- Promotion burden: (12,500 \times 0.10 / 0.90 = 1,388.89).
- Final: Rp13,888.89, rounded to **Rp13,889**.

### Example C — capped promotion

Same Rp10,000 net and 20% admin; promotion 10%, maximum discount Rp500, subsidy 100%:

- Uncapped burden would be Rp1,388.89.
- Maximum burden is Rp500.
- Final price: **Rp13,000**.

### Example D — subsidy 50%

Same Rp10,000 net and 20% admin; 10% promotion with 50% merchant subsidy:

- Effective rate: 10% × 50% = 5%.
- Burden: (12,500 \times 0.05 / 0.95 = 657.89).
- Final: **Rp13,158**.

### Example E — minimum purchase

Same Rp10,000 net and 20% admin; 10% percentage promotion; minimum purchase Rp25,000; subsidy 100%; no cap:

- Current price after admin: Rp12,500.
- Ratio (a=25,000/12,500=2).
- Burden at minimum: (25,000 \times 0.10/0.90=2,777.78).
- Per-item adjusted burden: (2,777.78/2=1,388.89).
- Final: **Rp13,889**.

### Example F — package chooses the greatest burden

At net Rp10,000 and admin 20%, a package containing 10% and 20% percentage promotions selects the 20% candidate only:

- Current price: Rp12,500.
- 20% burden: Rp3,125.
- Final: **Rp15,625**.

For a package with 10% promotion and nominal Rp2,500 promotion, the algorithm compares their calculated monetary burdens and selects the larger, rather than comparing the raw discount numbers.

### Example G — crossed-out promotion last

At net Rp10,000 and admin 20%, a normal standalone nominal merchant promo of Rp1,000 is applied before a crossed-out 10% promo:

- Rp12,500 + Rp1,000 = Rp13,500.
- Crossed-out 10% burden: Rp13,500 × 0.10 / 0.90 = Rp1,500.
- Final: **Rp15,000**.

## 7. Calculation workflow for an AI

1. Confirm the requested target: preserve a net receipt, compare marketplaces, evaluate a promotion, or inspect a current selling price.
2. Gather the target net price and exact settings for the selected marketplace.
3. Gather all enabled promotions and their applicability, subsidy, cap, minimum, package, and crossed-out metadata.
4. Reproduce the AYDO sequence exactly: admin fee → ranked normal stages → crossed-out stages.
5. For each promotion stage, calculate every candidate against the same current price and add only the greatest burden for that stage.
6. Keep full precision between stages; round only for final output and displayed breakdown.
7. Return final selling price, selected marketplace, assumptions, and a readable step-by-step breakdown.
8. If comparing marketplaces, run the same target net and promotion rules separately for each marketplace, applying only promotions that are applicable to each one.
9. Distinguish source-derived outputs from any added costs or rules that AYDO does not model.
10. If actual platform fees or promotion terms are uncertain, request the user's current merchant settings or verify the current official terms before treating them as facts.

## 8. Generalization beyond AYDO

The AYDO method can inform pricing workflows for other online marketplaces and direct online sales, but only where the fee and promotion mechanics match the model.

For a different platform:
- Map its actual fee components to percentage fee and fixed fee only if their calculation bases match.
- Identify whether each discount is funded by the merchant, platform, or shared; the AYDO `merchantSubsidy` input represents the merchant-funded share.
- Confirm whether minimum purchase is evaluated per item, per basket, or another basis.
- Confirm whether discount caps apply before or after subsidy.
- Confirm promotion stacking and precedence rules.
- Keep taxes, delivery, payment fees, service charges, packaging, affiliate commission, and other costs separate unless their bases and order are explicitly modeled.
- Do not force a platform's fee structure into AYDO's formula when the structure is materially different. Explain the mismatch and model the platform-specific rule separately.

The skill is reusable across businesses: food merchants, retail, digital goods, services, and other online sellers. The target net can represent a chosen net receipt or price floor; it is not automatically the same as accounting net profit. HPP and desired profit must be incorporated into the target net by a separate, transparent cost/profit calculation.

## 9. Output format

For a single calculation, show:
- Target net per item.
- Marketplace and fee settings used.
- Applied promotions in exact order.
- Final selling price.
- Breakdown of each added burden.
- Assumptions, unknowns, and configuration date/source.

For a comparison, show a table by marketplace with fee settings, applicable promotion burden, final price, and resulting net receipt check.

Do not claim that the result guarantees profitability. A correct reverse price only preserves the supplied target net under the supplied fee and promotion assumptions; it cannot validate whether the target net covers HPP, overhead, taxes, or desired business profit.

## Related skills

- [Financial Intelligence](financial-intelligence/SKILL.md) — financial framing and specialist routing.
- [Cash Flow Management](cash-flow-management/SKILL.md) — liquidity, timing, and operating cash.
- [Financial Statement Literacy](financial-statement-literacy/SKILL.md) — formal accounting interpretation.
- [Business Operations & Scaling](../business/business-operations-and-scaling/SKILL.md) — operational costs and capacity.
