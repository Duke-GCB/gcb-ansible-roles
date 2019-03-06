# bespin_lando_k8s

Ansible role for deploying [lando](https://github.com/Duke-GCB/lando) as services for running k8s jobs.
- Writes a config file `/etc/lando_k8s_config.yml` based on `bespin_settings`.
- Creates a docker container that will run `lando.k8s.lando` to run jobs in k8s 
- Creates a docker container that will run `lando.k8s.watcher` to watches k8s jobs/send messages to the `lando.k8s.lando` container
