import sys
students_txt = open(sys.argv[1],'r',encoding='UTF-8')
wanted_students = sys.argv[2].split(',')
all_students = {student.split(':')[0]: student.replace(':',',').replace('\n','').split(',') for student in students_txt.readlines()}

for wanted_student in wanted_students:
    try:   
        WS_values = all_students[wanted_student] 
        print(f'Name: {WS_values[0]}, University: {WS_values[1]},{WS_values[2]}')
    except KeyError:
        print(f"No record of {wanted_student} was found!")