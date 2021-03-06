"""
API MAPPING FOR StatusPage API V1
"""


import re


mapping_table = {

    'content_type': 'application/x-www-form-urlencoded',
    'path_prefix': '/v1',

    # Components
    'get_components': {
        'path': '/pages/{{page}}/components.json'
    },
    'get_component': {
        'path': '/pages/{{page}}/components/{{component}}.json'
    },
    'update_component': {
        'method': 'PATCH',
        'path': '/pages/{{page}}/components/{{component}}.json',
        'valid_params': ['component[status]']
    },
    'get_component_subscribers': {
        'path': '/pages/{{page}}/components/{{component}}/subscribers.json'
    },

    # Incidents
    'get_incidents': {
        'path': '/pages/{{page}}/incidents.json'
    },
    'get_incident': {
        'path': '/pages/{{page}}/incidents/{{incident}}.json'
    },
    'get_unresolved_incidents': {
        'path': '/pages/{{page}}/incidents/unresolved.json'
    },
    'delete_incident': {
        'method': 'DELETE',
        'path': '/pages/{{page}}/incidents/{{incident}}.json',
    },
    'update_incident': {
        'method': 'PATCH',
        'path': '/pages/{{page}}/incidents/{{incident}}.json',
        'valid_params': ['incident[name]','incident[status]','incident[message]','incident[wants_twitter_update]','incident[impact_override]',re.compile('^incident\[components\]\[[a-z0-9]+\]$'),'incident[component_ids][]']
    },
    'get_incident_subscribers': {
        'path': '/pages/{{page}}/incidents/{{incident}}/subscribers.json'
    },

    # Subscribers
    'get_subscribers': {
        'path': '/pages/{{page}}/subscribers.json'
    },

}
