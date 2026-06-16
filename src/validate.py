def validate_data(df):
    df = df.dropna().dropDuplicates()
    return df
