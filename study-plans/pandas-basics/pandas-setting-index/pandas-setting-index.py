import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    data = pd.DataFrame(data)
    data.set_index(index_col, inplace = True)
    return {
        'index_values': data.index.values.tolist(),
        'columns': list(data.columns),
        'data': data.to_dict(orient = 'list')
    }