import pytest
from src.lasso import lasso_regression
from src.utils import generate_red_data, train_test_split_data
import numpy as np

def test_red_lasso_regression():
    X, y = generate_red_data(n_rows=100, n_cols=10, sim_min=100, sim_max=1000, seed_value=42)
    X_train, X_test, y_train, y_test = train_test_split_data(X, y, train_test_split_ratio=0.4, seed_value=42)
    best_params, r2 = lasso_regression(X_train, X_test, y_train, y_test, params={'lasso__alpha':np.logspace(-4, 0, 50)}, cv=5)
    assert not (r2 > 0.5)