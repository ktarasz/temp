from asana import asana
import choice
from pprint import pprint
import requests
import json
asana_api = asana.AsanaAPI('',debug=True)



# tasks = 

# for task in asana_api.get_project_tasks(17412748309135):
# 	resp = requests.post("http://localhost:5000/tasks", 
# 		data=json.dumps({'title': task['name'],
# 			             'project': "54c4e110d54df36a33fb1f72",
# 			             'external_id': {'asana_id': task['id']}}),
# 		headers={'content-type': 'application/json'}
# 	)
# 	if resp.ok:
# 		print task['name'], resp.status_code
# 	else:
# 		import pdb; pdb.set_trace()

# import pdb; pdb.set_trace()
choices = [(item['id'], item['name']) for item in asana_api.list_workspaces()]

workspace = choice.Menu(choices).ask() 

for project in asana_api.list_projects(workspace, include_archived=False):
	# {u'id': 20786005245857, u'name': u'API 0.4'}
	# import pdb; pdb.set_trace()
	extended_project = asana_api.get_project(project['id'])
	resp = requests.post("http://localhost:5000/projects", 
		data=json.dumps({'name': extended_project['name'], 
						 'asana': {
						 		'id': extended_project['id'],
						 		'created_at': extended_project['created_at'],
								'modified_at': extended_project['modified_at'],
								'archived': extended_project['archived']
						 }}),
		headers={'content-type': 'application/json'}
	)
	if resp.ok:
		print project['name'], resp.status_code
	else:
		import pdb; pdb.set_trace()

