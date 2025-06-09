import file_processing_NMT

nmt = file_processing_NMT.NMT

women = nmt[nmt['Sex'] == 'жіноча']
men = nmt[nmt['Sex'] == 'чоловіча']

avg_women = women['Average Score'].mean()
avg_men = men['Average Score'].mean()

print(avg_women, '\n', avg_men)
