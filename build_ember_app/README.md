# build\_ember\_app

Ansible role for building an Ember application into a docker volume from a git repo

## Requirements

Uses the [docker_container](https://docs.ansible.com/ansible/2.6/modules/docker_container_module.html), [docker_volume](https://docs.ansible.com/ansible/2.6/modules/docker_volume_module.html) and [git](https://docs.ansible.com/ansible/2.6/modules/git_module.html) modules, so requires docker and git installed.

## Usage

This role uses a nodejs Docker image to build the application from source into a named docker volume..
build\_ember\_app is designed to run before [bespin_web](../bespin_web), where a Docker container running a web server serves a pre-built Ember application from a named docker volume.

It requires the following variables to build the docker image:

- `repo_url`: URL of git repo containing an Ember application
- `version`: tag, branch, or commit to check out from Git repo.
- `repo_name`: Name of the application to build. Just used for local directory uniqueness (e.g. so that the same host can build two different ember apps)
- `target_volume`: Name of docker volume to create and place built application. Note that this is a named docker volume, not a host path.
- `build_environment`: Dictionary of environment variables and values to provide at build-time

## Examples:

Build the ember app from the tag `v0.6.3` the repo at `https://github.com/Duke-GCB/bespin-ui` using the production `JOB_WATCHER_URL`. Place the built `index.html` and other assets in a volume called `bespin-ui-v0.6.3`

    repo_url: https://github.com/Duke-GCB/bespin-ui
    version: v0.6.3
    repo_name: bespin-ui
    target_volume: bespin-ui-v0.6.3
    build_environment: { JOB_WATCHER_URL: wss://bespin-ws-prod.gcb.duke.edu }

To avoid repeating version numbers, use variables wherever possible.
