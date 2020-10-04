'''def foo(a, b, *some_args):
    print('a is', a)
    print('b is ', b)
    print('som_args is ', some_args)

foo(10, 12, 1, 2, 3, 4, 5)
def goo(**kwargs):
    print(kwargs)
    

goo(name="suresh", age=22)'''



def mean_cal (**kwargs):
    subject_list = []
    sum_score=0
    for subject, score in kwargs.items():
        subject_list.append(subject)
        sum_score += score
    student_mean = sum_score/len(kwargs)
    
    return student_mean, subject_list
            

mean = mean_cal(math=100, english=90, history=85)
print(mean)

print(mean[0])

tuple = ("vfed", "Dscfv")

print(tuple)

listt = list(tuple)

print(listt)