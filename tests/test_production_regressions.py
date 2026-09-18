import asyncio
from pathlib import Path

from HELPERS.download_jobs import create_download_job
from HELPERS.quality_formats import available_video_qualities, format_quality, quality_format_selector


def _video(height, codec="avc1", audio="none", **extra):
    return {
        "format_id": extra.pop("format_id", f"v{height}-{codec}"),
        "width": int(height * 16 / 9),
        "height": height,
        "vcodec": codec,
        "acodec": audio,
        **extra,
    }


def test_quality_metadata_maxima_and_no_fake_4k():
    assert available_video_qualities({"formats": [_video(360), _video(1080)]}) == ["360p", "1080p"]
    assert available_video_qualities({"formats": [_video(1080), _video(1440)]})[-1] == "1440p"
    assert "2160p" not in available_video_qualities({"formats": [_video(1080)]})
    assert available_video_qualities({"formats": [_video(1080), _video(2160)]})[-1] == "2160p"


def test_4k_aliases_video_only_duplicates_and_merge_selector():
    aliases = [
        {"vcodec": "vp9", "format_note": "4K"},
        {"vcodec": "av01", "resolution": "3840x2160"},
        {"vcodec": "hevc", "format_id": "2160p"},
    ]
    assert {format_quality(item) for item in aliases} == {"2160p"}
    info = {"formats": [_video(2160, "vp9"), _video(2160, "av01"), {"format_id": "a", "vcodec": "none", "acodec": "opus"}]}
    assert available_video_qualities(info) == ["2160p"]
    selector = quality_format_selector("4K", "vp9")
    assert "[height<=2160]" in selector
    assert "+ba" in selector


def test_same_user_jobs_are_isolated_and_cleanup_cannot_cross_delete(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    async def run():
        first, second = await asyncio.gather(
            asyncio.to_thread(create_download_job, 42),
            asyncio.to_thread(create_download_job, 42),
        )
        assert first.path != second.path
        media1, media2 = first.path / "same.mp4", second.path / "same.mp4"
        media1.write_bytes(b"one")
        media2.write_bytes(b"two")
        thumb1 = first.temp_path(media1, ".__tgthumb.jpg")
        thumb2 = second.temp_path(media2, ".__tgthumb.jpg")
        thumb1.write_bytes(b"thumb-one")
        thumb2.write_bytes(b"thumb-two")
        assert thumb1 != thumb2
        first.cleanup()
        assert not first.path.exists()
        assert media2.read_bytes() == b"two"
        assert thumb2.read_bytes() == b"thumb-two"
        second.cleanup()
        assert not second.path.exists()

    asyncio.run(run())


def test_different_users_are_isolated_concurrently(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    async def run():
        jobs = await asyncio.gather(*[asyncio.to_thread(create_download_job, uid) for uid in (10, 20)])
        assert jobs[0].path != jobs[1].path
        assert jobs[0].path.parent.parent.name == "10"
        assert jobs[1].path.parent.parent.name == "20"
        await asyncio.gather(*[asyncio.to_thread(job.cleanup) for job in jobs])
        assert all(not job.path.exists() for job in jobs)

    asyncio.run(run())


def test_success_pipeline_has_no_promotional_completion_message():
    source = Path(__file__).parents[1].joinpath("DOWN_AND_UP/down_and_up.py").read_text()
    assert "DOWN_UP_UPLOAD_COMPLETE_MSG" not in source
    assert "CREDITS_MSG" not in source


def test_url_keyboard_flow_has_no_invisible_placeholder():
    source = Path(__file__).parents[1].joinpath("HELPERS/decorators.py").read_text()
    assert 'safe_send_message(user_id, "\\u2063"' not in source
    assert 'edit_message_text(user_id, msg_id, "\\u2063"' not in source
