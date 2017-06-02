import json, yaml

FILENAME = 'resume.json'



with open(FILENAME) as f:

    resume = json.load(f)



OUTPUT_FILENAME = 'resume.yaml'
yaml_resume = yaml.dump(resume, default_flow_style=False)

with open(OUTPUT_FILENAME, 'w') as f:

    f.write(yaml_resume)