import pandas as pd


def select_col(df):
    ball100 = []
    for col in df.columns:
        if 'Ball100' in col:
            ball100.append(col)
    df = df[['OUTID', 'Sex', 'Age'] + ball100]
    return df

# 2019 EIT
df_2019 = pd.read_csv('data/2019.csv', encoding='cp1251', low_memory=False, sep=';')
df_2019['Age'] = 2019 - df_2019['Birth']
df_2019 = df_2019.rename(columns={'SEXTYPENAME': 'Sex'})
df_2019 = select_col(df_2019)
# 2020
df_2020 = pd.read_csv('data/2020.csv', encoding='1251', low_memory=False, sep=';')
df_2020['Age'] = 2020 - df_2020['Birth']
df_2020 = df_2020.rename(columns={'SEXTYPENAME': 'Sex'})
df_2020 = select_col(df_2020)
#2021
df_2021 = pd.read_csv('data/2021.csv', encoding='', low_memory=False, sep=';')
df_2021['Age'] = 2021 - df_2021['Birth']
df_2021 = df_2021.rename(columns={'SexTypeName': 'Sex'})
df_2021 = select_col(df_2021)

# 2022 NMT
df_2022 = pd.read_csv('data/2022.csv', encoding='', sep=';')
df_2022['Age'] = 2022 - df_2022['Birth']
df_2022 = df_2022.rename(columns={'SexTypeName': 'Sex'})
df_2022 = select_col(df_2022)
# 2023
df_2023 = pd.read_csv('data/2023.csv', encoding='', sep=';')
df_2023['Age'] = 2023 - df_2023['Birth']
df_2023 = df_2023.rename(columns={'SexTypeName': 'Sex'})
df_2023 = df_2023.rename(columns={'outid': 'OUTID'})
df_2023 = select_col(df_2023)
# 2024
df_2024 = pd.read_csv('data/2024.csv', encoding='', sep=';')
df_2024['Age'] = 2024 - df_2024['Birth']
df_2024 = df_2024.rename(columns={'SexTypeName': 'Sex'})
df_2024 = df_2024.rename(columns={'outid': 'OUTID'})
df_2024 = select_col(df_2024)

EIT = pd.concat([df_2019, df_2020, df_2021], ignore_index=True)
NMT = pd.concat([df_2022, df_2023, df_2024], ignore_index=True)

print(EIT)
print(NMT)