import json
import yaml

def convert_to_yaml(owtsg_json):
    yaml_structure = []

    for category_name, category_data in owtsg_json['categories'].items():
        category_id = category_data['id']
        category_tests = category_data['tests']

        category_entry = {
            'id': category_id,
            'title': category_name,
            'children': []
        }

        for test in category_tests:
            test_entry = {
                'id': test['id'],
                'title': test['name'],
                'description': test['objectives'][0],
                'reference': test['reference'],
                'tested': False,
                'isvulnerable': False,
                'observations': '',
                'steps': []
            }

            category_entry['children'].append(test_entry)

        yaml_structure.append(category_entry)

    return yaml_structure

# Read OWTSG.json
with open('WSTG.json') as json_file:
    owtsg_json = json.load(json_file)

# Convert to YAML
yaml_structure = convert_to_yaml(owtsg_json)

# Convert YAML to string
yaml_string = yaml.dump(yaml_structure)

# Print the resulting YAML string
print(yaml_string)
