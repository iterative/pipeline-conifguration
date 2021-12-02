import yaml


print("Stage: DATA_LOAD")

with open("params.yaml") as fd:
    params = yaml.safe_load(fd)
    run_mode = params['run_mode']
    
# get stage configs
data_load_preset = params['data_load_with_preset'][run_mode]

print(f"INFO:  run mode: {run_mode}")
print(f"DEBUG: dataset:  {data_load_preset['name']}")
print(f"INFO:  Sampling size: {data_load_preset['size']}")
