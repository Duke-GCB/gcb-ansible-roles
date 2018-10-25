# bespin_lando_worker

Ansible role for deploying [lando](https://github.com/Duke-GCB/lando) in worker configuration along with cwltool.

This role installs the following:
- **lando** - Code that will read messages related to staging data, running a specific workflow, and storing output
- **cwltool** - Program to use for running the workflow, cwltool can be overridden if the tool is installable via pip3.

This role sets up lando as a service and creates a nfs mount.
Lando is installed directly from github repository.
cwltool is installed via pypi release.

## Dependencies
None

## Usage

By default deploys latest lando and cwltool.
Users can select a specific version in a playbook like so:
```
...
  roles:
    - role: bespin_lando_worker
      lando_version: 0.9.3
      cwl_runner_version: 1.0.20180912090223
...
```
