# bespin\_k8s\_gcloud\_cluster

Ansible role to create a google cloud k8s cluster and create a namespace to run bespin jobs in.

## Requirements

Uses the [bespin_k8s_namespace](../bespin_k8s_namespace/README.md) ansible role, so install it's requirements.

Command line tool requirements:
- gcloud has been installed (including [beta components](https://cloud.google.com/sdk/gcloud/reference/components/install)) and is authenticated to google cloud
- kubectl has been installed
- ansible has been installed
- helm has been installed
- python and the requests module have been installed (used to communicate with bespin-api)
- connected to the bespin-api network

## Usage

This role requires gcloud to logged in.
It requires the following variables:
- `lando_k8s_state`: either 'present' or 'absent' to remove or add the namespace
- `gcloud_project_id`: name of the google cloud project to create a cluster within
- `gcloud_compute_zone`: name of the google cloud zone to create the cluster in
- `cluster_name`: Name of the k8s cluster
- `gcloud_machine_type`: google cloud machine type to be used in the cluster's default pool
- `gcloud_num_nodes`: number of nodes to create in the default pool
- `gcloud_min_nodes`: min number of nodes allowed in the default pool
- `gcloud_max_nodes`: max number of nodes allowed in the default pool
- `large_pool_machine_type`: google cloud machine type to be used in the cluster's large machine pool
- `large_pool_num_nodes`: number of nodes to create in the large machine pool
- `large_pool_min_nodes`: min number of nodes allowed in the large machine pool
- `large_pool_max_nodes`: max number of nodes allowed in the large machine pool
- `namespace_name`: Name of the namespace to create inside the cluster
- `filestore_name`: Name of the filestore used to provide ReadWriteMany volumes
- `file_share_capacity`: Size in GB of the ReadWriteMany k8s storage used when running a job
- `file_share_name`: Name of the file share
- `file_store_tier`: Tier to use for the file share
- `job_runtime_k8s_id`: ID that specifies the set of commands to be run (this is the primary key of a pre-existing JobRuntimeK8s record in bespin-api)
- `job_flavor_id`: ID that specifies cpus counts and memory size (this is the primary key of a JobFlavor record in bespin-api)
- `volume_size_base`: Base volume size in GB associated with JobStrategy that will be created for jobs in this cluster
- `volume_size_factor`: factor used in determining volume size associated with this JobStrategy
- `duke_ds_config_path`: Path to a ddsclient config file to be used for staging data in the namespace
- `stage_system_data_items_path`: Path to a list of files to be staged into a system data volume

See [defaults/main.yml](defaults/main.yml) for optional variables.
