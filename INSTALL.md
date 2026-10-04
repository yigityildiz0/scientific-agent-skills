# Installation

## Easiest method

1. Pick a skill in the catalog.
2. Download its ZIP for your platform.
3. Inspect the files, then extract the skill folder into one of these locations:

| Platform | Personal | Project |
|---|---|---|
| Claude Code | `~/.claude/skills` | `.claude/skills` |
| OpenAI Codex | `~/.agents/skills` | `.agents/skills` |
| OpenCode | `~/.config/opencode/skills` | `.opencode/skills` |

Each installed folder must contain `SKILL.md` directly: `<skills-root>/<skill-name>/SKILL.md`.

## Platform bundles

The release bundles contain the correct hidden directory tree. Extract the matching archive into your home folder for personal use, or into a project root for project-scoped use.

| Platform | Bundle |
|---|---|
| Claude Code | [⬇ Download](https://github.com/yigityildiz0/scientific-agent-skills/releases/latest/download/scientific-agent-skills-claude.zip) |
| OpenAI Codex | [⬇ Download](https://github.com/yigityildiz0/scientific-agent-skills/releases/latest/download/scientific-agent-skills-codex.zip) |
| OpenCode | [⬇ Download](https://github.com/yigityildiz0/scientific-agent-skills/releases/latest/download/scientific-agent-skills-opencode.zip) |

## Verify

- Folder name matches the `name` in YAML frontmatter.
- `SKILL.md` is uppercase and directly inside the skill folder.
- Restart the host if a newly installed skill does not appear.
- Large libraries can crowd discovery metadata. Install selectively or use the router bundle when this repository provides one.

Official references: [Claude Code skills](https://code.claude.com/docs/en/skills), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [OpenCode skills](https://opencode.ai/docs/skills).

## Literature review: cloud surfaces

Use the updated per-skill Claude ZIP in Claude.ai via Customize > Skills > Create skill > Upload a skill, with code execution and account permissions enabled. Its name remains scientific-literature-review and its description is under 200 characters. GPT/Codex local use takes the Codex ZIP; for ChatGPT web/mobile distribution, bundle it under a plugin's skills/scientific-literature-review with a root plugin.json following the official OpenAI guide. A local copy does not prove cloud installation or future monitoring. No schedule is created by this skill.

Official guides: [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [OpenAI plugins](https://developers.openai.com/plugins/build/plugins), [Claude custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
