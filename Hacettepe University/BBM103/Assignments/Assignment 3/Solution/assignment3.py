#Samed Ökçeci 2210356015
import string
import sys

def open_input_file(input_file_name):
    return open(str(input_file_name),'r',encoding='UTF-8').readlines() #opens input file with UTF-8 and readlines method.


def open_output_file(output_file_name):
    return open(str(output_file_name),'w') #returns output file


def save_output(text):
    output.write(text+'\n') #Writes 'text' to the output file 
    print(text) #prints 'text' to the command line

def create_category(categoryName, rowsxcolumns):
    if not category_dict.get(str(categoryName)): #checks if a category named categoryName exists. continues if it does not exist
        if (categoryName.split('-')[1][0]=='1' or categoryName.split('-')[1][0]=='2'): #checks if syntax like category-1X or category-2X. continues if syntax correct. 
            rows, columns = [int(number) for number in rowsxcolumns.split('x')] #splits rowsxcolumns to int rows and int columns relative to 'x'
            if not rows>26: #because we have 26 letters in the alphabet
                uppercase_characters = string.ascii_uppercase[:rows] #takes all uppercase characters until last row. 'ABCDEF..'
                str_categoryName = str(categoryName) 
                temp_categoryName={} #creates temporary dictionary for holding seats and seat values.

                for letter in uppercase_characters: #letter starts with and continues until end of the row A, B, C ... 
                    for number in range(columns): #number starts from 0 until end of the column
                        key = f"{letter}{number}" #e.g. A0
                        value = "X" 
                        temp_categoryName.update({key: value}) #adds e.g. A0: "X" to the temporary dictionary 
                #temp dict looks like A0: "X", A1: "X", B0: "X", B1: "X"
                category_dict.update({str_categoryName: temp_categoryName}) #e.g. category-1B: A0: "X", A1: "X", B0: "X", B1: "X" is added to category_dict
                total_balance_dict.update({str_categoryName: {'student': 0, 'full': 0, 'season': 0}}) 
                save_output("The category '{}' having {} seats has been created".format(str_categoryName, rows*columns))
        else:
            save_output("Warning: Category name syntax should be like 'category-1X' or 'category-2X'. X can be replaced by other letters. (example: category-2A)")
    else:
        save_output(f"Warning: Cannot create the category for the second time.\
 The stadium has already {categoryName}")


def rangedSeats_checker(categoryName, seat): #if input has ranged seats like 'C2-5'. this code checks if all seats are empty. If all are empty returns True, even one of them is occupied returns False. 
    nondashed_seats = dashedSeat_to_normalSeats(seat)
    for nondashed_seat in nondashed_seats:
        if category_dict[categoryName][nondashed_seat]!='X':   
            return False
    else:
       return True

def range_check(categoryName, initial_seat): #checks ranges of columns and rows

    last_letter = list(category_dict[categoryName].keys())[-1][0] #takes the last element of category_dict and takes its first character. For ex: last element:Z3 -> Z 
    last_number = int(list(category_dict[categoryName].keys())[-1][1:]) #takes the last element of category_dict and takes all number values except first character and turns it into a integer. For ex: last element:Z24 -> 24 
    uppercase_characters = string.ascii_uppercase
    last_letters_index = uppercase_characters.find(last_letter) #takes last_letter's index
    
    if '-' in initial_seat:       
        seperated_seats = dashedSeat_to_normalSeats(initial_seat) 
        
        for seat in seperated_seats:
            if not last_letters_index >= uppercase_characters.find(seat[0]) and not last_number>=int(seat[1:]): #.find() finds index of seats letter e.g. B(1),E(4).
                save_output(f"Error: The category '{categoryName}' has less row and column than the specified index {initial_seat}!")
                return False
            
            elif not last_letters_index >= uppercase_characters.find(seat[0]):
                save_output(f"Error: The category '{categoryName}' has less row than the specified index {initial_seat}!")
                return False

            elif not last_number>=int(seat[1:]):
                save_output(f"Error: The category '{categoryName}' has less column than the specified index {initial_seat}!")
                return False

        else:
            return True

    else:

        if not last_letters_index >= uppercase_characters.find(initial_seat[0]) and not last_number>=int(initial_seat[1:]):
            save_output(f"Error: The category '{categoryName}' has less column and row than the specified index {initial_seat}!")
            return False

        elif not last_letters_index >= uppercase_characters.find(initial_seat[0]):
            save_output(f"Error: The category '{categoryName}' has less row than the specified index {initial_seat}!")
            return False

        elif not last_number>=int(initial_seat[1:]):
            save_output(f"Error: The category '{categoryName}' has less column than the specified index {initial_seat}!")
            return False

        else:
            return True



def seller(categoryName, ticketType, seat):
    
    if ticketType=='student':
        category_dict[categoryName][seat]='S' #changes seats value from X to S
        total_balance_dict[categoryName]['student']+=1 #adds 1 to student key of total_balance_dict
    
    elif ticketType=='season': 
        category_dict[categoryName][seat]='T' #changes seats value from X to T
        total_balance_dict[categoryName]['season']+=1 #adds 1 to season key of total_balance_dict

    elif ticketType=='full':
        category_dict[categoryName][seat]='F' #changes seats value from X to F
        total_balance_dict[categoryName]['full']+=1 #adds 1 to full key of total_balance_dict


