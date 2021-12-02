# Multiple DVC params

Why? Because it's inconvenient to have a large list of things in `-S` when there are 2 main groups of params (e.g. testing & default/production).

- default run: `dvc exp run`

# Patterns

## 1. Single `params.yaml` file 
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

## 2. Multiple `params` files
Project: `multiple-params-files/`
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

## Install

```bash
python3 -m venv venv
echo 'export PYTHONPATH=.' >> venv/bin/activate
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Setup linting

Make dir `.vscode` and create config file `settings.json`:

```bash
mkdir -p .vscode
touch .vscode/settings.json
```

Add parameters to `settings.json`:

```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.lintOnSave": true
}
```
