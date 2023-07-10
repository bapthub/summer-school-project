import pandas as pd

pd.set_option('display.max_columns', 500)

def main():
    df_2021 = pd.read_csv('data/fr-esr-parcoursup_2021.csv',sep=";")
    # print(df_2021.head())
    print(df_2021.describe())
    print(df_2021.info())

if __name__ == '__main__':
    main()