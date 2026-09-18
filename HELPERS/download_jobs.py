"""Per-request workspace ownership for download and upload jobs."""

from __future__ import annotations

import os
import logging
import shutil
import uuid
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DownloadJob:
    """A workspace owned by exactly one request.

    User preferences remain in ``users/<id>``; disposable media and thumbnails
    live below the unique job directory and can therefore be cleaned safely.
    """

    user_id: int
    job_id: str
    path: Path

    def temp_path(self, media_path: str | os.PathLike, suffix: str) -> Path:
        media = Path(media_path)
        # The random component also protects two media items with equal titles in
        # a playlist from sharing a thumbnail.
        return self.path / f"{media.stem}.{uuid.uuid4().hex}{suffix}"

    def cleanup(self) -> None:
        root = self.path.resolve()
        downloads_root = (Path("users") / str(self.user_id) / "downloads").resolve()
        if root.parent != downloads_root:
            raise ValueError(f"refusing to clean non-job path: {root}")
        shutil.rmtree(root, ignore_errors=True)
        logger.info("Cleaned download job user=%s job=%s", self.user_id, self.job_id)


def create_download_job(user_id: int, base_dir: str | os.PathLike = "users") -> DownloadJob:
    """Create and return an isolated workspace, safe under concurrency."""
    job_id = uuid.uuid4().hex
    path = Path(base_dir) / str(user_id) / "downloads" / job_id
    path.mkdir(parents=True, exist_ok=False)
    logger.info("Created download job user=%s job=%s path=%s", user_id, job_id, path)
    return DownloadJob(user_id=user_id, job_id=job_id, path=path.resolve())


def cleanup_download_job(path: str | os.PathLike, user_id: int) -> None:
    """Idempotently clean only the explicitly-owned job directory."""
    resolved = Path(path).resolve()
    root = (Path("users") / str(user_id) / "downloads").resolve()
    if resolved.parent != root:
        raise ValueError(f"refusing to clean non-job path: {resolved}")
    shutil.rmtree(resolved, ignore_errors=True)
    logger.info("Cleaned download job user=%s path=%s", user_id, resolved)
