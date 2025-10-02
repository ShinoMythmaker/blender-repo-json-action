# Blender Repo JSON Updater Action

This action will generate a repo.json file and populate it with data from blender_manifest.toml and latest release zip. 
blender_manifest.toml has to be in the root folder!

## Usage

```yaml
- name: Run blender-repo-json-action
  uses: ShinoMythmaker/blender-repo-json-action@v2
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    GITHUB_REPOSITORY: ${{ github.repository }}
    RELEASE_TAG: ${{ github.event.release.tag_name }}
```
