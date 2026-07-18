# Kurulum

## En kolay yöntem

1. Katalogdan bir skill seç.
2. Platformuna ait ZIP’i indir.
3. Dosyaları gözden geçir ve skill klasörünü şu yollardan birine aç:

| Platform | Kişisel | Proje |
|---|---|---|
| Claude Code | `~/.claude/skills` | `.claude/skills` |
| OpenAI Codex | `~/.agents/skills` | `.agents/skills` |
| OpenCode | `~/.config/opencode/skills` | `.opencode/skills` |

Kurulan her klasörde `SKILL.md` doğrudan bulunmalı: `<skills-root>/<skill-name>/SKILL.md`.

## Platform paketleri

Release paketleri doğru gizli klasör ağacını içerir. Kişisel kullanım için kullanıcı ana klasörüne, proje kullanımı için proje köküne aç.

| Platform | Paket |
|---|---|
| Claude Code | [⬇ İndir](https://github.com/yigityildiz0/scientific-agent-skills/releases/latest/download/scientific-agent-skills-claude.zip) |
| OpenAI Codex | [⬇ İndir](https://github.com/yigityildiz0/scientific-agent-skills/releases/latest/download/scientific-agent-skills-codex.zip) |
| OpenCode | [⬇ İndir](https://github.com/yigityildiz0/scientific-agent-skills/releases/latest/download/scientific-agent-skills-opencode.zip) |

## Doğrula

- Klasör adı YAML frontmatter içindeki `name` ile aynı olmalı.
- `SKILL.md` büyük harfle yazılmalı ve skill klasörünün doğrudan içinde olmalı.
- Yeni skill görünmüyorsa host’u yeniden başlat.
- Çok büyük kütüphaneler keşif metadata bütçesini doldurabilir. Seçerek yükle veya varsa router paketini kullan.

Resmî kaynaklar: [Claude Code skills](https://code.claude.com/docs/en/skills), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [OpenCode skills](https://opencode.ai/docs/skills).
