import pandas as pd

def cross_tab(data, row_col, col_col):
    """
    Returns: nested dict {col_value: {row_value: frequency}}
    """
    data = pd.DataFrame(data)
    return pd.crosstab(data[row_col], data[col_col]).to_dict()