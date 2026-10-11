# Inter-skill handoff fallback

A `$physio-*` reference is a request to the host agent; it is not proof that the target skill loaded.

1. Prefer the explicitly invoked specialist. The implicit hub performs only the safety/routing wrapper and must not duplicate the specialist output.
2. Before relying on a handoff, verify that the target skill is actually available in the host context when the host exposes that information.
3. If available, pass a minimal de-identified brief: user goal, safety/escalation status, population/setting/jurisdiction, known facts, material unknowns, requested output, and sources already verified.
4. If unavailable, do not impersonate its full method or claim that it ran. Complete only the current skill's bounded workflow, state the missing capability, give a safe minimum structure or reproducible next step, and identify the missing capability only when it materially limits the requested result.
5. Never let a failed handoff weaken emergency escalation, privacy, uncertainty, or scope boundaries.

The embedded modules support this consolidated skill's own workflows. Optional companion skills or plugins can extend them, but their absence does not block a supported bounded task. When a companion is unavailable, use the current embedded method and disclose only the material limitation; never claim the absent skill ran.
