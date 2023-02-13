#Samed Ökçeci 2210356015
import sys

def open_file(fileName,method):
    return open(fileName,method,encoding='UTF-8')

def rounder(number):
    number = str(number)
    if ',' in number:
        number = number.replace(',','.')
    
    number1, number2 = number.split('.')

    if int(number2[0])>=5:
        return int(number1)+1
    else:
        return int(number1)


try:
    input_file_name = None
    comparison_file_name = None
    input_file_name = sys.argv[1]
    comparison_file_name = sys.argv[2]

except IndexError:
    print('IndexError: number of input files less than expected.\n')
    print('~ Game Over ~')
    exit()


try:
    if input_file_name!=None:
        input_file = open_file(input_file_name,'r')
    
except IOError:
    print(f'IOError:cannot open {input_file_name}\n')
    print('~ Game Over ~')
    exit()


try:
    if comparison_file_name!=None:
        comparison_file = open_file(comparison_file_name,'r')

except IOError:
    print(f'IOError:cannot open {comparison_file_name}\n')
    print("̃  Game Over ̃ ̃")    
    exit()


count = -1
comparison_file_list = comparison_file.readlines()


for input_line in input_file:
    count+=1


    try:
        try:
            print('------------')
            div, nondiv, from_number, to_number = rounder(float(input_line.split(' ')[0])), rounder(float(input_line.split(' ')[1])), rounder(float(input_line.split(' ')[2])), rounder(float(input_line.split(' ')[3]))
            
        except IndexError:
            print("IndexError: number of operands less than expected.")
            print(f'Given input: {input_line}',end='')
            continue

        except ValueError:
            print("ValueError: only numeric input is accepted.")
            print(f'Given input: {input_line}',end='')
            continue


        try:
            str_div_numbers = []
            str_nondiv_numbers = []
            for number in range(int(from_number),int(to_number)+1):
                division = number % int(div)
                if division==0:
                    str_div_numbers.append(str(number))

                division = number % int(nondiv)
                if division==0:
                    str_nondiv_numbers.append(str(number))

        except ZeroDivisionError:
            print("ZeroDivisionError: You can't divide by 0.")
            print(f'Given input: {input_line}',end='')
            continue
            
        except ValueError:
            print("ValueError: only numeric input is accepted.")
            print(f'Given input: {input_line}',end='')
            continue

        my_result= set(str_div_numbers) - set(str_nondiv_numbers)
        comparison_result = comparison_file_list[count].replace('\n','').split(' ')
        
        print('My results:                  ',' '.join(sorted(list(my_result))))
        print('Results to compare:          ',' '.join(sorted(comparison_result)))   
        
        assert my_result == set(comparison_result)
        
        print('Goool!!!')

    except ValueError:
        print("ValueError: only numeric input is accepted.")
        print(f'Given input: {input_line}')
        continue
    
    except IndexError:
        print("IndexError: number of operands less than expected.")
        print(f'Given input: {input_line}')
        
        continue
    
    except ZeroDivisionError:
        print("ZeroDivisionError: You can't divide by 0.")
        print(f'Given input: {input_line}')
        continue
    
    except AssertionError:
        print("Assertion Error: results don't match.")
        continue
    
    except:
        print("kaBOOM: run for your life!")
        continue
print()
print("̃  Game Over ̃ ̃")


#Samed Ökçeci 2210356015
