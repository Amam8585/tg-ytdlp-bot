"""Process-wide runtime compatibility hooks for the bot and yt-dlp CLI."""

# Python imports ``sitecustomize`` automatically during interpreter startup.
# Keeping this import here also covers the ``python -m yt_dlp`` subprocesses
# used by the bot, not only modules that import the yt-dlp API directly.
import yt_dlp_kvs_compat  # noqa: F401
