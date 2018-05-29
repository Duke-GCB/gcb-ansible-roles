# d4s2_webapp

Ansible role for deploying [D4S2](https://github.com/Duke-GCB/d4s2/)

This role installs 4 docker containers to run the datadelivery web application:

- **db** - PostgreSQL database
- **app** - D4S2 Django Web Application
- **worker** - D4S2 Django Background Task processor
- **web** - Nginx reverse proxy for https

## Dependencies

This role depends on the [docker_webapp](../docker_webapp) role.

## Usage

This role is designed to be used on hosts with docker installed, after the `docker_webapp` role.
It reads host-specific and secret variables, which should be provided securely:

    d4s2_docker_network: d4s2
    d4s2_docker_env:
      D4S2_ALLOWED_HOST: '*'
      D4S2_SECRET_KEY: 'randomly-generated-key-here'
      D4S2_DDSCLIENT_URL: 'https://dataservice.host.com/api/v1'
      D4S2_DDSCLIENT_PORTAL_ROOT: 'https://dataservice.host.com'
      D4S2_DDSCLIENT_OPENID_PROVIDER_ID: 'provider-id-from-dds-openid-provider'
      D4S2_SMTP_HOST: 'smtp.host.com'
      D4S2_DDSCLIENT_AGENT_KEY: 'agent-key-here'
      D4S2_PRODUCTION: '1'
      POSTGRES_USER: 'd4s2_user'
      POSTGRES_PASSWORD: 'generated-postgres-password-here'
      POSTGRES_DB: 'd4s2_db'
      POSTGRES_HOST: 'db'

