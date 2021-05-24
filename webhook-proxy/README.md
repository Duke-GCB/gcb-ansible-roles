# webhook-proxy

Ansible role for deploying nginx/letsencrypt as a webhook proxy for Openshift.

## Requirements

The following variables need to be defined before running this role:
- `domain`: proxy website url
- `sysadmin_email`: support email address for letsencrypt
- `openshift_url`: url of openshift
