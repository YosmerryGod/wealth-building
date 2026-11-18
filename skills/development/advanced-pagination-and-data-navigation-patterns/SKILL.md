---
name: advanced-pagination-and-data-navigation-patterns
title: Advanced Pagination & Data Navigation Patterns
category: development
source_type: user-provided-video-and-operational-framework
source: User-provided video file 67567.mp4; creator watermark visible as @kodebin; no public source URL supplied
language: Indonesian
description: "Use when a request needs pagination pattern selection, page jumping, page previews, or sliding page navigation."
triggers:
  - "pagination"
  - "paginasi"
  - "navigasi halaman"
  - "jump input"
  - "page preview"
  - "sliding pagination"
out_of_scope: "Overall site navigation architecture, visual identity, data-query architecture, or general frontend implementation ownership"
escalation: "Hand off overall navigation architecture to Modern Web Navigation & Interaction Patterns, visual direction to Frontend Design, detailed interaction feedback to Micro-Interactions & UI Feedback Design, and implementation to the project's frontend engineering owner; invoke Risk Assessment for material legal, safety, exploitation, or high-consequence actions."
---

# Advanced Pagination & Data Navigation Patterns

## Purpose

Choose and design pagination controls that help users move through multi-page collections without adding unnecessary complexity. The skill owns navigation between pages of the same result set or content collection, not movement between major product sections.

Pagination is not automatically better when it looks more advanced. Select the simplest pattern that fits the number of pages, content type, user task, device, and need for orientation.

## Source evidence and limits

The user-provided video (file 67567.mp4, creator watermark visible as @kodebin) demonstrates three patterns:

1. **Jump Input:** a compact page-number input that lets a user enter a target page and jump directly to it. The video shows this in a paginated order list and a smaller input example.
2. **Page Preview:** a page selector accompanied by visual content previews. The video shows preview cards for a visual guide/article collection, giving users a glimpse of page content before opening it.
3. **Sliding Pagination:** a horizontally shifting sequence of page numbers, with the visible range moving as the user navigates. The video illustrates this for a long page sequence and mentions timeline/gallery-style content as a suitable context.

The video also contrasts when to use a new pattern: consider it when there are hundreds of pages or when content is visual and benefits from a preview; keep the existing/simple pagination when there are few pages and function matters more than visual treatment.

The video does not provide implementation code, usability research, performance measurements, or controlled evidence that one pattern is universally superior. The selection framework, accessibility guidance, edge cases, and testing workflow below are additional operational synthesis, not claims made by the video.

## Pattern ownership

### 1. Jump Input

Allow users to enter a page number directly, usually alongside previous/next controls and a visible current-page/total-pages label.

**Good fit**
- Large result sets where users know or receive a page number.
- Admin tables, order histories, logs, reports, and records with stable page ordering.
- Tasks where direct page access is more useful than scanning many numbered links.

**Design and behavior**
- Show the current page and total page count clearly.
- Validate input as an integer within the valid range.
- Define whether navigation occurs on Enter, an adjacent Go button, or both; do not navigate on every keystroke.
- Clamp or reject out-of-range values consistently and explain the valid range.
- Preserve the current filter, sort, and search query when changing pages.
- Keep previous/next controls available when they are useful; disable them at the boundaries.
- On small screens, avoid shrinking the input until its purpose or value becomes unreadable.

**Avoid when**
- The collection has only a few pages.
- Users have no reason to know a target page number.
- Page ordering changes frequently enough that a remembered page number is misleading.

### 2. Page Preview

Show a small, meaningful preview of page content as part of choosing a destination. A preview may be a thumbnail, image, title, or concise content excerpt, depending on the content type.

**Good fit**
- Visual galleries, image collections, editorial pages, maps, catalogs, or other content where a visual clue helps users recognize a destination.
- Collections where page identity is more meaningful than its number alone.

**Design and behavior**
- Preview actual destination content; do not use decorative or misleading placeholder imagery.
- Keep previews lightweight and avoid loading every page's full content at once.
- Provide a clear page label and a keyboard/touch-accessible way to select it.
- Use a fallback when thumbnails or preview data are unavailable.
- Ensure the preview adds enough orientation to justify its visual and network cost.

**Avoid when**
- Pages contain mostly tabular or repetitive records.
- Thumbnails are unavailable, expensive, or do not help distinguish pages.
- The preview makes the pagination area larger or slower without improving selection.

### 3. Sliding Pagination

Display a limited window of page numbers that shifts as the current page changes. It may include first/last shortcuts, ellipses, and previous/next controls when they help users understand the range.

**Good fit**
- Long collections with many pages.
- Timelines, galleries, catalogs, and result sets where nearby page context matters.
- Interfaces where showing every page number would overwhelm the layout.

**Design and behavior**
- Keep the current page visibly distinct.
- Use a predictable window around the current page and define how it behaves near the beginning and end.
- Use ellipses only when they represent omitted page ranges; make them actionable only if the behavior is clear.
- Preserve stable focus when the page window shifts.
- Do not rely on swipe or drag alone; provide visible controls and keyboard operation.
- Consider first/last controls only when users benefit from those destinations.

**Avoid when**
- There are very few pages and a simple numbered list is clearer.
- The changing window causes users to lose their place or makes keyboard focus unpredictable.
- The collection is better navigated by search, filtering, or continuous scrolling.

