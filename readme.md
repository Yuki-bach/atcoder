- contest: https://atcoder.jp/
- dashboard: https://kenkoooo.com/atcoder/#/table/yukibach

## Shell Scripts Usage

### Create Scripts
Create new problem directories with template files:

```bash
# Python
./scripts/create_py.sh <problem_name>

# Ruby
./scripts/create_rb.sh <problem_name>

# TypeScript
./scripts/create_ts.sh <problem_name>
```

Example: `./scripts/create_py.sh ABC367_A`

### Run Scripts
Execute solutions with input files:

```bash
# Python
./scripts/run_py.sh <task_name>

# Ruby
./scripts/run_rb.sh <task_name>

# TypeScript (includes ESLint check)
./scripts/run_ts.sh <task_name>
```

Example: `./scripts/run_py.sh ABC367_A`
