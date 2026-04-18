import pandas as pd

def melt_dataframe(data, id_vars, value_vars):
    """
    Returns: dict with keys from id_vars plus 'variable' and 'value'
    """
    data = pd.DataFrame(data)
    return pd.melt(data, id_vars = id_vars, value_vars = value_vars).to_dict(orient = 'list')