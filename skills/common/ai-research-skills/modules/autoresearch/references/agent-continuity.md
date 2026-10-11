# Agent Continuity: Keeping Research Running

Autonomous research requires agents that keep working continuously — hours, overnight, or days. This reference covers how to set up the wall-clock loop on each platform.

## Optional: Explicitly Authorized Continuity

Start research in the current session. Configure a wall-clock loop only when the user explicitly requests recurring work; agree its duration, cadence, compute budget and cancellation method. Twenty minutes is an example interval, not a default instruction.

This is completely separate from the research inner/outer loops. The authorized wall-clock loop is a scheduled task prompt that retains the same permission and budget boundaries. The research loops run at experiment speed (minutes to hours per cycle). They will not sync and don't need to.

## Claude Code: /loop

**Example only after authorization and verification of current platform support:**

```
/loop 20m Continue autoresearch. Read research-state.yaml and findings.md. Check: is the current experiment done? Are there errors? Is progress stalling? If everything is on track, keep working. If something is wrong, step back and fix it. Continue within the agreed scope and budget; stop on completion or cancellation.
```

### What Happens on Each Tick

The `/loop` message fires every 20 minutes. When it fires:

1. **Read state** — `research-state.yaml` and `findings.md` to remember where you are and what you've learned
2. **Check health** — is the current experiment running? Did it error? Is training diverging?
3. **If on track** → continue whatever you were doing (don't restart or re-plan)
4. **If stuck or broken** → step back, diagnose the issue, fix it, then continue
5. **If idle** → choose a next hypothesis only within the remaining authorized budget; otherwise report completion or the blocking condition.

The tick is a nudge, not a phase boundary. If the previous tick's work isn't done, just keep going.

### When Experiments Run Longer Than 20 Minutes

This is normal and expected. On the next tick:
- Check if the experiment finished
- If still running: monitor for errors, do lightweight work (update notes, search papers)
- Don't restart or duplicate the experiment

### Context Recovery

Your primary memory between ticks is `research-state.yaml` and `findings.md`. Keep them updated after every experiment and reflection. If you lose context, read both files plus `research-log.md` to reconstruct where you are.

## OpenClaw: Cron Job

**Optional, explicitly authorized recurring-work example:** Use the `cron.add` tool to create a recurring job bound to the current chat session:

```json
{
  "name": "autoresearch-loop",
  "schedule": { "kind": "every", "everyMs": 1200000 },
  "sessionTarget": "current",
  "payload": {
    "kind": "agentTurn",
    "message": "Continue autoresearch. Read research-state.yaml and findings.md. Check: is the current experiment done? Are there errors? Is progress stalling? If everything is on track, keep working. If something is wrong, step back and fix it. Continue within the agreed scope and budget; stop on completion or cancellation."
  }
}
```

Key details:
- `sessionTarget: "current"` binds the cron to the current chat session (resolved to `session:<sessionKey>` at creation time), so it maintains conversation context across ticks
- `everyMs: 1200000` = 20 minutes
- Verify with `cron.list` that the job is created and enabled
- To check run history later: `cron.runs` with the job ID

### Context Between Cron Ticks

OpenClaw cron invocations may start fresh each time. Your workspace files are your memory:

- `research-state.yaml` — where you are, what's active
- `findings.md` — what you've learned (read this every time!)
- `research-log.md` — what happened chronologically

Keep these updated after every action so the next cron tick can pick up seamlessly.

### Progress Reports

OpenClaw can't `open` HTML files locally like Claude Code can. When you have something to report:

1. Generate a PDF progress summary (use Python with reportlab, matplotlib, or similar)
2. Include: research question, key results, optimization trajectory plot, current understanding, next steps
3. Share the local report in the current chat. External messaging requires explicit authorization for the recipient, service and report contents
4. Give meaningful progress updates in the current chat; do not infer external-send permission from an interesting result

## Research State as Ground Truth

Both platforms share the same ground truth: the workspace files.

| File | Purpose | Update Frequency |
|---|---|---|
| `research-state.yaml` | Machine-readable state | After every experiment and reflection |
| `research-log.md` | Decision timeline | After every significant action |
| `findings.md` | Narrative understanding + project memory | After every outer loop |
| `experiments/*/results/` | Raw experimental data | After every experiment |

The wall-clock loop (`/loop` or cron) is just the trigger. The workspace files are the memory. Keep them current.
