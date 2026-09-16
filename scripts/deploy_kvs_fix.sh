#!/usr/bin/env bash
set -Eeuo pipefail

# One-command Ubuntu deployment. An optional first argument selects the branch
# to deploy; otherwise the server's currently checked-out branch is updated.
repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

branch="${1:-$(git branch --show-current)}"
if [[ -z "$branch" ]]; then
    echo "Cannot determine a branch; pass it as the first argument." >&2
    exit 1
fi

echo "Updating $repo_dir from origin/$branch..."
git fetch origin "$branch"
git checkout "$branch"
git pull --ff-only origin "$branch"

compose=(docker compose)
if ! docker compose version >/dev/null 2>&1; then
    compose=(docker-compose)
fi

echo "Building the application image..."
"${compose[@]}" build --pull app

echo "Running KVS regression tests inside the built image..."
"${compose[@]}" run --rm --no-deps --entrypoint python app \
    -m pytest -q tests/test_kvs_compat.py

echo "Recreating the bot with the verified image..."
"${compose[@]}" up -d --no-deps --force-recreate app
"${compose[@]}" ps app
echo "Deployment complete."
