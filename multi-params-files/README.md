# Pattern: Multiple `params` files

Project: `multi-params-files/`
```bash 
cd multiple-params-files
```

1. Move custom configurations for some of stages (`data_load` and `train` for this example) in `configs/` folder:

  - `dev`: 'configs/params_dev.yaml'
  - `test`: 'configs/params_test.yaml'
  - `prod`: 'configs/params_prod.yaml'

2. Leave common configurations in `params.yaml`   (including `run_mode`)
  - only few parameters changes for a selected `run_mode` (e.g. name of dataset, sample size, number of epochs)
  - it's easy to control selected params in `.py` code

3. Switch between running modes with a command: 
```bash 
dvc exp run -S run_mode=dev
dvc exp run -S run_mode=test
dvc exp run -S run_mode=prod
```
