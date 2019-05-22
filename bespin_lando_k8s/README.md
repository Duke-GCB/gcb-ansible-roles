# bespin_lando_k8s

Ansible role for deploying [lando](https://github.com/Duke-GCB/lando) as a service for running k8s jobs.
Supports deploying multiple lando instances for running jobs on multiple clusters.

For each cluster this role will
- Writes a config file used by the services based on `bespin_settings`.
- Creates a docker container that will run `lando.k8s.lando` to run jobs in k8s 
- Creates a docker container that will run `lando.k8s.watcher` to watches k8s jobs/send messages to the `lando.k8s.lando` container

## Required fields
- `bespin_settings` dictionary of settings used to deploy lando.k8s.* services. 
For each item in the `bespin_settings.k8s_clusters` dictionary the a
- `k8s_cluster_name` a unique name for this cluster, used as key for reading cluster specific 
settings from `bespin_settings.k8s_clusters` dictionary.

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
            verify_ssl: True
            config_file_data: {} # additional config added to the end of the lando config file
...
```
