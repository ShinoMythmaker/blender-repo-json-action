# Blender Repo JSON Updater Action

## Usage

```yaml
- name: Update repo.json
  uses: youruser/blender-repo-json-action@v1
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    GITHUB_REPOSITORY: ${{ github.repository }}
    RELEASE_TAG: ${{ github.event.release.tag_name }}
```