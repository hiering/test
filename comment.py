import json
import requests
import os

workflows_runs_url = 'https://api.github.com/repos/hiering/test/actions/workflows/comment.yml/runs'
header = {'Accept':'application/vnd.github.v3+json'}
#with open('/home/runner/work/_temp/_github_workflow/event.json') as event_file:
with open(os.environ['GITHUB_EVENT_PATH']) as event_file:
  github_event = json.load(event_file)

pr_data_url = github_event['issue']['pull_request']['url']
pr_request = requests.get(url=pr_data_url, headers=header)
pr_data = json.loads(pr_request.content)

commit_sha = pr_data['head']['sha']

runs_request = requests.get(url=workflows_runs_url, headers=header)
runs_list = json.loads(runs_request.content)

for run in runs_list['workflow_runs']:
  if run['head_sha'] == commit_sha:
    requests.post(url=)
