---
name: 2d-mesh-avatar-rigging
description: Turn a single character illustration into an editable animated 2D mesh avatar with layered artwork, rigging, expressions, lip sync, and motion review.
---

# 2D Mesh Avatar Rigging

## Purpose

Help a coding agent prepare an illustration as an animated 2D avatar, then hand the project to a local editor for refinement and export.

## Input requirements

- Prefer a front-facing, head-and-shoulders illustration with clear facial features.
- Transparent PNG backgrounds simplify segmentation.
- Three-quarter views, occluded faces, overlapping hair, hands across the face, and complex accessories increase reconstruction difficulty.
- Preserve the source image locally unless the user explicitly approves sending it to an external image service.

## Workflow

1. Inspect image dimensions, transparency, pose, facial visibility, and likely segmentation challenges.
2. Create a project structure that preserves the source image and generated working files.
3. Map facial and body landmarks; calibrate coordinate-reading accuracy before detailed rigging.
4. Define editable parts and control points for face, eyes, mouth, hair, buns, accessories, and optional body regions.
5. Separate the illustration into layers while preserving overlaps and occlusion.
6. Build a mesh rig with suitable deformation regions and motion parameters.
7. Preview fixed poses: head turns, tilts, blinking, idle breathing, hair sway, and mouth movement.
8. Correct distortions and rebuild layers when source outlines or masks change.
9. Add drawn variants such as closed eyes, vowel mouths, and expressions when they materially improve animation.
10. Export a portable avatar package and document the source-image and asset terms.

## Quality review

- Facial features remain aligned during head movement.
- Hair and accessories do not detach or deform unnaturally.
- Blinks close cleanly and reopen without jitter.
- Lip-sync shapes remain readable.
- Idle motion is subtle and does not distract.
- The avatar works in the intended player, streaming, or application environment.

## Technical considerations

- Check required Node.js, Python, image-processing, and browser-rendering dependencies against the current project documentation.
- Run the project's diagnostic commands before generation.
- Use visual calibration and fixed-pose reviews rather than trusting coordinate estimates blindly.
- Keep generated layers, masks, rig data, and source images organized and reproducible.
- Camera and microphone processing should be transparent to the user; document what stays local and what is transmitted.

## Source and attribution

Original knowledge synthesis based on [shinshin86/mesh-avatar-studio](https://github.com/shinshin86/mesh-avatar-studio), licensed MIT. Its sample character Miko is explicitly excluded from the repository's MIT license and has separate usage terms. Do not reuse or redistribute that character as a generic MIT asset.
