import json
import pandas as pd

data = {
    'date': [
        '2025-06-30', '2025-06-27', '2025-06-20', '2025-06-26', '2025-06-25',
        '2025-06-24', '2025-06-23', '2025-06-22', '2025-06-21', '2025-06-19',
        '2025-06-18', '2025-06-17', '2025-06-16', '2025-06-15', '2025-06-14',
        '2025-06-13', '2025-06-12', '2025-06-11'
    ],
    'answered_questions': [
        10, 8, 18, 15, 12,
        20, 9, 14, 16, 11,
        13, 17, 10, 9, 8,
        12, 15, 10
    ],
    'correct_answers': [
        8, 7, 14, 13, 10,
        17, 7, 12, 13, 9,
        11, 14, 7, 8, 6,
        9, 11, 8
    ],
    'wrong_answers': [
        2, 1, 4, 2, 2,
        3, 2, 2, 3, 2,
        2, 3, 3, 1, 2,
        3, 4, 2
    ],
    'study_time': [
        3, 3, 20, 2, 2,
        4, 2, 3, 3, 2,
        2, 3, 2, 2, 1,
        2, 3, 2
    ],
    'subject': [
        'history', 'biology', 'physics', 'math', 'geography',
        'math', 'english', 'chemistry', 'history', 'biology',
        'physics', 'math', 'english', 'history', 'chemistry',
        'biology', 'physics', 'math'
    ]
}

"""
Some important data to show:

- Percentage of correct answers
- Average daily study time (in hours)
- Top 3 most studied subjects based on total study hours
"""

df = pd.DataFrame(data)

correct_answers = df["correct_answers"].sum()
wrong_answers = df["wrong_answers"].sum()
total_exercises = correct_answers + wrong_answers

percentage_correct_answers = round(((correct_answers / total_exercises) * 100), 2)

print(f'The percentage of correct answers is {percentage_correct_answers:.2f}%')

days_studied = len(df["date"])
total_study_hours = df["study_time"].sum()
average_daily_study = total_study_hours / days_studied
average_daily_study = round(average_daily_study, 1)

print(percentage_correct_answers)

percentage_wrong_answers = round(100 - round(percentage_correct_answers, 2), 2)
print(percentage_wrong_answers)

print(f'The average of studied hours by day was {average_daily_study:.2f} hours')

subjects = df.groupby("subject").study_time.sum().sort_values(ascending=False)
print(subjects)

subjects_most_studied = []
study_time_by_subject = []

for _ in range(3):
    subjects_most_studied.append(subjects.index[_])
    study_time_by_subject.append(int(subjects.iloc[_]))

print(subjects_most_studied)
print(study_time_by_subject)

summary_data = {
    "percentage_correct_answers": percentage_correct_answers,
    "percentage_wrong_answers": percentage_wrong_answers,
    "average_daily_study": round(average_daily_study, 2),
    "most_studied_subjects": subjects_most_studied,
    "study_time_by_subject": study_time_by_subject
}

with open("dashboard_summary.json", "w") as json_file:
    json.dump(summary_data, json_file)


