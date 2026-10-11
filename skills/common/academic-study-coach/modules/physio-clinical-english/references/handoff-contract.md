# Inter-skill handoff fallback

A `$physio-*` reference is a request to the host agent; it is not proof that the target skill loaded.

1. Prefer the explicitly invoked specialist. The implicit hub performs only the safety/routing wrapper and must not duplicate the specialist output.
2. Before relying on a handoff, verify that the target skill is actually available in the host context when the host exposes that information.
3. If available, pass a minimal de-identified brief: user goal, safety/escalation status, population/setting/jurisdiction, known facts, material unknowns, requested output, and sources already verified.
4. If unavailable, do not impersonate its full method or claim that it ran. Complete only the current skill's bounded workflow, state the missing capability, give a safe minimum structure or reproducible next step, and ask the user to install/use the complete plugin when that capability matters.
5. Never let a failed handoff weaken emergency escalation, privacy, uncertainty, or scope boundaries.

The complete `physio-evidence-suite` plugin is the supported configuration for automatic hub routing. A specialist may be used alone for its own workflow. A standalone hub is incomplete by design and is not a release artifact.
