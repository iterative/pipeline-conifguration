import yaml


print("Stage: DATA_LOAD")

# Load main config (params.yaml)
with open("params.yaml") as fd:
    params = yaml.safe_load(fd)
    
# Load a stage config for the current run_mode 
run_mode = params['run_mode'] 
stage_config_file = params['configs'][run_mode]
with open(stage_config_file) as fd:
    data_load_config = yaml.safe_load(fd)['data_load']
    
# Get sampling size (if sampling is enabled)
if data_load_config['sampling']['enable'] is True:
    sampling_size = data_load_config['sampling']['size']

print(f"INFO:  Running mode:     {run_mode}")
print(f"INFO:  Use stage config: {stage_config_file}")
print(f"INFO:  Dataset:          {data_load_config['dataset']}")
print(f"INFO:  Sampling enabled: {data_load_config['sampling']['enable']}")
print(f"INFO:  Sampling size:    {sampling_size}")
