# __Writing unit tests for ML workflows__


## __Creating conda env for local execution__

```bash
conda create -n unit_tests_ml_workflows python=3.8 -y
conda activate unit_tests_ml_workflows
pip install -r requirements.txt
```

## __Running unit tests and generating CLI, XML and HTML reports__

```bash
pytest .
pytest --cov-report term --cov=src tests/
pytest --cov-report term --cov-report xml:coverage.xml --cov=src tests/
pytest --cov-report term --cov-report html:coverage --cov=src tests/
conda deactivate
```

## __GitHub actions to trigger unit tests__

```bash
name: Run unit tests for ML workflows

on: [push]

jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version:
          - "3.8"
          - "3.9"
          - "3.10"
          - "3.11"
    name: Check Python ${{ matrix.python-version }}
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: Setup Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install package
        run: python -m pip install -r requirements.txt
      - name: Run unit tests and generate coverage report
        run: python -m pytest --cov-report term --cov-report xml:coverage.xml --cov=src tests/
```


