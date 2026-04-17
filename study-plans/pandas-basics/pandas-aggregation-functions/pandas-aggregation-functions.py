import pandas as pd

def multi_agg(data, group_col, value_col, funcs):
    """
    Returns: dict mapping function name to {group: value} dict
    """
    data = pd.DataFrame(data)
    return data.groupby(group_col)[value_col].agg(funcs).to_dict()