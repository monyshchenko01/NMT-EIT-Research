import pandas as pd
import file_processing_EIT

eit = file_processing_EIT.EIT

only_scors = eit.columns.difference(['Sex', 'Age', 'OUTID'])
eit[only_scors] = eit[only_scors].apply(pd.to_numeric, errors='coerce')

women = eit[eit['Sex'] == 'жінка']
men = eit[eit['Sex'] == 'чоловік']

avg_women = women[only_scors].mean()
avg_men = men[only_scors].mean()

# print(avg_women, '\n', avg_men)
