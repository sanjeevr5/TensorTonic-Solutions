import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    data = pd.DataFrame(data)
    before = {c: str(d) for c, d in data.dtypes.to_dict().items()}
    data[column] = data[column].astype(target_type)
    return [
        before,
        {c: str(d) for c, d in data.dtypes.to_dict().items()}
    ]