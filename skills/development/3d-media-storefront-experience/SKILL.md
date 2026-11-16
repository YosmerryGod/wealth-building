---
name: 3d-media-storefront-experience
description: Design browser-based 3D storefronts and walkable catalog experiences for media libraries, games, and other browsable digital collections.
---

# 3D Media Storefront Experience

## Purpose

Translate a conventional digital catalog into a spatial retail experience where users browse aisles, inspect items, discover categories, and move toward a clear viewing or purchase action.

## Experience model

- **Store identity:** storefront architecture, era, colors, signage, lighting, and environmental details.
- **Departments:** organize the collection into recognizable aisles and genre zones.
- **Shelf browsing:** show clear item covers, titles, metadata, and category context.
- **Item inspection:** provide a closer view and useful details without losing the user's place.
- **Checkout or action point:** connect the browsing experience to the real next step, such as opening a streaming service, launching a game, or accessing a product.
- **Ambient life:** optional characters, traffic, and environmental animation can make the store feel active, but should not obstruct navigation.

## Workflow

1. Identify the catalog source, audience, collection size, and primary user action.
2. Design the store layout around the information architecture, not visual spectacle alone.
3. Define item metadata, search, filtering, sorting, and category navigation.
4. Choose interaction controls appropriate for keyboard, gamepad, TV remote, touch, and mouse.
5. Connect to the authorized media or catalog source and handle unavailable items gracefully.
6. Optimize asset loading, level of detail, draw calls, texture sizes, and low-power rendering.
7. Provide a conventional list/grid mode for users who prefer speed or accessibility.
8. Test navigation, item selection, search, performance, and external-service failures.

## Product and integration considerations

- A 3D store is a presentation layer, not a media-hosting or licensing solution.
- Respect the APIs, authentication requirements, and terms of connected services.
- Clearly distinguish catalog metadata from playable content and subscription entitlements.
- Do not imply that the storefront owns or supplies content that is actually provided by another service.
- Consider privacy and security when exposing a self-hosted media library to visitors.

## Source and attribution

Inspired by the user experience and integration concepts in [halcyon-video/halcyon-video](https://github.com/halcyon-video/halcyon-video), licensed GPL-3.0. This is an original descriptive skill, not a copy of Halcyon's code. Any distribution of modified or combined GPL-covered software must follow GPL-3.0 obligations. Media artwork and third-party catalog assets may have separate rights.
