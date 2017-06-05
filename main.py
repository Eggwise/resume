import json, yaml
from lib import generate_resume


def json_to_yaml(filename_in, filename_out):
    with open(filename_in) as f:
        resume = json.load(f)

    yaml_resume = yaml.dump(resume, default_flow_style=False)

    with open(filename_out, 'w') as f:
        f.write(yaml_resume)


def yaml_to_json(filename_in, filename_out):
    with open(filename_in, encoding='utf8') as f:
        resume = yaml.load(f)

    json_resume = json.dumps(resume)

    with open(filename_out, 'w') as f:
        f.write(json_resume)

FILENAME_JSON = 'resume.json'
FILENAME_YAML = 'resume.yaml'

yaml_to_json(FILENAME_YAML, FILENAME_JSON)
generate_resume()