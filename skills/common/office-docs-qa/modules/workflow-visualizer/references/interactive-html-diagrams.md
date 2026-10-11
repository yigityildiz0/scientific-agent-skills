# Interactive HTML Diagram Rules

Keep an accessible static reading order and a printable main path. Interaction may reveal detail, highlight a route, filter an already-visible model, or synchronize a details panel; it must not hide essential nodes or force pointer use.

## Structure

- Use stable internal IDs, short visible labels, and a separate details model.
- Use flow for sequential/branching work, swimlanes for ownership, hub-and-spoke for shared services, and a focused state/sequence diagram for loops or time.
- Split large diagrams into overview and focused subdiagrams before adding zoom/pan complexity.

## Interaction and accessibility

- Use buttons and focusable controls with names and visible state.
- Support keyboard activation, Escape/reset where applicable, focus restoration, reduced motion, and no-hover alternatives.
- Pair color with labels, shape, line style, or patterns. Maintain contrast in both normal and selected states.
- Use `textContent`, safe attributes, and a restrictive CSP; do not concatenate untrusted values into HTML, SVG, CSS, selectors, or handlers.

## Validation

Check syntax, connectivity, narrow screen behavior, zoom, keyboard sequence, screen-reader reading order, print view, and the artifact after opening from disk with no network access.
