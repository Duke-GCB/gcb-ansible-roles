from __future__ import print_function
import os
import requests

bespin_api_token=os.environ['BESPIN_API_TOKEN']
bespin_api_admin_url = os.environ['BESPIN_API_URL'] + '/admin/'
cluster_name=os.environ['CLUSTER_NAME']

headers = {
    'Authorization': 'Token {}'.format(bespin_api_token),
}

print("Finding JobStrategy with name {}".format(cluster_name))
url = '{}{}?name={}'.format(bespin_api_admin_url, 'job-strategies/', cluster_name)

resp = requests.get(url, headers=headers)
resp.raise_for_status()
matching_items = resp.json()
if matching_items:
    job_strategy_id = matching_items[0]['id']
    print("Deleting JobStrategy {}".format(job_strategy_id))

    url = '{}{}{}'.format(bespin_api_admin_url, 'job-strategies/', job_strategy_id)
    resp = requests.delete(url, headers=headers)
    resp.raise_for_status()
    print("Deleted JobStrategy {}".format(job_strategy_id))
else:
    print("No JobStrategy with name {} found".format(cluster_name))


