import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    data = pd.DataFrame(data)
    return [
        data.iat[row, col],
        data.iloc[row].tolist(),
        data.iloc[:, col].tolist()
    ]