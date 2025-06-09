import file_processing_EIT

eit = file_processing_EIT.EIT

women = eit[eit['Sex'] == 'жіноча']
men = eit[eit['Sex'] == 'чоловіча']

avg_women = women['Average Score'].mean()
avg_men = men['Average Score'].mean()

print(avg_women, '\n', avg_men)
