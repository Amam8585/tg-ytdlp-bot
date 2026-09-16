import pytest
from yt_dlp import YoutubeDL
from yt_dlp.extractor.generic import GenericIE
from yt_dlp.utils import ExtractorError

import yt_dlp_kvs_compat  # noqa: F401  (ensures patch under all test runners)


URL = "https://example.com/videos/demo/"
VIDEO_URLS = {
    "video_url": "https://cdn.example.com/get_file/1/abc/video_360p.mp4",
    "video_alt_url": "https://cdn.example.com/get_file/1/def/video_480p.mp4",
    "video_alt_url2": "https://cdn.example.com/get_file/1/ghi/video_720p.mp4",
    "video_alt_url3": "https://cdn.example.com/get_file/1/jkl/video_1080p.mp4",
}


def _object(extra=""):
    urls = ",\n".join(
        f"{key}: '{value}', {key}_text: '{height}'"
        for (key, value), height in zip(VIDEO_URLS.items(), ("360p", "480p", "720p", "1080p"))
    )
    return "{" + f"""
        video_id: '42',
        license_code: '1234567890123456',
        preview_url: '//cdn.example.com/preview.jpg',
        {urls}
        {extra}
    """ + "}"


def _page(declaration):
    return f"""<!doctype html><html><head>
      <title>Video: Dynamic KVS demo</title>
      <link rel="canonical" href="https://example.com/videos/demo/">
    </head><body><script>{declaration}</script></body></html>"""


def _extract(page):
    with YoutubeDL({"quiet": True}) as ydl:
        return GenericIE(ydl)._extract_kvs(URL, page, "demo")


def test_legacy_flashvars_behavior_is_preserved():
    info = _extract(_page(f"var flashvars = {_object()};"))
    assert info["id"] == "42"
    assert len(info["formats"]) == 4


@pytest.mark.parametrize("name", [
    "t7591bc940b", "abc123", "_player987", "$kvsPlayer", "KVS_DATA_123",
])
def test_dynamic_kvs_variable_names(name):
    info = _extract(_page(f"var {name} = {_object()};"))
    assert info["id"] == "42"
    assert [item["height"] for item in info["formats"]] == [360, 480, 720, 1080]
    assert all(item["http_headers"] == {"Referer": URL} for item in info["formats"])
    assert all("/get_file/" in item["url"] for item in info["formats"])


def test_balanced_object_and_multiple_script_tags():
    page = """<html><head><title>Nested object</title></head><body>
      <script>var unrelated = {video_id: 'wrong', nested: {value: '}'}};</script>
      <script>const player_data = %s;</script>
    </body></html>""" % _object(", metadata: {nested: {enabled: true}}")
    info = _extract(page)
    assert info["id"] == "42"
    assert len(info["formats"]) == 4


@pytest.mark.parametrize("candidate", [
    "var random = {answer: 42, video_url: '/get_file/nope'};",
    "var missing_license = {video_id: '42', video_url: '/get_file/nope'};",
    "var missing_id = {license_code: '1234', video_url: '/get_file/nope'};",
])
def test_non_kvs_objects_are_rejected(candidate):
    with pytest.raises(ExtractorError, match="Unable to extract flashvars"):
        _extract(_page(candidate))


def test_multiple_objects_selects_only_complete_kvs_config():
    page = _page(
        "var first = {video_id: 'wrong', video_url: '/get_file/nope'};"
        "let second = {license_code: 'wrong', video_url: '/get_file/nope'};"
        f"const actual = {_object()};")
    assert _extract(page)["id"] == "42"


def test_upstream_url_transform_remains_in_use():
    plain = "https://cdn.example.com/get_file/1/hash/video.mp4"
    assert GenericIE._kvs_get_real_url(plain, "1234") == plain
