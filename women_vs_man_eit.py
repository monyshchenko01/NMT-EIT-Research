import file_processing_NMT
import file_processing_EIT

eit = file_processing_EIT.EIT
nmt = file_processing_NMT.NMT

only_scors = eit.columns.difference(['Sex', 'Age', 'OUTID'])

women = eit[eit['Sex'] == 'жінка']
men = eit[eit['Sex'] == 'чоловік']

acg_women = women[only_scors].mean()
acg_men = men[only_scors].mean()

print(acg_women, acg_men)