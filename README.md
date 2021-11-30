# Multiple DVC params groups

Why? Because it's inconvenient to have a large list of things in `-S` when there are 2 main groups of params (e.g. testing & default/production).

- default run: `dvc exp run`
  - one modified param: `dvc exp run -S epochs=10`
- test run: `dvc exp run -S type=test`
  - one modified param: `dvc exp run -S type=test -S test.epochs=10`

# Multiple DVC params files

Alternative approach at branch [`multi`](https://github.com/iterative/multi-params-files/tree/multi).
