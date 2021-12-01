Why? Because it's inconvenient to have a large list of things in `-S` when there are 2 main groups of params (e.g. testing & default/production).

## Single DVC params file

- default run: `dvc exp run`
  - one modified param: `dvc exp run -S epochs=10`
- test run: `dvc exp run -S type=test`
  - one modified param: `dvc exp run -S type=test -S test.epochs=10`

## Multiple DVC params files

- default run: `dvc exp run`
  - one modified param: `dvc exp run -S params-default.yaml:epochs=10`
- test run: `dvc exp run -S params.yaml:file=params-test.yaml`
  - one modified param: `dvc exp run -S params.yaml:file=params-test.yaml -S params-test.yaml:epochs=10`
