# Pattern: Single `params.yaml` file 
Project: `single-params-yaml/`
```bash 
cd single-params-yaml
```

1. Use custom parameters updates, when:
  - only few parameters changes for a selected `run_mode` (e.g. name of dataset, sample size, number of epochs)
  - it's easy to control selected params in `.py` code

Examples: `data_load` and `train` stages
```bash 
dvc exp run -S train.epochs=10
dvc exp run -S data_load.dataset=micro -S train.epochs=10
```

2. Use parameters `presets`, when:
  - stage configuration is large and depends on selected `run_mode` (`dev/test/prod`) or model (estimator)
  - it's easy to control selected params in `.py` code 

Examples:  `data_load_with_preset` stage
```bash 
dvc exp run -S run_mode=dev
dvc exp run -S run_mode=test
dvc exp run -S run_mode=prod
```

