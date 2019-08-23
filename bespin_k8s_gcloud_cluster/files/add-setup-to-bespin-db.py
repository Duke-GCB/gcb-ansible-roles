from __future__ import print_function
import requests
import os

bespin_api_token = os.environ['BESPIN_API_TOKEN']
bespin_api_admin_url = os.environ['BESPIN_API_URL'] + '/admin/'
lando_host = os.environ['RABBIT_HOST']
lando_user = os.environ['RABBIT_USERNAME']
lando_password = os.environ['RABBIT_PASSWORD']
cluster_name = os.environ['CLUSTER_NAME']
job_runtime_k8s_id = int(os.environ['JOB_RUNTIME_K8S_ID'])
job_flavor_id = int(os.environ['JOB_FLAVOR_ID'])
volume_size_base = int(os.environ['VOLUME_SIZE_BASE'])
volume_size_factor = int(os.environ['VOLUME_SIZE_FACTOR'])

headers = {
    'Authorization': 'Token {}'.format(bespin_api_token),
}


def get_return_json(url):
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


def post_returning_json(url, payload):
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()


print("Listing LandoConnections with queue_name {}".format(cluster_name))
lando_connection_id = None
url = '{}{}'.format(bespin_api_admin_url, 'lando-connections/')
for item in get_return_json(url):
    if item['queue_name'] == cluster_name:
        lando_connection_id = item['id']
        print("Found existing LandoConnection with id {}".format(lando_connection_id))
if not lando_connection_id:
    print("Creating LandoConnection")
    lando_connection_dict = {
        "cluster_type": "k8s",
        "host": lando_host,
        "username": lando_user,
        "password": lando_password,
        "queue_name": cluster_name
    }
    lando_connection_id = post_returning_json(url, lando_connection_dict)['id']
    print("Created LandoConnection with id {}".format(lando_connection_id))
print()

print("Listing JobSettings with name {}".format(cluster_name))
job_settings_id = None
url = '{}{}'.format(bespin_api_admin_url, 'job-settings/')
for item in get_return_json(url):
    if item['name'] == cluster_name:
        job_settings_id = item['id']
        print("Found existing JobSettings with id {}".format(job_settings_id))
if not job_settings_id:
    print("Creating JobSettings with name {}".format(cluster_name))
    job_settings_dict = {
        "name": cluster_name,
        "lando_connection": lando_connection_id,
        "job_runtime_k8s": job_runtime_k8s_id
    }
    job_settings_id = post_returning_json(url, job_settings_dict)['id']
    print("Created JobSettings {}".format(job_settings_id))
print()

print("Listing JobStrategy with name {}".format(cluster_name))
job_strategy_id = None
url = '{}{}'.format(bespin_api_admin_url, 'job-strategies/')
for item in get_return_json(url):
    if item['name'] == cluster_name:
        job_strategy_id = item['id']
        print("Found existing JobStrategy with id {}".format(job_strategy_id))
if not job_strategy_id:
    print("Creating JobStrategy with name {}".format(cluster_name))
    job_strategy_dict = {
        "name": cluster_name,
        "volume_size_base": volume_size_base,
        "volume_size_factor": volume_size_factor,
        "job_settings": job_settings_id,
        "job_flavor": job_flavor_id
    }
    job_strategy_id = post_returning_json(url, job_strategy_dict)['id']
    print("Created JobStrategy {}".format(job_strategy_id))
