import yaml

with open("params.yaml") as fd:
    params = yaml.safe_load(fd)['file']
print(f"INFO:using params file {params}")

with open(params) as fd:
    params = yaml.safe_load(fd)
print(f"DEBUG:contents:{params}")
