# prune\_docker

Removes unused docker containers and images on a host

## Requirements

Docker must be running on the host where this role is deployed.
Requires either `become` privilege escalation or execution by a user with access to docker (e.g. in `docker` group)

## Usage

Run after deploying a new image to clean up old unused images and containers

The following variables can be set, butdefault to `yes`:

- `prune_containers`: If yes, stopped containers will be pruned
- `prune_images`: If yes, unused images will be pruned

## Example:

```
    - role: prune_docker
      become: yes
      vars:
        prune_containers: yes
        prune_images: no
```
