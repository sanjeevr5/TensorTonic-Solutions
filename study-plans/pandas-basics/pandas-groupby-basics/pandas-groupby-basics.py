import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    data = pd.DataFrame(data)
    return {
        'sum': data.groupby(group_col, dropna = False)[value_col].sum().to_dict(),
        'mean': data.groupby(group_col, dropna = False)[value_col].mean().to_dict(),
        'count': data.groupby(group_col, dropna = False)[value_col].count().to_dict()
    }