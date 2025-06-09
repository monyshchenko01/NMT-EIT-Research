import file_processing_EIT

eit = file_processing_EIT.EIT

women = eit[eit['Sex'] == 'жіноча']
men = eit[eit['Sex'] == 'чоловіча']
women = women[women['Average Score'] != 0]
men = men[men['Average Score'] != 0]

avg_women = women['Average Score'].mean()
avg_men = men['Average Score'].mean()

print(f"Average woman score on EIT:\t{avg_women.round()}\nAverage man score on EIT:\t{avg_men.round()}\n\n")

avg_women_by_subject = women[file_processing_EIT.grades_only].mean()
avg_men_by_subject = men[file_processing_EIT.grades_only].mean()

print(f"Average woman score on EIT by subject: \n{avg_women_by_subject.round()}\n\nAverage man score on EIT by subject: \n{avg_men_by_subject.round()}")
