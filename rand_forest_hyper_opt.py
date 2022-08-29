import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor
import sklearn.metrics as metrics
import sklearn.model_selection as ms

data = pd.read_csv(r'E:\personal\ucla_ext\Intro to Data Science\introdatasci_final_project\data\full.csv')
data = data[data['WATER_ELEVATION'] >= 0].reset_index(drop=True)
data['GW_MEAS_DATE'] = pd.to_numeric(pd.to_datetime(data['GW_MEAS_DATE']))

x_cols = ['GW_MEAS_DATE', 'PRCP', 'TMAX', 'TMIN', 'ELEVATION']
y_cols = ['DEPTH', 'WATER_ELEVATION']

x = data[x_cols]
y = data[y_cols[1]]
        
def rfr_optimize_all(x,y,range_list):
    '''
    This function is used to optimize the hyperparameters of the Random Forest Regressor.
    Input:
        x: the training data
        y: the target data
        range_list: a list of hyperparameters to be optimized
    '''
    rfr = RandomForestRegressor(
        criterion ='poisson',
        random_state=42,
        n_jobs=10,
        verbose=2
        )
    param_grid = {
        'n_estimators': range_list[0],
        'max_depth': range_list[1],
        }
    grid = ms.GridSearchCV(rfr, param_grid, cv=5, scoring='neg_mean_poisson_deviance')
    grid.fit(x, y)
    return grid.best_params_

n_estimators = list(range(85, 95, 1))
max_depth = list(range(55, 65, 1))
range_list = [n_estimators, max_depth]

rfr_optimize_all(x, y, range_list)