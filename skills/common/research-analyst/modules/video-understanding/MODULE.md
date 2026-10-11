# Module: video-understanding

Use for “videoyu izle/anla/özetle”, timestamped event analysis, lecture or exercise-video review. This adds a workflow, not a video model or plugin.

## Choose an available route

1. Identify the actual video or URL, goal, language and relevant interval. Resolve whether the user needs spoken content, visual actions, on-screen text or all three. Ask only if this changes the analysis.
2. If the current host natively accepts video, use its documented file/length limits and report the interval actually inspected. A URL, thumbnail or title alone is not access to the video.
3. Otherwise use a local file plus existing FFmpeg/ffprobe for metadata, timestamped frames and audio; use an already installed local speech recognizer such as Whisper for transcription. No separately billed transcription/video/vision API fallback. Do not install a plugin for this workflow.
4. Without a visual-capable model/tool, a transcript supports speech analysis only. State that visual actions were not inspected and ask for relevant screenshots or a locally supported vision route.

## Evidence workflow

- Record duration, streams, source identity, inspected intervals and sampling strategy. Use regular sampling plus denser sampling around cuts, rapid motion, procedure transitions and the user’s event. Do not infer an absent event from unsampled intervals.
- Keep a manifest of frame file, requested timestamp, actual timestamp when available, observation and uncertainty. Account for variable frame rate, seeking, orientation and time offsets; frame number divided by nominal FPS is not a universal timestamp.
- Separate `VISUAL`, `TRANSCRIPT`, `ON_SCREEN_TEXT`, `INFERENCE` and `EXTERNAL_CHECK`. Cite video timestamps for observed events and URLs for independently verified factual claims.
- Align transcript segments with frames. Recheck names, numbers, units, negations and Turkish/English/Latin medical terms against audio/context. Never silently repair uncertain dosage or left/right labels.
- For exercise/gait/clinical videos, distinguish visible movement from inferred pain, diagnosis or intent. Use physio-clinical-copilot for clinical interpretation; report camera-angle, occlusion and missing-patient-context limits.
- Synthetic/editing detection is probabilistic. Compression artifacts alone do not establish manipulation; use source-verification for provenance and reverse-search checks.
- Final answer: requested result, timestamped evidence, inspected coverage, remaining uncertainty. Say “sampled frames + transcript” when that is what happened, not “watched the whole video”.

## Local tooling reference

The bundled [sample_video.py](scripts/sample_video.py) uses existing FFmpeg/ffprobe to extract local PNG frames and a manifest containing requested positions, decoded PTS when available, source hash and coverage. Run `python <module-root>/scripts/sample_video.py <local-video> --out <new-directory> --samples 8`, then inspect the frames with the current host’s actual image capability. It never transcribes, downloads a model, calls an API or claims complete video understanding. Use more targeted samples when the event needs them.

Inspect the installed version and available tools before adapting commands. Metadata-only example:

```text
ffprobe -v error -show_format -show_streams -of json INPUT_VIDEO
```

For extraction, choose a new output directory; use the actual FFmpeg version’s frame-selection/timestamp options. Reading a file is not permission to upload it, and a local recognizer’s model download/storage is a separate environment requirement. The existing host’s permissions remain unchanged.

Official references (checked 2026-10-11):
- [FFmpeg / ffprobe documentation](https://ffmpeg.org/documentation.html)
- [FFmpeg frame output and synchronization](https://ffmpeg.org/ffmpeg-all.html)
- [OpenAI Whisper: local speech recognition, not visual understanding](https://github.com/openai/whisper)

A plugin is useful for an integrated frame/timeline/transcript UI and local processing; a skill alone cannot add that runtime. DSH Vision Toolkit provides image inspection, not established end-to-end video decoding. Its configured provider may charge separately; prefer the current host’s native vision or an already available local model under this profile. No plugin install is required or implied.
