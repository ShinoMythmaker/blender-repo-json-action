# Blender Repo JSON Updater Action
<a href="https://www.paypal.com/donate/?hosted_button_id=VVSSL3GDRSBNC"><img alt="Sponsor Badge" src="https://img.shields.io/badge/Mythmaker-Sponsor-pink?style=flat"></a>

This action will generate a repo.json file and populate it with data from blender_manifest.toml and latest release zip. 
blender_manifest.toml has to be in the root folder!

## Usage

```yaml
- name: Run blender-repo-json-action
  uses: ShinoMythmaker/blender-repo-json-action@v3
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    GITHUB_REPOSITORY: ${{ github.repository }}
    RELEASE_TAG: ${{ github.event.release.tag_name }}
```
