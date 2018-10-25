# build\_docker\_image

Ansible role for building a docker image from a git repo

## Requirements

Uses the [docker_image](https://docs.ansible.com/ansible/2.6/modules/docker_image_module.html) and [git](https://docs.ansible.com/ansible/2.6/modules/git_module.html) modules, so requires docker and git installed.

## Usage

This role is designed to be called just before deploying a docker container with the [docker_container](https://docs.ansible.com/ansible/2.6/modules/docker_container_module.html) module.

It requires the following variables to build the docker image:

- `repo_url`: URL of git repo containing a Dockerfile in the root.
- `version`: tag, branch, or commit to check out from Git repo. Will also be used for the docker image tag
- `image_name`: Name of the docker image to build.

Optional variables for building a second image from the same repo:

- `secondary_context`: Subdirectory in the repo to use as docker build context for secondary image.
- `secondary_version`: Tag to use when building the secondary image.
- `secondary_buildargs`: Dictionary of build arguments to pass to the secondary build

## Examples:

Build an image `lando:0.6.3` from the repo at `https://github.com/Duke-GCB/bespin-lando`

    repo_url: https://github.com/Duke-GCB/bespin-lando
    version: 0.6.3
    image_name: lando

Build `bespin-api:v1.5.2` then `bespin-api:v1.5.2-apache` from tag `v1.5.2` of `https://github.com/Duke-GCB/bespin-api`, the latter built from the `apache-docker` subdirectory

    version: v1.5.2
    repo_url: https://github.com/Duke-GCB/bespin-api
    image_name: "bespin-api"
    secondary_context: "apache-docker"
    secondary_version: "v1.5.2-apache"
    secondary_buildargs: { BASE_IMAGE: "bespin-api:v1.5.2" }

To avoid repeating version numbers, use variables wherever possible.
