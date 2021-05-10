import numpy as np

def solution(answers):
    correct1 = corect2 = corect3 = 0
    answer=[]

    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    lens1 = len(answers)//5
    lens2 = len(answers)//8
    lens3 = len(answers)//10

    s1_answers = answers[:]+(5-len(answers) % 5)*[0]
    s2_answers = answers[:]+(8-len(answers) % 8)*[0]
    s3_answers = answers[:]+(10-len(answers) % 10)*[0]

    student1 = student1*(lens1+1)
    student2 = student2*(lens2+1)
    student3 = student3*(lens3+1)

    s1_true = list(np.equal(student1,s1_answers))
    s2_true = list(np.equal(student2,s2_answers))
    s3_true = list(np.equal(student3,s3_answers))

    s1_true = s1_true.count(True)
    s2_true = s2_true.count(True)
    s3_true = s3_true.count(True)

    a = [s1_true,s2_true,s3_true]
    max_val = max(a)

    for i in range(0,3,1):
        if a[i] == max_val:
            answer.append(i+1)

    return answer