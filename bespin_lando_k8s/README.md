# bespin_lando_k8s

Ansible role for deploying [lando](https://github.com/Duke-GCB/lando) for running jobs on a k8s cluster.
This role deploys a pair of containers consisting of a runner(`lando.k8s.lando`) and a watcher(`lando.k8s.watcher`).
A config file is written that is used by the pair of containers.
This role supports deploying multiple pairs of containers to allow bespin to utilize multiple k8s clusters.

## Required fields
- `bespin_settings` dictionary of settings used to deploy lando.k8s.* services.
- `k8s_clusters` dictionary where keys are the names of clusters to setup and the values are configuration used to setup the runner/watcher containers that will monitor the cluster

## Optional fields
- `lando_k8s_state` string that is "present" or "absent" to setup or remove the specified bespin_lando_k8s instances. Defaults to "present".

## Dependencies
None

## Usage

Example role that installs a lando server and watcher with the name "hardspin":
```
...
  roles:
    - role: bespin_lando_k8s
      vars:
        bespin_settings:
          lando:
             build:
               image_name: "lando"
               version: "master"
          rabbit:
            host: "somehost"
            username: "lando"
            password: "secret"
            worker_username: "worker"
            worker_password: "secret"
          web:
            token: "bespin_api_token"
            url: "bespin_api_url"
        k8s_clusters:
          hardspin:
            listen_queue: "hardspin_queue"
            host: "k8shost"
            token: "k8s_access_token"
            namespace: "k8s_namespace_to_run_jobs_under"
            verify_ssl: True
            config_file_data: {} # additional config added to the end of the lando config file
...
```
