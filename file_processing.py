import pandas as pd

df_2019 = pd.read_csv('data/2019.csv', encoding='cp1251', low_memory=False, sep=';')
print(df_2019.columns.tolist())
for i in range(5):
    print(df_2019.head(i+1).values, '\n')
print('\n')

df_2020 = pd.read_csv('data/2020.csv', encoding='1251', low_memory=False, sep=';')
print(df_2020.columns.tolist(), '\n')
for i in range(5):
    print(df_2020.head(i+1).values, '\n')
print('\n')

df_2021 = pd.read_csv('data/2021.csv', encoding='', low_memory=False, sep=';')
print(df_2021.columns.tolist(), '\n')
for i in range(5):
    print(df_2021.head(i+1).values, '\n')
print('\n')

df_2022 = pd.read_csv('data/2022.csv', encoding='', sep=';')
print(df_2022.columns.tolist(), '\n')
for i in range(5):
    print(df_2022.head(i+1).values, '\n')
print('\n')

df_2023 = pd.read_csv('data/2023.csv', encoding='', sep=';')
print(df_2023.columns.tolist(), '\n')
for i in range(5):
    print(df_2023.head(i+1).values, '\n')
print('\n')

df_2024 = pd.read_csv('data/2024.csv', encoding='', sep=';')
print(df_2023.columns.tolist(), '\n')
for i in range(5):
    print(df_2024.head(i+1).values, '\n')
print('\n')
