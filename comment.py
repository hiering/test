import json
import requests
import os

GH_USER = 'runner'
GH_TOKEN = os.environ['TOKEN']

header = {'Accept':'application/vnd.github.v3+json'}
with open(os.environ['GITHUB_EVENT_PATH']) as event_file:
  github_event = json.load(event_file)

pr_data_url = github_event['issue']['pull_request']['url']
pr_request = requests.get(url=pr_data_url, auth=(GH_USER, GH_TOKEN), headers=header)
pr_data = json.loads(pr_request.content)

commit_sha = pr_data['head']['sha']

runs_request = requests.get(url='https://api.github.com/repos/hiering/test/actions/workflows/comment.yml/runs', auth=(GH_USER, GH_TOKEN), headers=header)
runs_list = json.loads(runs_request.content)

for run in runs_list['workflow_runs']:
  if run['head_sha'] == commit_sha:
    re_run = requests.post(url=f'https://api.github.com/repos/hiering/test/actions/runs/{run["id"]}/rerun', auth=(GH_USER, GH_TOKEN), headers=header)
