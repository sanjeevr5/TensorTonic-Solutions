import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    data = pd.DataFrame(data)
    return {
        "null_counts": data.isna().sum(axis=0).to_dict(),
        "cleaned_data": data.fillna(fill_value).to_dict(orient = 'list')
    }