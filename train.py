import yaml

with open("params.yaml") as fd:
    params = yaml.safe_load(fd)
print(f"INFO:using params type {params['type']}")

# override params with specified type
if params['type'] != 'default':
    params.update(params[params['type']])

print(f"DEBUG:params:{params}")
