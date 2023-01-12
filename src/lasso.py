from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# Define the function 'lasso_regression'

def lasso_regression(X_train, X_test, y_train, y_test, params, cv):
    """Returns the best alpha value and the corresponding R squared value"""
    steps = [('scaler', StandardScaler()),('lasso', Lasso())]
    pipeline = Pipeline(steps)
    parameters = params
    gm_cv = GridSearchCV(pipeline, parameters, cv=cv, n_jobs= -1)
    gm_cv.fit(X_train, y_train)
    r2 = gm_cv.score(X_test, y_test)
    print("Tuned Lasso Alpha: {}".format(gm_cv.best_params_))
    print("Tuned Lasso R squared: {}".format(r2))
    return gm_cv.best_params_, r2
