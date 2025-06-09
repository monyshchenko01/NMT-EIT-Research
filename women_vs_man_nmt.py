import pandas as pd
import file_processing_NMT

nmt = file_processing_NMT.NMT

only_scors = nmt.columns.difference(['Sex', 'Age', 'OUTID'])
nmt[only_scors] = nmt[only_scors].apply(pd.to_numeric, errors='coerce')

women = nmt[nmt['Sex'] == 'жінка']
men = nmt[nmt['Sex'] == 'чоловік']

avg_women = women[only_scors].mean()
avg_men = men[only_scors].mean()

print(avg_women, '/n', avg_men)
