import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    data = pd.DataFrame(data)
    before = data.set_index(index_col)
    after = before.reset_index()
    return [
        list(before.columns),
        list(after.columns)
    ]