# postgres\_backup

Creates a cron job that runs a docker container to backup a postgres database onto nfs.

## Requirements

Docker must be running on the host where this role is deployed.
Must be run in a playbook including the role (must be `sudo` or `become` since role installs packages and adds a backup user).

## Usage

It requires the following variables to setup the backup cron job:

- `database_image`: name of the postgres image to use for performing the backup eg. "postgres:9.5"
- `database_host`: host the database is running on
- `database_name`: name of the database to backup
- `database_username`: username to use to log into the database
- `database_password`: password to use to log into the database
- `nfs_mount_device`: device where we will backup the database to
- `nfs_mount_dir`: name of the directory where the nfs device will be mounted

Optional variables customizing backup operation:

- `database_port`: Port postgres is listening on. Defaults to standard postgres port 5432
- `backup_filename_prefix`: Prefix to put in front of the backup filenames.
- `backup_user_home`: User home directory
- `docker_network_name`: Name of docker network to use when backing up 

## Example:

```
    - role: postgres_backup
      vars:
        database_image: "postgres:9.5"
        database_host: "bespin-dev-database"
        database_name: "bespin"
        database_username: "lando"
        database_password: "secret"
        nfs_mount_device: "someserver:/somepath/pgbup/bespin-dev-backups"
        nfs_mount_dir: "/mnt/pgbup"
        backup_filename_prefix: "bespin-dev"
```
