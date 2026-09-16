"""Compatibility support for KVS players that use dynamic variable names.

KVS used to expose its player configuration as ``var flashvars = {...}``.
Some current deployments generate the variable name per page.  yt-dlp's
GenericIE still keys discovery to ``flashvars`` (as of 2026.08.30), although
the rest of its KVS implementation can already process these configurations.

This module deliberately patches only the discovery failure.  Once a
structurally valid KVS object is found, the original yt-dlp implementation is
called with a synthetic ``flashvars`` declaration.  URL decoding, resolution
parsing, Referer headers, and all future upstream behavior therefore remain
owned by yt-dlp.
"""

from __future__ import annotations

import json
import re
from functools import wraps

from yt_dlp.extractor.generic import GenericIE
from yt_dlp.utils import ExtractorError, js_to_json


_DECLARATION_RE = re.compile(
    r"\b(?:var|let|const)\s+[A-Za-z_$][\w$]*\s*=\s*(?={)")
_VIDEO_URL_RE = re.compile(r"^video_(?:url|alt_url\d*)$")
_PATCH_FLAG = "_tg_ytdlp_dynamic_kvs_patch"


def _find_dynamic_kvs_config(extractor, webpage: str, video_id: str):
    """Return the first structurally valid KVS configuration, if present.

    ``InfoExtractor._search_json`` supplies balanced-object extraction and
    yt-dlp's JavaScript-to-JSON conversion.  Iterating declarations lets us
    skip unrelated objects and malformed candidates without inventing a
    second JavaScript parser.
    """

    for declaration in _DECLARATION_RE.finditer(webpage):
        config = extractor._search_json(
            r"\A",
            webpage[declaration.end() :],
            "dynamic KVS configuration",
            video_id,
            transform_source=js_to_json,
            fatal=False,
            default=None,
        )
        if not isinstance(config, dict):
            continue
        if not config.get("video_id") or not config.get("license_code"):
            continue
        if not any(
                _VIDEO_URL_RE.fullmatch(key)
                and isinstance(value, str)
                and "/get_file/" in value
                for key, value in config.items()):
            continue
        return config
    return None


def install_dynamic_kvs_compat() -> bool:
    """Install the compatibility wrapper once; return whether it was added."""

    original = GenericIE._extract_kvs
    if getattr(original, _PATCH_FLAG, False):
        return False

    @wraps(original)
    def extract_kvs(extractor, url, webpage, video_id):
        try:
            return original(extractor, url, webpage, video_id)
        except ExtractorError as error:
            # Do not conceal errors from later stages of upstream extraction.
            if "Unable to extract flashvars" not in str(error):
                raise
            discovery_error = error

        config = _find_dynamic_kvs_config(extractor, webpage, video_id)
        if config is None:
            raise discovery_error

        # JSON is also valid JavaScript.  Appending rather than replacing page
        # content retains title/canonical metadata used by GenericIE.
        compatible_webpage = (
            f"{webpage}\n<script>var flashvars = "
            f"{json.dumps(config, ensure_ascii=False)};</script>")
        return original(extractor, url, compatible_webpage, video_id)

    setattr(extract_kvs, _PATCH_FLAG, True)
    GenericIE._extract_kvs = extract_kvs
    return True


install_dynamic_kvs_compat()
