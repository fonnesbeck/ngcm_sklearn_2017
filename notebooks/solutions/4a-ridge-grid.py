import numpy as np

from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV, train_test_split


boston = load_boston()
X, y = boston.data, boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=.2,
                                                    random_state=123)

param_grid = {
    'ridge__alpha': np.logspace(-1, 3, 5),
    'polynomialfeatures__degree': [1, 2, 3]
}

pipeline = make_pipeline(
    StandardScaler(),
    PolynomialFeatures(),
    Ridge()
)

estimator = GridSearchCV(pipeline, param_grid=param_grid, cv=5)
estimator.fit(X_train, y_train)

print(estimator.score(X_test, y_test))
print(estimator.best_score_)
print(estimator.best_params_)
