# bespin\_k8s\_namespace

Ansible role to setup a k8s namespace to run bespin jobs in.

## Requirements

Uses the [k8s](https://docs.ansible.com/ansible/latest/modules/k8s_module.html)
and [k8s_info](https://docs.ansible.com/ansible/devel/modules/k8s_info_module.html)
modules, so install their requirements.

## Usage

This role requires a k8s cluster to create and setup a namespace within.
It requires the following variables to create/delete the namespace:

- `lando_k8s_state`: either 'present' or 'absent' to remove or add the namespace
- `namespace_name`: name of the namespace to be created
- `duke_ds_config_path`: Path to a ddsclient config file to be used for staging data in the namespace
- `stage_system_data_items_path`: Path to a list of files to be staged into a system data volume

See [defaults/main.yml](defaults/main.yml) for optional variables.

It requires environment variables for specifying k8s connection and authentication.
See [k8s documentation](https://docs.ansible.com/ansible/latest/modules/k8s_module.html) for more
