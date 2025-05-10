from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict

BASE_PATH = "docs/filter"

def get_unique_values(data, field):
    values = set()
    for exemplar in data['exemplars']:
        if isinstance(exemplar[field], str):
            values.update(v.strip() for v in exemplar[field].split(','))
        else:
            values.add(str(exemplar[field]).strip())
    return sorted(values)

def filter_exemplars(data, field, value):
    return {
        'paths': data['paths'],
        'exemplars': [
            e for e in data['exemplars'] 
            if value in [v.strip() for v in str(e[field]).split(',')]
        ],
        'is_main_index': False,
        'current_filter_type': field,
        'current_filter_value': value
    }

def adjust_paths(data, depth):
   """Adjust paths based on depth: 0 for main, 1 for filter, 2 for categories"""
   new_data = data.copy()
   if depth == 0:
       return new_data
   relative_base = '../' * depth
   new_data['paths'] = {k: f"{relative_base}{v.lstrip('./')}" for k, v in data['paths'].items()}
   return new_data

def render_template():
    # Load YAML data
    with open('exemplars.yaml', 'r') as f:
        data = yaml.safe_load(f)
    
    # Setup Jinja environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('tools/index.md.jinja')
    exemplar_template = env.get_template('tools/exemplar.md.jinja')
    people_template = env.get_template('tools/people.md.jinja')
    
    # Create directories
    for dir_name in ['language', 'discipline', 'method']:
        Path(f'{BASE_PATH}/{dir_name}').mkdir(parents=True, exist_ok=True)
    Path('docs/exemplars').mkdir(parents=True, exist_ok=True)

    # Generate main index (depth 0)
    main_data = adjust_paths(data, 0)
    main_data['is_main_index'] = True
    with open('docs/index.md', 'w') as f:
        f.write(template.render(**main_data))

    # Generate filter index (depth 1)
    filter_data = adjust_paths(data, 1)
    filter_data['is_filter_index'] = True
    with open('docs/filter/index.md', 'w') as f:
        f.write(template.render(**filter_data))

    # Generate filtered versions (depth 2)
    for field in ['language', 'discipline', 'method']:
        for value in get_unique_values(data, field):
            filtered_data = adjust_paths(filter_exemplars(data, field, value), 3)
            filename = f"{BASE_PATH}/{field}/{value.lower().replace(' ', '_')}.md"
            with open(filename, 'w') as f:
                f.write(template.render(**filtered_data))

    # Generate individual exemplar pages
    for exemplar in data['exemplars']:
        filename = f"docs/exemplars/{exemplar['link']}.md"
        with open(filename, 'w') as f:
            f.write(exemplar_template.render(exemplar=exemplar))
            
    # Generate people page
    with open('docs/people.md', 'w') as f:
        f.write(people_template.render(exemplars=data['exemplars']))

if __name__ == '__main__':
    render_template()