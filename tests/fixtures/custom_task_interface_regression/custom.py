"""
Copyright 2021 DataRobot, Inc. and its affiliates.
All rights reserved.
This is proprietary source code of DataRobot, Inc. and its affiliates.
Released under the terms of DataRobot Tool and Utility Agreement.
"""
# This custom estimator task implements a decision tree regressor

import pandas as pd
from sklearn.linear_model import Ridge
from datarobot_drum.custom_task_interfaces import RegressionEstimatorInterface


class CustomTask(RegressionEstimatorInterface):
    def fit(self, X, y, row_weights=None, **kwargs):
        """This hook defines how DataRobot will train this task.
        DataRobot will run this hook when the task is trained inside a blueprint.
        The input parameters are passed by DataRobot based on project and blueprint configuration.
        The output is the trained Custom Task instance, which allows a user to easily test, e.g.
        task.fit(...).save(...) or task.fit(...).predict_proba(...)

        Parameters
        -------
        X: pd.DataFrame
            Training data that DataRobot passes when this task is being trained.
        y: pd.Series
            Project's target column.
        row_weights: np.ndarray (optional, default = None)
            A list of weights. DataRobot passes it in case of smart downsampling or when weights column
            is specified in project settings.

        Returns
        -------
        CustomTask
            returns an object instance of class CustomTask that can be used in chained method calls
        """
        self.estimator = Ridge()
        self.estimator.fit(X, y)

        return self

    def predict(self, X, **kwargs):
        """This hook defines how DataRobot will use the trained estimator from fit() to predict on new data.
        DataRobot runs this hook when the task is used for scoring inside a blueprint.
        The input parameters are passed by DataRobot based on dataset and blueprint configuration.
        The output is the estimator's predictions on the new data in a tabular format (typically a pandas dataframe)

        Parameters
        -------
        X: pd.DataFrame
            Data that DataRobot passes for transformation.

        Returns
        -------
        pd.DataFrame
            Returns a dataframe with transformed data.
        """

        # note how the regression estimator only outputs one column, so no explicit column names are needed
        return pd.DataFrame(data=self.estimator.predict(X))
