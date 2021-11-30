# Multiple DVC params files

Why? Because it's inconvenient to have a large list of things in `-S` when there are 2 main groups of params (e.g. testing & default/production).

- default run: `dvc exp run`
  - one modified param: `dvc exp run -S params-default.yaml:epochs=10`
- test run: `dvc exp run -S params.yaml:file=params-test.yaml`
