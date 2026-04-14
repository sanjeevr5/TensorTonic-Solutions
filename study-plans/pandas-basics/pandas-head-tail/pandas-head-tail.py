import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    data = pd.DataFrame(data)
    return {
        'head': data.head(n).to_dict(orient = "list"),
        'tail': data.tail(n).to_dict(orient = "list")
    }