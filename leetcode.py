# COMBINE TWO TABLES

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # 1. Left join 'person' and 'address' DataFrames on 'personId'
    merged_df = pd.merge(person, address, on='personId', how='left')
    
    # 2. Select only the requested columns
    result_df = merged_df[['firstName', 'lastName', 'city', 'state']]
    
    return result_df