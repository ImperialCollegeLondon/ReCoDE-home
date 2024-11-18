from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict

BASE_PATH = "docs/filter"

def get_unique_values(data, field):
    values = set()
    for exemplar in data['exemplars']:
        if ',' in str(exemplar[field]):
            values.update(v.strip() for v in exemplar[field].split(','))
        else:
            values.add(exemplar[field])
    return sorted(values)

def filter_exemplars(data, field, value):
    return {
        'paths': data['paths'],
        'exemplars': [
            e for e in data['exemplars'] 
            if value in str(e[field]).split(', ')
        ],
        'is_main_index': False,
        'current_filter_type': field,
        'current_filter_value': value
    }

def render_template():
    # Load YAML data
    with open('exemplars.yaml', 'r') as f:
        data = yaml.safe_load(f)
    
    # Setup Jinja environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('tools/index.md.jinja')
    exemplar_template = env.get_template('tools/exemplar.md.jinja')
    
    # Create directories
    for dir_name in ['language', 'discipline', 'method']:
        Path(f'{BASE_PATH}/{dir_name}').mkdir(parents=True, exist_ok=True)
    Path('docs/exemplars').mkdir(parents=True, exist_ok=True)

    # Generate main index
    main_data = {**data, 'is_main_index': True}
    with open('docs/index.md', 'w') as f:
        f.write(template.render(**main_data))

    # Generate filter index
    filter_data = {**data, 'is_filter_index': True}
    with open('docs/filter/index.md', 'w') as f:
        f.write(template.render(**filter_data))
    
    # Generate filtered versions
    for field in ['language', 'discipline', 'method']:
        for value in get_unique_values(data, field):
            filtered_data = filter_exemplars(data, field, value)
            filename = f"{BASE_PATH}/{field}/{value.lower().replace(' ', '_')}.md"
            with open(filename, 'w') as f:
                f.write(template.render(**filtered_data))

    # Generate individual exemplar pages
    for exemplar in data['exemplars']:
        filename = f"docs/exemplars/{exemplar['link']}.md"
        with open(filename, 'w') as f:
            f.write(exemplar_template.render(exemplar=exemplar))

if __name__ == '__main__':
    render_template()