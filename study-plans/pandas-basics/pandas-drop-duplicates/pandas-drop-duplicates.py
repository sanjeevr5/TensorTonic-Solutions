import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    data = pd.DataFrame(data)
    dedup = data.drop_duplicates().reset_index(drop = True)
    return [
        len(data),
        len(dedup),
            dedup.to_dict(orient = 'list')
    ]