## Selection workflow

1. **Understand the collection:** determine total/approximate page count, whether the count is stable, ordering, page size, and whether users can search or filter.
2. **Understand the content:** distinguish records/tables from visual or editorial content; establish whether page identity can be previewed.
3. **Understand the task:** decide whether users browse nearby pages, jump to a known page, recognize content visually, or need only previous/next movement.
4. **Choose the simplest sufficient pattern:**
   - Few pages: simple numbered pagination or previous/next.
   - Many pages and known target: Jump Input.
   - Visual content where recognition matters: Page Preview.
   - Many pages where nearby page context matters: Sliding Pagination.
   - Very large or rapidly changing collections: assess search, filters, cursor-based navigation, or virtualized/continuous browsing before assuming numbered pagination is appropriate.
5. **Check device and input:** design for touch, mouse, keyboard, narrow viewports, and assistive technology.
6. **Validate the data behavior:** confirm page boundaries, total count, sort/filter persistence, loading behavior, and empty/error states.
7. **Test with realistic content:** verify that users can find a target page and understand where they are without unnecessary steps.

## Functional and accessibility requirements

- Use semantic links when a page destination has a stable URL and browser history should support it; use buttons for stateful actions without a navigable URL.
- Expose the current page programmatically (for example, with `aria-current="page"`) as well as visually.
- Give inputs and controls explicit accessible labels; do not rely on placeholder text as the only label.
- Support keyboard navigation and visible focus. Keep focus behavior stable after page changes.
- Announce loading or result updates appropriately without creating noisy screen-reader output.
- Ensure controls have usable touch targets and sufficient contrast.
- Do not use color, animation, or position alone to communicate the selected page.
- Respect reduced-motion preferences if the page window animates.
- Preserve filters, sorting, and search state unless the user explicitly resets them.

## Data, performance, and edge cases

- Avoid fetching every page merely to render page controls or previews.
- Use server-side pagination for large datasets when appropriate; align UI page size and page parameters with the backend contract.
- For cursor-based APIs, do not fabricate numbered pages or a total count when the backend does not provide them.
- Define behavior for zero results, one page, unknown total, deleted records, changed filters, stale page links, and out-of-range page values.
- Prevent duplicate requests and stale responses when users navigate quickly.
- Prefer stable ordering with a deterministic tie-breaker so records do not unexpectedly appear on multiple pages or disappear between requests.
- Treat loading, empty, error, and boundary states as part of the component, not afterthoughts.

## Practical review checklist

- [ ] The pattern matches page count, content type, and user intent.
- [ ] A simpler pattern was considered and rejected for a clear reason.
- [ ] Current page and total/unknown count are communicated accurately.
- [ ] First/last boundaries and invalid page values behave predictably.
- [ ] Search, filters, and sorting persist correctly.
- [ ] Keyboard, touch, screen-reader, focus, and reduced-motion behavior are usable.
- [ ] Preview assets are real, relevant, and loaded efficiently.
- [ ] Backend pagination semantics match the UI.
- [ ] Mobile layout remains understandable and operable.
- [ ] Loading, empty, error, and stale-data cases are tested.

## AI implementation rules

- Inspect the existing application, data source, routing, and pagination contract before editing.
- Do not add Jump Input, Page Preview, or Sliding Pagination merely because the video shows them.
- Follow the video's own selection principle: advanced patterns are most relevant for very large page counts or visual content that benefits from a preview; simple pagination remains preferable when the collection is small.
- Explain trade-offs only when they affect the user's choice.
- Preserve existing filters, sorting, route conventions, and unrelated UI.
- Do not claim a preview, page count, or navigation behavior exists unless the project data supports it.
- If asked to implement, change only the requested pagination scope and test the affected states.

## Relationship to other Development skills

- **Modern Web Navigation & Interaction Patterns:** owns movement between product sections and navigation destinations; this skill owns movement between pages inside one collection.
- **Frontend Design:** owns overall product-specific visual direction; this skill defines pagination-specific selection and behavior.
- **Micro-Interactions & UI Feedback Design:** owns detailed interaction feedback and motion; this skill specifies pagination states that need feedback.
- **AI Interface Design & Unslop Engineering:** may audit whether the pagination choice is product-specific and not decorative complexity.
- **Reverse Engineering & Reference-Based Reconstruction:** owns evidence gathering from a supplied reference; this skill translates observed pagination patterns into reusable selection and implementation guidance.

## Ownership and routing boundary

Follow [Skill Boundary & Routing Governance](../../orchestrator/skill-boundary-governance/SKILL.md). Advanced Pagination & Data Navigation Patterns owns pagination pattern selection and page-to-page navigation behavior within a collection. It does not own global navigation, overall visual design, backend query architecture, or general frontend engineering. Use the smallest relevant combination of specialists and return one coherent recommendation.

## Classification

- Primary skill: Advanced Pagination & Data Navigation Patterns
- Domain: Development / UI/UX
- Source-derived patterns: Jump Input, Page Preview, Sliding Pagination
- Primary use cases: Long result lists, order histories, reports, visual collections, galleries, timelines, and catalogs
- Source status: User-provided video 67567.mp4 reviewed directly; operational selection, accessibility, data, performance, and testing guidance is added synthesis
