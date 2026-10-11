#!/usr/bin/env python3
"""Local timestamped video frames. No API, download, model, plugin or transcription."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess

def run(args):
    result = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    if result.returncode:
        raise RuntimeError(result.stderr[-2000:])
    return result

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path)
    ap.add_argument("--out", required=True, type=Path, help="new output directory")
    ap.add_argument("--samples", type=int, default=8)
    ap.add_argument("--ffmpeg", default="ffmpeg")
    ap.add_argument("--ffprobe", default="ffprobe")
    a = ap.parse_args()
    source = a.input.resolve(strict=True)
    if not source.is_file() or a.samples < 1:
        ap.error("input must be a local file; samples must be positive")
    for command in (a.ffmpeg, a.ffprobe):
        if not shutil.which(command):
            ap.error("missing local tool: " + command)
    metadata = json.loads(run([a.ffprobe,"-v","error","-protocol_whitelist","file,pipe","-show_format","-show_streams","-of","json",str(source)]).stdout)
    videos = [s for s in metadata.get("streams",[]) if s.get("codec_type")=="video" and not s.get("disposition",{}).get("attached_pic")]
    if not videos:
        ap.error("no video stream")
    video = videos[0]
    duration = float(video.get("duration") or metadata.get("format",{}).get("duration") or 0)
    if not math.isfinite(duration) or duration <= 0:
        ap.error("finite positive duration unavailable; inspect metadata manually")
    a.out.mkdir(parents=True, exist_ok=False)
    digest = hashlib.sha256()
    with source.open("rb") as f:
        for block in iter(lambda: f.read(1024*1024), b""):
            digest.update(block)
    manifest = {"source":str(source),"sha256":digest.hexdigest(),"metadata":metadata,"duration_seconds":duration,"sampling":"uniform requested positions; not complete visual coverage","transcription":False,"visual_model_run":False,"frames":[],"complete":False}
    dest = a.out / "manifest.json"
    def save(): dest.write_text(json.dumps(manifest,ensure_ascii=False,indent=2,allow_nan=False),"utf-8")
    save()
    for i in range(a.samples):
        requested = duration * i / a.samples
        frame = a.out / f"frame-{i:04d}.png"
        result = run([a.ffmpeg,"-nostdin","-n","-v","info","-protocol_whitelist","file,pipe","-ss",str(requested),"-copyts","-i",str(source),"-map","0:" + str(video["index"]),"-frames:v","1","-vf","showinfo","-an","-sn","-dn","-update","1",str(frame)])
        if not frame.exists() or frame.stat().st_size == 0:
            raise RuntimeError("no frame at requested position: " + str(requested))
        match = re.search(r"\bn:\s*0\s+pts:.*?pts_time:([+-]?[0-9.eE]+)",result.stderr)
        pts = float(match.group(1)) if match else None
        manifest["frames"].append({"file":frame.name,"requested_elapsed_seconds":requested,"decoded_pts_seconds":pts,"timestamp_note":"PTS is source stream time, not automatically elapsed time; check start_time/timebase before alignment"})
        save()
    manifest["complete"] = True
    save()
    print(json.dumps({"manifest":str(dest.resolve()),"frames":len(manifest["frames"]),"visual_coverage":"sampled only","model_run":False}))

if __name__ == "__main__":
    main()
