import json
import yaml

def transform(json_data):
    yaml_data = []
    for category, details in json_data['categories'].items():
        new_category = {
            'id': details['id'],
            'title': category,
            'atomic_tests': []
        }
        for test in details['tests']:
            new_test = {
                'id': test['id'],
                'description': test['name'],
                'observations': 'Your observation',
                'reference': test['reference'],
                'objectives': test['objectives'],
                'substeps': [
                    "Your note 1",
                ],
                'wasTested': False,
                'wasVulnerable': False
            }
            new_category['atomic_tests'].append(new_test)
        yaml_data.append({'category': new_category})
    return yaml_data

def json_to_yaml(json_filename, yaml_filename):
    with open(json_filename, 'r') as f:
        json_data = json.load(f)
    yaml_data = transform(json_data)
    with open(yaml_filename, 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True)

json_to_yaml('WSTG.json', 'owstg.yaml')


