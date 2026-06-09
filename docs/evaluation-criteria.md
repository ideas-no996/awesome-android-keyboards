# Evaluation Criteria

This project evaluates Android keyboards along practical dimensions, not only popularity.

## Maintenance status

- `active`: Recent releases, commits, or visible development.
- `maintenance-only`: Usable, but development appears limited to fixes.
- `inactive`: No meaningful recent maintenance signal.
- `archived`: Repository is archived or project is explicitly discontinued.
- `unknown`: Source is not enough to classify confidently.

## Chinese support

- `none`: No meaningful Chinese input support.
- `basic`: Can type Chinese only through limited layouts, system dictionaries, or external support.
- `good`: Practical Chinese typing for common users.
- `excellent`: Strong Chinese prediction, phrase handling, cloud or local dictionaries, and mainstream usage.
- `rime-based`: Uses Rime or Rime-compatible schemas as a central input engine.

## Theme system

- `none`: No meaningful visual customization.
- `basic`: Light/dark or simple color options.
- `good`: Multiple themes, adjustable layout, colors, or key styles.
- `advanced`: Extensible theme packs, detailed layout control, or theme formats suitable for reuse.

## Privacy level

- `high`: Open source or well-scoped, works offline, and does not require network access for core typing.
- `medium`: Proprietary or cloud-assisted, but core typing can reasonably work without always-on network features.
- `low`: Typing depends heavily on network services or privacy posture is hard to evaluate.

Privacy level is not a legal claim. It is a curation signal based on available sources and observable architecture.

## Development feasibility

- `high`: Buildable open-source project with approachable architecture and active maintenance.
- `medium`: Open source but large, old, native-heavy, or hard to modify safely.
- `low`: Proprietary, closed-source, abandoned, or unsuitable as a fork base.

## Architecture complexity

- `low`: Small codebase or narrow feature set.
- `medium`: Typical Android IME complexity.
- `high`: Multi-engine, native code, cloud features, AI features, plugin systems, or deep schema support.

## Theme adaptation suitability

`suitable_for_ios_like_theme` and `suitable_for_glassmorphism` indicate whether the project appears practical for visual adaptation. A "true" value does not mean the project already ships that exact style.

Criteria include:

- Existing theme hooks.
- Layout flexibility.
- Rendering architecture.
- Buildability.
- License compatibility.
- Maintenance state.
