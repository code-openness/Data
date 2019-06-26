def apply_cleanup(pik_df, functions):
    for function in functions:
        pik_df = function(pik_df)
    return pik_df
