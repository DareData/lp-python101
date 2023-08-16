import pandas as pd

def load_auto(path :str)-> pd.DataFrame:
    return pd.read_csv(path)

def clean_auto(auto : pd.DataFrame)-> pd.DataFrame:
    df = auto.copy()
    df[['brand', 'model']] = df['car name'].str.split(pat=' ', n=1, expand=True)

    return df

def create_report(auto: pd.DataFrame):
    print(f"Average miles per galon: {auto['mpg'].mean()}")
    print(f"Number missing values: {auto.isna().sum().sum()}")
    print(f"do we have repeated car names? {auto['car name'].duplicated().any()}")
    print(f"how many ford, dodges and vws?\n{auto['brand'].value_counts().loc[['ford', 'dodge', 'volkswagen']]}")

if __name__=='__main__':
    auto = load_auto("../data/auto-mpg.csv")
    cleaned_auto = clean_auto(auto)
    create_report(cleaned_auto)
