#Samed Ökçeci 2210356015

input_list = [int(number) for number in input('Please enter numbers. Example syntax: 1,2,3,4,5 ').split(',')]


def minimum_number(list):
    if len(list)==1:
        return (list[0])
    if list[0] <= list[1]:
        list.pop(1)
        return minimum_number(list)
    else:
        list.pop(0)
        return minimum_number(list)

def maximum_number(list):
    if len(list)==1:
        return (list[0])
    if list[0] <= list[1]:
        list.pop(0)
        return maximum_number(list)
    else:
        list.pop(1)
        return maximum_number(list)

 
def average_of_list(list):
    def sum_of_list(list):
        if len(list)!=1:
            return int(list[0]) + sum_of_list(list[1:])
        else:
            return int(list[0])  
    return sum_of_list(list)/len(list)

print('Minimum number:', minimum_number(input_list[:]))
print('Maximum number:', maximum_number(input_list[:]))
print('Average of list:', average_of_list(input_list[:]))

#Samed Ökçeci 2210356015
