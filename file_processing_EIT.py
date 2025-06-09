import pandas as pd


def select_col(df):
    ball100 = []
    for col in df.columns:
        if 'Ball100' in col:
            ball100.append(col)
        if col == 'SEXTYPENAME':
            df = df.rename(columns={'SEXTYPENAME': 'Sex'})
        if col == 'SexTypeName':
            df = df.rename(columns={'SexTypeName': 'Sex'})

    df = df[['OUTID', 'Sex', 'Age'] + ball100]

    df = df.rename(columns={'UkrBall100': 'Ukrainian'})
    df = df.rename(columns={'histBall100': 'History'})
    df = df.rename(columns={'mathBall100': 'Math'})
    df = df.rename(columns={'physBall100': 'Physic'})
    df = df.rename(columns={'chemBall100': 'Chemistry'})
    df = df.rename(columns={'bioBall100': 'Biology'})
    df = df.rename(columns={'geoBall100': 'Geography'})
    df = df.rename(columns={'engBall100': 'English'})
    df = df.rename(columns={'fraBall100': 'French'})
    df = df.rename(columns={'deuBall100': 'German'})
    df = df.rename(columns={'spaBall100': 'Spanish'})

    df = df.rename(columns={'UMLBall100': 'Ukrainian Literature'})
    df = df.rename(columns={'HistBall100': 'Applied History'})
    df = df.rename(columns={'MathBall100': 'Applied Math'})
    df = df.rename(columns={'PhysBall100': 'Applied Physic'})
    df = df.rename(columns={'ChemBall100': 'Applied Chemistry'})
    df = df.rename(columns={'BioBall100': 'Applied Biology'})
    df = df.rename(columns={'GeoBall100': 'Applied Geography'})
    df = df.rename(columns={'EngBall100': 'Applied English'})
    df = df.rename(columns={'FraBall100': 'Applied French'})
    df = df.rename(columns={'DeuBall100': 'Applied German'})
    df = df.rename(columns={'SpaBall100': 'Applied Spanish'})

    return df


df_2019 = pd.read_csv('data/2019.csv', encoding='cp1251', low_memory=False, sep=';')
df_2019['Age'] = 2019 - df_2019['Birth']
df_2019 = select_col(df_2019)

df_2020 = pd.read_csv('data/2020.csv', encoding='1251', low_memory=False, sep=';')
df_2020['Age'] = 2020 - df_2020['Birth']
df_2020 = select_col(df_2020)

df_2021 = pd.read_csv('data/2021.csv', encoding='', low_memory=False, sep=';')
df_2021['Age'] = 2021 - df_2021['Birth']
df_2021 = select_col(df_2021)

EIT = pd.concat([df_2019, df_2020, df_2021], ignore_index=True)

grades_only = ['Ukrainian', 'History', 'Math', 'Physic',
               'Chemistry', 'Biology', 'Geography', 'English', 'French', 'German',
               'Spanish', 'Ukrainian Literature', 'Applied History', 'Applied Math',
               'Applied Physic', 'Applied Chemistry', 'Applied Biology',
               'Applied Geography', 'Applied English', 'Applied French',
               'Applied German', 'Applied Spanish']

for col in grades_only:
    EIT[col] = EIT[col].str.replace(',', '.', regex=False).astype(float)

EIT['Average Score'] = EIT[grades_only].mean(axis=1, skipna=True)
