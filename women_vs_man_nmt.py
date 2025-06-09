import file_processing_NMT

nmt = file_processing_NMT.NMT

women = nmt[nmt['Sex'] == 'жіноча']
men = nmt[nmt['Sex'] == 'чоловіча']

avg_women = women['Average Score'].mean()
avg_men = men['Average Score'].mean()

print(f"Average woman score on NMT:\t{avg_women.round()}\nAverage man score on NMT:\t{avg_men.round()}\n\n")

avg_women_by_subject = women[file_processing_NMT.grades_only].mean()
avg_men_by_subject = men[file_processing_NMT.grades_only].mean()

print(f"Average woman score on NMT by subject: \n{avg_women_by_subject.round()}\n\nAverage man score on NMT by subject: \n{avg_men_by_subject.round()}")
