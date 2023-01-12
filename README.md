# __Writing unit tests for ML workflows__

```bash
conda create -n unit_tests_ml_workflows python=3.8 -y
conda activate unit_tests_ml_workflows
pip install -r requirements.txt
```

```bash
pytest .
pytest --cov-report term --cov=src tests/
pytest --cov-report term --cov-report xml:coverage.xml --cov=src tests/
pytest --cov-report term --cov-report html:coverage --cov=src tests/
conda deactivate
```