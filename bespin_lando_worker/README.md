# bespin_lando_worker

Ansible role for deploying [lando](https://github.com/Duke-GCB/lando) in worker configuration along with cwltool and a utility package used for data staging/etc.

This role installs the following:
- **lando** - Code that will read messages related to staging data, running a specific workflow, and storing output
- **cwltool** - Program to use for running the workflow, cwltool can be overridden if the tool is installable via pip3.
- **lando-util** - Utility program used to use for staging data, organizing output and uploading results by default this is [lando-util](https://github.com/Duke-GCB/lando-util).

This role sets up lando as a service and creates a nfs mount.
By default lando, cwltool and lando-util are installed via pip.

## Required fields
- `lando_version` version of lando to install from pypi
- `cwl_runner_version` version of cwltool to install from pypi
- `util_package_version` version of lando-util to install from pypi

## Optional fields
- `lando_install_source` defaults to `PyPI` other supported value is `GitHub`
- `lando_github_version` branch to install from github when `lando_install_source` is set to `GitHub`
- `cwl_runner` name of workflow runner software to install from pypi (defaults to `cwltool`)
- `util_package_name` name of the utility package to install from pypi (defaults to `lando-util`)
- `lando_work_directory` WorkingDirectory used for lando-worker service (defaults to `/work`)
- `worker_mount_name` - name of nfs to mount (defaults to `/data`)
- `worker_mount_src`- src nfs to mount (defaults to `bespin-nfs:/mnt/bespin_datasets`)

## Dependencies
None

## Usage

Example role that installs with required specific versions:
```
...
  roles:
    - role: bespin_lando_worker
      lando_version: 0.9.3
      cwl_runner_version: 1.0.20180912090223
      util_package_version: 0.5.0
...
```
