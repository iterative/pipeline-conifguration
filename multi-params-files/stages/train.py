import yaml


print("Stage: TRAIN")

# Load main config (params.yaml)
with open("params.yaml") as fd:
    params = yaml.safe_load(fd)
    
# Load a stage config for the current run_mode 
run_mode = params['run_mode'] 
stage_config_file = params['configs'][run_mode]
with open(stage_config_file) as fd:
    train_config = yaml.safe_load(fd)['train']

print(f"INFO:  Running mode:     {run_mode}")
print(f"INFO:  Use stage config: {stage_config_file}")
print(f"INFO:  Train params:     {train_config}")