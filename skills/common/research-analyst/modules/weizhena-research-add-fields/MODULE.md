# Module: weizhena-research-add-fields

> Weizhena/Deep-Research-skills (MIT) Claude/generic variant, unchanged. Paths relative to this module folder.
> Original trigger scope: Add field definitions to existing research outline. Use with an existing /research outline. Turkish triggers: araştırmaya alan ekle, yeni kriter ekle.

# Research Add Fields - Supplement Research Fields

## Trigger
`/research-add-fields`

## Workflow

### Step 1: Auto-locate Fields File
Find `*/fields.yaml` file in current working directory, auto-read existing fields definitions.

### Step 2: Get Supplement Source
Ask user to choose:
- **A. User direct input**: User provides field names and descriptions
- **B. Web Search**: Launch agent to search common fields in this domain

### Step 3: Display and Confirm
- Display suggested new fields list
- User confirms which fields to add
- User specifies field category and detail_level

### Step 4: Save Update
Append confirmed fields to fields.yaml, save file.

## Output
Updated `{topic}/fields.yaml` file (in-place modification, requires user confirmation)

## Host notes (added for the user's setup)

- If this host has no background web-search agent or subagents (for example ChatGPT/Claude web or mobile), run the same prompt template yourself for each item — sequentially, or with the host's parallel tools — and write the same outputs.
- The validator is `validate_json.py` inside the `research` skill folder. If the path shown above does not exist on this host, locate that file next to the `research` skill and run it from there (requires `pip install pyyaml`).
- Group related clarification questions into one message. Use defaults only when the user explicitly approves them, and state the chosen date range and batch size.
