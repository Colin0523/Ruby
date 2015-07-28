grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def print_grades(grades):
    for grade in grades:
        print grade
print_grades(grades)


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
o = [6,5]
def grades_sum(scores):
    total = sum(scores)
    return total
print grades_sum(grades)


def grades_average(grades):
    total = grades_sum(grades)
    aver = total/float(len(grades))
    return aver
print grades_average(grades)



def grades_variance(scores):
    average =  grades_average(scores)
    print 'average =  ',average
    variance = 0 
    for score in scores:
        variance += float((average - score) ** 2)
    total_variance = variance / float(len(scores))
    return total_variance 
    
print grades_variance(o)


def grades_std_deviation(variance):
    return variance ** 0.5
variance = grades_variance(grades)
print grades_std_deviation(variance)