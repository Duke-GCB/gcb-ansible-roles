# data-driven-hypothesis
Ansible role to deploy datadrivenhypothesis.org to an OpenShift cluster.

## Requirements
Uses the [k8s](https://docs.ansible.com/ansible/latest/modules/k8s_module.html) module so install the associated requirements.

Requires `oc` command line utility to login to the OpenShift cluster. Follow 
[instructions for installing oc](https://docs.openshift.com/enterprise/3.0/cli_reference/get_started_cli.html#installing-the-cli).

## Usage
This role requires an OpenShift cluster that a user has already authenticated with.
A convenient method to login is to copy the login command from within the OpenShift console.
Within the OpenShift web console click your email address in the top right corner and choose `Copy Login Command`.
In a terminal window where you will run a playbook that uses this role paste the copied login command. 
Then run your playbook.

Example role:
```
...
  roles:
  - role: data-driven-hypothesis
```
