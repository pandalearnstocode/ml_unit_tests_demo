import numpy as np
from sklearn.model_selection import train_test_split

def generate_red_data(n_rows, n_cols, sim_min, sim_max, seed_value):
    np.random.seed(seed_value)
    X = np.random.uniform(sim_min, sim_max, size = (n_rows, n_cols))
    y = np.random.rand(n_rows)
    return X, y

def generate_green_data(n_rows, n_cols, sim_min, sim_max, seed_value):
    np.random.seed(seed_value)
    X = np.random.uniform(sim_min, sim_max, size = (n_rows, n_cols))
    y = np.random.uniform(n_rows) + X.sum(1)
    return X, y

def train_test_split_data(X, y, train_test_split_ratio, seed_value):
    np.random.seed(seed_value)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=train_test_split_ratio, random_state=seed_value)
    return X_train, X_test, y_train, y_test