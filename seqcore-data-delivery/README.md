# seqcore-data-delivery
Ansible role to deploy sequencing core data delivery scripts.

## Requirements
Requires `git` and `python3` to be installed on the target server.

## Usage

Example role:
```
...
  roles:
  - role: seqcore-data-delivery
```

Optional variables:
- seqcore_repo: url to repo to clone
- seqcore_repo_version: branch/tag from the repo to check out
- seqcore_repo_dest: path to clone the repo on the target server
