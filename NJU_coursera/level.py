__author__ = 'nylon7'

#輸入成績分級，100～90=A 89~70=B 69~60=C 60~0=D others Invalid score

flag = 'y'
while (flag == 'y'):
    print "key in your grades"
    grades = int(raw_input())
    print grades
    if (grades <= 100 and grades > 90):
        print "A class"
    elif (grades <90 and grades >=70):
        print "B class"
    elif (grades <70 and grades >=60):
        print "C class"
    elif (grades <60 and grades >=0):
        print "D class"
    else:
        print "Invalid score"
        continue
    print "try again? y or n"
    flag = raw_input()
    print flag
else:
    print"program finish"
