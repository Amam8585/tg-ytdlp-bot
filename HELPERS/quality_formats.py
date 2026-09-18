"""Pure helpers for deriving selectable qualities from yt-dlp metadata."""

from __future__ import annotations

import re

from HELPERS.qualifier import get_quality_by_min_side


def format_quality(fmt: dict) -> str | None:
    """Return a normalized ``NNNp`` class for a video format."""
    if fmt.get("vcodec") == "none":
        return None
    width, height = fmt.get("width"), fmt.get("height")
    if width and height:
        quality = get_quality_by_min_side(int(width), int(height))
        if quality != "best":
            return quality
    text = " ".join(str(fmt.get(k) or "") for k in ("resolution", "format_note", "format_id"))
    if re.search(r"(?i)(?:^|\W)4k(?:\W|$)", text) or re.search(r"3840\s*[x×]\s*2160", text):
        return "2160p"
    match = re.search(r"(?<!\d)(144|240|360|480|540|576|720|1080|1440|2160|4320)p?(?!\d)", text, re.I)
    return f"{int(match.group(1))}p" if match else None


def available_video_qualities(info: dict) -> list[str]:
    """Return sorted, de-duplicated qualities actually advertised by yt-dlp."""
    qualities = {q for fmt in info.get("formats", []) if (q := format_quality(fmt))}
    return sorted(qualities, key=lambda q: int(q[:-1]))


def quality_format_selector(quality: str, codec: str | None = None) -> str:
    """Build a merge-capable yt-dlp selector for an actual quality button."""
    height = int(quality.lower().replace("4k", "2160").rstrip("p"))
    codec_filter = f"[vcodec*={codec}]" if codec else ""
    return f"bv*{codec_filter}[height<={height}][height>{max(0, _previous(height))}]+ba/bv*{codec_filter}[height<={height}]+ba/b[height<={height}]/best"


def _previous(height: int) -> int:
    return max((h for h in (0, 144, 240, 360, 480, 540, 576, 720, 1080, 1440, 2160) if h < height), default=0)
