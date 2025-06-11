import file_processing_EIT

eit = file_processing_EIT.EIT

women = eit[eit['Sex'] == 'жіноча']
men = eit[eit['Sex'] == 'чоловіча']

median_women = women['Average Score'].median()
median_men = men['Average Score'].median()

print(f"Average women score on EIT:\t{median_women.round()}\nAverage men score on EIT:\t{median_men.round()}\n\n")

median_women_by_subject = women[file_processing_EIT.grades_only].median()
median_men_by_subject = men[file_processing_EIT.grades_only].median()

print(f"Average women score on EIT by subject: \n{median_women_by_subject.round()}\n\nAverage men score on EIT by subject: \n{median_men_by_subject.round()}")
