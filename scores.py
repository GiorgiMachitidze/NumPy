import numpy as np
import pandas as pd

firstnames = ['Venus', 'Tina', 'Thea', 'Soso', 'Miranda', 'Zhenia', 'Tatiana', 'Edward', 'Clara', 'Simon', 'Anzor',
              'Sofia', ' Soso', 'Nelly', 'Bondo', 'Eduard', 'Sonia', 'Archil', 'Mariam', 'Sofia', 'Emma', 'Isolde',
              'Omar', 'Tatiana', 'Victor', 'Karine', 'Cuckoo', 'Kakha', 'Rosa', 'Rusudan', 'Simon', 'Nelly', 'Badri',
              'Madonna', 'Irine', 'Mindia', 'Natia', ' Gulnara', 'Kakha', 'Elza', 'Roin', 'Naira', 'Liana', 'Ninel',
              'Makvala', 'Rezo', 'Zhuzhuna', 'Zina', 'Gocha', 'Murman']
lastnames = ['Kutateladze', 'Megrelishvili', 'Salukvadze', 'Kharaishvili', 'Shelia', 'Kevlishvili', 'Buchukuri',
             'Tkebuchava', 'Mikaberidze', 'Urushadze', 'Dzidziguri', 'Goguadze', ' Antadze', 'Valyeva', 'Rogava',
             'Nakashidze', 'Ghurtskaya', 'Gvazawa', 'Gvasalia', 'Zarandia', 'Skhirtladze', 'Beradze', 'Khvichia',
             'Basilashvili', 'Kakabadze', 'Merebashvili', 'Nozadze', 'Kharabadze', 'Musaeva', 'Mamulashvili',
             'Elizbarashvili', 'Mamulashvili', 'Jojua', 'Gulua', 'Khalvashi', 'Kharatishvili', 'Dumbadze',
             ' Berianidze', 'Jokhadze', 'Samkharadze', 'Liparteliani', 'Iobidze', 'Gabaidze', 'Kharabadze',
             'Inasaridze', 'Beradze', 'Shengelia', 'Kobalia', 'Mikava', 'Revazishvili']

subjects = ["students", "Georgian", "Mathematics", "English", "Physics", "Biology"]
numstudents = 100

studentnames = []

scores = np.random.randint(1, 101, size=(numstudents, len(subjects)))  # generate random scores from 1 to 100
for names in range(numstudents):  # use for loop to generate random names and surnames from the given lists
    fnames = np.random.choice(firstnames)
    lnames = np.random.choice(lastnames)
    studentnames.append(f"{fnames} {lnames}")

student_table = np.column_stack((studentnames, scores[:, 0], scores[:, 1], scores[:, 2], scores[:, 3], scores[:, 4]))
student_table = np.vstack((subjects, student_table))  # create tables of students using numpy arrays
st = pd.DataFrame(student_table)  # use panda to get better looking table


# print(st)
def calculate_students_avg_scores(studenttable):
    avgscores = np.mean(studenttable[1:, 1:].astype(float), axis=1, )
    avgscores = np.append("average scores", avgscores)
    studenttable = np.column_stack((studenttable, avgscores))
    studtable = pd.DataFrame(studenttable)
    return studtable


def extreme_math_scores(studenttable):
    index1 = np.argmax(studenttable[1:, 2].astype(float))
    index2 = np.argmax(studenttable[1:, 2].astype(float))
    score1 = np.max(studenttable[1:, 2].astype(float))
    score2 = np.min(studenttable[1:, 2].astype(float))
    return (f" Student with the greates score in math is {studentnames[index1]} with score {score1} and the student "
            f"with the worst score {score2} is {studentnames[index2]}")


def average_scores_in_english():
    avgscore = np.mean(student_table[1:, 3].astype(float))
    greaterscore = student_table[1:, 0][student_table[1:, 3].astype(float) > avgscore]
    return f" Students with greater scores than average in english are: {greaterscore}"


# print(extreme_math_scores(student_table))  # use this line to acess students who have the greatest and the worst
# scores in math
# print(calculate_students_avg_scores(student_table))  # use this line to understand average scores of
# students
# print(average_scores_in_english())               # use this line to get students names who have
# higher scores than average in english
