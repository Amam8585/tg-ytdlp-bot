import importlib
import string
import sys
import types
from pathlib import Path

import pytest


@pytest.fixture
def caption_module(monkeypatch):
    config_module = types.ModuleType("CONFIG.config")
    config_module.Config = type("Config", (), {"BOT_NAME": "caption_bot"})
    monkeypatch.setitem(sys.modules, "CONFIG.config", config_module)
    sys.modules.pop("HELPERS.caption", None)
    module = importlib.import_module("HELPERS.caption")

    class Messages:
        CAPTION_VIDEO_URL_LINK_MSG = (
            '<a href="{url}">🔗 Video URL</a>{quality_codec}{bot_mention}'
        )

    monkeypatch.setattr(module, "safe_get_messages", lambda _user_id: Messages())
    return module


def _truncate(module, quality_codec=""):
    return module.truncate_caption(
        title="A normal title",
        description="A normal description",
        url="https://example.com/video",
        tags_text="#video",
        user_id=42,
        quality_codec=quality_codec,
    )


def test_video_caption_without_optional_quality_codec(caption_module):
    parts = _truncate(caption_module)
    assert parts[4] == (
        '<a href="https://example.com/video">🔗 Video URL</a> @caption_bot'
    )
    assert parts[:4] == (
        "<b>A normal title</b>", "", "A normal description", "#video\n"
    )


def test_video_caption_preserves_real_quality_codec(caption_module):
    parts = _truncate(caption_module, " · 1080p / H.264")
    assert "Video URL</a> · 1080p / H.264 @caption_bot" in parts[4]


def test_kvs_caption_without_format_metadata_can_reach_upload(caption_module):
    """Model the KVS handoff: caption creation must finish before upload is called."""
    uploaded = []
    link_block = _truncate(caption_module, quality_codec=None)[4]
    uploaded.append(link_block)
    assert uploaded == [
        '<a href="https://example.com/video">🔗 Video URL</a> @caption_bot'
    ]


def test_actual_video_codec_metadata_is_read_from_ffprobe(monkeypatch):
    config_module = types.ModuleType("CONFIG.config")
    config_module.Config = type("Config", (), {})
    monkeypatch.setitem(sys.modules, "CONFIG.config", config_module)
    format_module = types.ModuleType("COMMANDS.format_cmd")
    format_module.get_user_mkv_preference = lambda _user_id: False
    monkeypatch.setitem(sys.modules, "COMMANDS.format_cmd", format_module)
    sys.modules.pop("DOWN_AND_UP.ffmpeg", None)
    ffmpeg = importlib.import_module("DOWN_AND_UP.ffmpeg")
    result = types.SimpleNamespace(returncode=0, stdout="h264\n")
    monkeypatch.setattr(ffmpeg.subprocess, "run", lambda *args, **kwargs: result)

    assert ffmpeg.get_video_codec_ffprobe("downloaded-kvs-video.mp4") == "h264"


def test_all_video_link_translations_have_compatible_placeholders():
    language_dir = Path(__file__).parents[1] / "CONFIG" / "LANGUAGES"
    expected = {"url", "quality_codec", "bot_mention"}
    files = sorted(language_dir.glob("messages_*.py"))
    assert files

    for path in files:
        source = path.read_text(encoding="utf-8")
        marker = "CAPTION_VIDEO_URL_LINK_MSG = "
        assignment = next(line for line in source.splitlines() if marker in line)
        template = eval(assignment.split(marker, 1)[1], {"__builtins__": {}})
        fields = {name for _, name, _, _ in string.Formatter().parse(template) if name}
        assert fields == expected, path.name
        assert template.format(
            url="https://example.com", quality_codec="", bot_mention=" @bot"
        )
