import pandas as pd


def select_col(df):
    ball100 = []
    for col in df.columns:
        if 'Ball100' in col:
            ball100.append(col)
        if col == 'outid':
            df = df.rename(columns={'outid': 'OUTID'})
        if col == 'SEXTYPENAME':
            df = df.rename(columns={'SEXTYPENAME': 'Sex'})
        if col == 'SexTypeName':
            df = df.rename(columns={'SexTypeName': 'Sex'})

    df = df[['OUTID', 'Sex', 'Age'] + ball100]

    df = df.rename(columns={'UkrBlockBall100': 'Ukrainian'})
    df = df.rename(columns={'HistBlockBall100': 'History'})
    df = df.rename(columns={'MathBlockBall100': 'Math'})
    df = df.rename(columns={'PhysBlockBall100': 'Physic'})
    df = df.rename(columns={'ChemBlockBall100': 'Chemistry'})
    df = df.rename(columns={'BioBlockBall100': 'Biology'})
    df = df.rename(columns={'GeoBlockBall100': 'Geography'})
    df = df.rename(columns={'EngBlockBall100': 'English'})
    df = df.rename(columns={'FraBlockBall100': 'French'})
    df = df.rename(columns={'DeuBlockBall100': 'German'})
    df = df.rename(columns={'SpaBlockBall100': 'Spanish'})
    df = df.rename(columns={'UkrLitBlockBall100': 'Ukrainian Literature'})

    return df



df_2022 = pd.read_csv('data/2022.csv', encoding='', sep=';')
df_2022['Age'] = 2022 - df_2022['Birth']
df_2022 = select_col(df_2022)

df_2023 = pd.read_csv('data/2023.csv', encoding='', sep=';')
df_2023['Age'] = 2023 - df_2023['Birth']
df_2023 = select_col(df_2023)

df_2024 = pd.read_csv('data/2024.csv', encoding='', sep=';')
df_2024['Age'] = 2024 - df_2024['Birth']
df_2024 = select_col(df_2024)

NMT = pd.concat([df_2022, df_2023, df_2024], ignore_index=True)
