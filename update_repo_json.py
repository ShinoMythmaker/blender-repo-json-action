import os
import toml
import json
import hashlib
import requests

GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
RELEASE_TAG = os.environ.get("RELEASE_TAG", "")
MANIFEST_FILE = "blender_manifest.toml"
REPO_JSON_FILE = "repo.json"

def get_latest_release():
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/releases/tags/{RELEASE_TAG}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def download_asset(asset):
    asset_url = asset["url"]
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/octet-stream"
    }
    resp = requests.get(asset_url, headers=headers)
    resp.raise_for_status()
    fname = asset["name"]
    with open(fname, "wb") as f:
        f.write(resp.content)
    return fname

def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    # Load manifest from TOML
    manifest = toml.load(MANIFEST_FILE)

    release = get_latest_release()
    zip_asset = next((a for a in release["assets"] if a["name"].endswith(".zip")), None)
    if not zip_asset:
        print("No ZIP asset found in release!")
        exit(1)
    zip_filename = download_asset(zip_asset)
    zip_size = os.path.getsize(zip_filename)
    zip_hash = sha256sum(zip_filename)
    zip_url = zip_asset["browser_download_url"]

    repo_data = {
        "version": "v1",
        "blocklist": [],
        "data": [
            {
                "schema_version": "1.0.0",
                "id": manifest.get("id", ""),
                "name": manifest.get("name", ""),
                "tagline": manifest.get("tagline", ""),
                "version": manifest.get("version", ""),
                "type": manifest.get("type", "add-on"),
                "maintainer": manifest.get("maintainer", ""),
                "license": manifest.get("license", []),
                "blender_version_min": manifest.get("blender_version_min", ""),
                "blender_version_max": manifest.get("blender_version_max", ""),
                "website": manifest.get("website", ""),
                "permissions": manifest.get("permissions", {}),
                "tags": manifest.get("tags", []),
                "archive_url": zip_url,
                "archive_size": zip_size,
                "archive_hash": f"sha256:{zip_hash}"
            }
        ]
    }

    if os.path.exists(REPO_JSON_FILE):
        with open(REPO_JSON_FILE, "r") as f:
            old = json.load(f)
        repo_data["blocklist"] = old.get("blocklist", [])
        # For multi-addon support, you could merge repo_data["data"] with old["data"]

    with open(REPO_JSON_FILE, "w") as f:
        json.dump(repo_data, f, indent=2)
    print("repo.json updated.")

if __name__ == "__main__":
    main()