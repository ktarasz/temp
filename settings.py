API_NAME = 'TIME TRACK API'
PAGINATION = False
PAGINATION_LIMIT = 100
PAGINATION_DEFAULT = 100 
HATEOAS = False
IF_MATCH = False
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
MONGO_HOST = 'localhost'
MONGO_PORT = 5001
MONGO_DBNAME = 'apitest'


projects = {
    'item_title': 'project',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],
    'schema': {
	    'name': {
	        'type': 'string',
	        'required': True
	    },
	    'asana':{
	    	'type': 'dict',
	    	'schema': {
	    		'id': {'type': 'number'},
	    		'created_at': {'type': 'datetime'},
	    		'modified_at': {'type': 'datetime'},
	    		'archived': {'type': 'boolean'},
	    	}
	    },
		'basecamp_id': {
			'type': 'string'
		}
	}
}


tasks = {
    'item_title': 'task',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],
    'schema': {
	    'name': {'type': 'string', 'required': True},
	    'project': {
		    'type': 'objectid',
		    'required': True,
	    	'data_relation': {
	    		'resource': 'projects',
	    		'field': '_id',
	    		'embeddable': False
	    	}
	    },
	    'parent_id': {
		    'type': 'objectid',
	    	'data_relation': {'resource': 'task'}
	    },
	    'asana': {
	    	'type': 'dict',
	    	'schema': {
	    		'id': {'type': 'number'},
	    		'created_at': {'type': 'datetime'},
			    'completed': {'type': 'boolean'},
			    'completed_at': {'type': 'datetime'},
			    'modified_at': {'type': 'datetime'},
	    	}
	    },
	    'basecamp_id': {'type': 'string'},	    
	    'time':{
	    	'type': 'list',
	    	'schema': {
	    		'notes' : {'type': 'string'},
	    		'time': {
	    			'required': True,
	    			'type': 'float'
	    		}

	    	}
	    }
	}
}

DOMAIN = {'projects': projects, 'tasks': tasks}
