from typing import List

import pandas as pd
import numpy as np
import statsmodels.api as sm


def calc_protected_class_pvalue(data: List) -> float:
    df = pd.DataFrame(data=data)
    df = pd.get_dummies(df, columns=["protected_class"], drop_first=True)

    x = df[["protected_class_reference", "tenure", "performance"]]
    y = df["compensation"]
    x = sm.add_constant(x)

    # Fit the OLS model with the adjusted formula
    model = sm.OLS(y, x.astype(float))
    results = model.fit()

    pvalue = results.pvalues.get("protected_class_reference")
    return pvalue
