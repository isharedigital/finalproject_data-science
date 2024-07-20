import pandas as pd

# Xử lý khoảng trắng

def remove_whitespace(df):
    """
    Loại bỏ khoảng cách ở đầu và cuối của tất cả các giá trị trong các cột loại object của DataFrame.
    """
    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].apply(lambda x: x.str.strip())
    return df