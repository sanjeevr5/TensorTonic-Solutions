import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    data = pd.DataFrame(data)
    count = int((data[column] == old_val).sum())
    data.replace({column: {old_val : new_val}}, inplace = True)
    return {
        'data': data.to_dict(orient = 'list'),
        'count': count
    }