def dashedSeat_to_normalSeats(seat):
    
    seat_splitted = seat.split("-") #splits C3-5 to C3 5.
    loop_number = int(seat_splitted[-1]) - int(seat_splitted[0][1:]) #for C3-5, loop number is 5-3 = 2
    seats_list = []
    
    for index in range(loop_number+1): #for C3-5, index will be 0, 1, 2
        letter = seat_splitted[0][0] #for C3-5, letter = C
        number = int(seat_splitted[0][1:]) #for C3-5, number = 3
        seats_list.append(letter + (str(number+index))) #'C' + 3+index 

    return seats_list #returns ['C3', 'C4', 'C5']


def sell_ticket(customerName, ticketType, categoryName, *seats):
    list_seats = list(*seats) #puts all *seats values into a list 
    for seat in list_seats: 
        if range_check(categoryName, seat): #checks if seat exceeds the range of category
            if '-' in seat: #checks if seat has '-'. For example. C2-10 returns True 
                if rangedSeats_checker(categoryName, seat): #calls rangedSeats_checker function, which checks for all the seats. Returns True if all seats empty, else False
                    nondashedSeats = dashedSeat_to_normalSeats(seat) #turns C1-14 to C1 C2 C3.. C14 and puts in nondashedSeats list.
                    for nondashedSeat in nondashedSeats: 
                        seller(categoryName, ticketType, nondashedSeat) #sells ticket               
                    save_output(f"Success: {customerName} has bought {seat} at {categoryName}") #prints output
                
                else:
                    save_output(f"Warning: The seats {seat} cannot be sold to {customerName} due some of them have already been sold")
            else: #single seat. For example: C3, A3, B5
                if category_dict[categoryName][seat]=='X': #check if seat is empty
                    seller(categoryName, ticketType, seat) #sells empty seat
                    save_output(f"Success: {customerName} has bought {seat} at {categoryName}") #prints output
                else:
                    save_output(f"Warning: The seat {seat} cannot be sold to {customerName} since it was already sold") #prints output


def cancel_ticket(categoryName, *seats):
    seats = list(*seats)
    for seat in seats:
        if range_check(categoryName, seat): #checks if seat exceeds the range of category
            if category_dict[categoryName][seat]=='X':
                save_output(f"Error: The seat {seat} at {categoryName} has already been free! Nothing to cancel")
            
            else:
                ticketType = category_dict[categoryName][seat] #gets current ticket type of the seat. S, T, or F
                
                if ticketType=='S':
                    total_balance_dict[categoryName]['student'] -= 1 
                    
                elif ticketType=='F':    
                    total_balance_dict[categoryName]['full'] -= 1
                
                elif ticketType=='T':
                    total_balance_dict[categoryName]['season'] -= 1
                
                category_dict[categoryName][seat]='X'

                save_output(f"Success: The seat {seat} at '{categoryName}' has been canceled and now ready to sell again")


def balance(categoryName):
    
    student_ticket_count = total_balance_dict[categoryName]['student'] #gets category's current number of student ticket counts 
    full_ticket_count = total_balance_dict[categoryName]['full']  #gets category's current number of full ticket counts 
    season_ticket_count = total_balance_dict[categoryName]['season']  #gets category's current number of season ticket counts 
    
    revenue = student_ticket_count*10 + full_ticket_count*20+ season_ticket_count*250
    
    save_output(f"category report of '{categoryName}'"+ "\n"+ \
'--------------------------------' + "\n" +
f'Sum of students = {student_ticket_count}, Sum of full pay = {full_ticket_count}, Sum of season ticket = {season_ticket_count}, \
and Revenues = {revenue} Dollars')


def show_category(categoryName):
    save_output(f"Printing category layout of {categoryName}\n")
    last_letter = list(category_dict[categoryName].keys())[-1][0] #if last seat B4 gets its letter for example B
    last_number = int(list(category_dict[categoryName].keys())[-1][1:]) #if last seat B4 gets its number for example 4
    uppercase_characters = string.ascii_uppercase #all uppercase characters inside a string 'ABCDEFG...'

    for index1 in range(uppercase_characters.find(last_letter),-1,-1): #if last_letter is B, (1,-1,-1) so index can be 1 and 0, if last_letter D index can be 3 2 1 0
        row = uppercase_characters[index1] #if last_letter ist B row = "ABCD.."[1] so it is B
        for index2 in range(last_number+1): #if last_nuber is 4 index2 can be 0 1 2 3 4
            row += ' ' + (category_dict[categoryName][uppercase_characters[index1]+str(index2)])+' ' #gets the value of the seat B + 0, B + 1, B + 2 .. B + 4.
        #at the end of the inner for loop last_letter goes one backward. If i looped for B now it is time for A
        save_output(row)

    row = " "
    for number in range(last_number+1): #prints last row from 0 to last seat number. 0 1 2 3 ...
        if number > 9:
            row += str(number) + ' '
        else:    
            row+=' '+str(number) +' '
    save_output(row)


def main():
    global category_dict, total_balance_dict, input, output
    category_dict, total_balance_dict = {}, {}
    
    output = open_output_file('output.txt')
    input = open_input_file(sys.argv[1])

    for line in input:

        line = line.replace('\n','').split(' ')

        if line[0]=='CREATECATEGORY':
            create_category(line[1],line[2])
        
        elif line[0]=='SELLTICKET':
            if len(line)>=4:
                sell_ticket(line[1],line[2],line[3],line[4:])
            else:
                save_output("ERROR: There aren't enough command line arguments!")
        
        elif line[0]=='CANCELTICKET':
            cancel_ticket(line[1],line[2:])

        elif line[0]=='BALANCE':
            balance(line[1])
        
        elif line[0]=='SHOWCATEGORY':
            show_category(line[1])


if __name__=="__main__":
    main()
#Samed Ökçeci 2210356015
