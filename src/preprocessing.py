import pandas as pd

def dataset_info(df):
    print("\n=======First 5 row======")
    print(df.head())

    print("\n=======Last 5 row======")
    print(df.tail())

    print("\n=======Dataset info======")
    print(df.info())

    print("\n=======Dataset Shape======")
    print(df.shape)

    print("\n=======Columns======")
    print(df.columns)

    print("\n=======Data Types======")
    print(df.dtypes)

    print("\n=======Statistical Summary======")
    print(df.describe())

def check_missing_values(df):
    print("\n=======Check Missing Values======")
    print(df.isnull().sum())

def check_duplicates(df):
    print("\n=======Duplicate Records======")
    print(df.duplicated().sum())

def remove_duplicates(df):
    df=df.drop_duplicates()
    return df

def remove_missing(df):
    df=df.dropna()
    return df

def save_clean_data(df):
    df.to_csv("data/online_retail_cleaned.csv",index=False)
    print("\nCleaned dataset saved successfully")

def overall_insights(df):
    print("\n=======Overall Count======")
    print(f"Total Customers: {df['CustomerID'].nunique()}")
    print(f"Total Products: {df['StockCode'].nunique()}")
    print(f"Total Country: {df['Country'].nunique()}")
    print(f"Total Invoices: {df['InvoiceNo'].nunique()}")