# copy_bespin_hosts

Ansible role that copies a list of Bespin hostname/IPs to /etc/hosts [bespin](https://github.com/Duke-GCB/bespin-api/)

This role fills in the list of necessary hostname/IP entries for the components of Bespin.
This role also creates an ansible fact to allow looking up IP from hostname in the form of a dictionary name `bespin_hosts_list`.


## Usage

This role requires the inventory to contain the necessary bespin component aliases and expects the
 ansible fact named `bespin_env` to contain the name of the environment we are installing
 bespin under (eg. 'dev' or 'prod')

For example a dev inventory would look like so:
```
[bespin_dev]
bespin_dev_rabbit ansible_host=<rabbit-ip-address>
bespin_dev_web ansible_host= ansible_host=<web-ip-address>
bespin_dev_lando ansible_host=<lando-ip-address>
bespin_dev_database ansible_host=<database-ip-address>
bespin_dev_nfs ansible_host=<nfs-ip-address>
bespin_dev_job_watcher ansible_host=<job-watcher-ip-address>
 ```

You can specify the `bespin_env` fact for this group like so: 
```
[bespin_dev:vars]
bespin_env=dev
```
