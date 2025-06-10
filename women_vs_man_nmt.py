import file_processing_NMT

nmt = file_processing_NMT.NMT

women = nmt[nmt['Sex'] == 'жіноча']
men = nmt[nmt['Sex'] == 'чоловіча']

median_women = women['Average Score'].median()
median_men = men['Average Score'].median()

print(f"Average woman score on NMT:\t{median_women.round()}\nAverage man score on NMT:\t{median_men.round()}\n\n")

median_women_by_subject = women[file_processing_NMT.grades_only].median()
median_men_by_subject = men[file_processing_NMT.grades_only].median()

print(f"Average woman score on NMT by subject: \n{median_women_by_subject.round()}\n\nAverage man score on NMT by subject: \n{median_men_by_subject.round()}")
