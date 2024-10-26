from typing import List

import pandas as pd
import numpy as np
import statsmodels.api as sm


def calc_protected_class_pvalue(data: List) -> float:
    df = pd.DataFrame(data=data)

    # Convert protected_class to dummy variables (for categorical data)
    df = pd.get_dummies(df, columns=["protected_class"], drop_first=True)

    # Define the independent variables (X) and dependent variable (y)
    x = df[["protected_class_reference", "tenure", "performance"]]
    y = df["compensation"]

    # Add a constant term to the model (for the intercept)s
    x = sm.add_constant(x)

    # Fit the OLS model
    model = sm.OLS(y, x.astype(float))
    results = model.fit()

    # Get the p-value of the protected_class variable (comparison group)
    pvalue = results.pvalues.get("protected_class_reference")
    return pvalue
