# Module: weizhena-research-add-items

> Weizhena/Deep-Research-skills (MIT) Claude/generic variant, unchanged. Paths relative to this module folder.
> Original trigger scope: Add items (research objects) to existing research outline. Use with an existing /research outline. Turkish triggers: araştırmaya madde ekle, listeye yeni öğe ekle.

# Research Add Items - Supplement Research Objects

## Trigger
`/research-add-items`

## Workflow

### Step 1: Auto-locate Outline
Find `*/outline.yaml` file in current working directory, auto-read.

### Step 2: Get Supplement Sources in Parallel
Simultaneously:
- **A. Ask user**: What items to supplement? Any specific names?
- **B. Ask if Web Search needed**: Launch agent to search for more items?

### Step 3: Merge and Update
- Append new items to outline.yaml
- Display to user for confirmation
- Avoid duplicates
- Save updated outline

## Output
Updated `{topic}/outline.yaml` file (in-place modification)

## Host notes (added for the user's setup)

- If this host has no background web-search agent or subagents (for example ChatGPT/Claude web or mobile), run the same prompt template yourself for each item — sequentially, or with the host's parallel tools — and write the same outputs.
- The validator is `validate_json.py` inside the `research` skill folder. If the path shown above does not exist on this host, locate that file next to the `research` skill and run it from there (requires `pip install pyyaml`).
- Group related clarification questions into one message. Use defaults only when the user explicitly approves them, and state the chosen date range and batch size.
