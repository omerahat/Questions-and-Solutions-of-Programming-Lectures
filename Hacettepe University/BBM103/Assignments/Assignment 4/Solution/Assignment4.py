#Samed Ökçeci 2210356015
import string 
import sys


def open_file(fileName,method):
    return open(fileName,method,encoding='UTF-8') #opens a file specified as name and method


def save_output(fileName, text):
    fileName.write(text+'\n') #Writes 'text' to the output file 
    print(text) #prints 'text' to the command line


def create_hiddenBoard(rowsxcolumns='10x10'):
    rows, columns = rowsxcolumns.split('x') #rowsxcolumns 10x10. it seperates into two 10, 10
    rows, columns = int(rows), int(columns) #converts them into integers
    uppercase_characters = string.ascii_uppercase[:rows] #takes uppercase characters until 10th index. ABCDEFGHIJ
    hiddenBoard = dict.fromkeys([str(letter)+str(number) for number in range(1,columns+1) for letter in uppercase_characters],'-') #creates a dictionary with A1: '-', A2: '-' ... J10: '-' .
    hiddenBoard.update({'C': 0, 'B': 0, 'S': 0, 'P': 0, 'D': 0}) #adds this key value pairs to count sunk ships
    return hiddenBoard #returns whole dictionary


def hiddenboard_visualizer(boardName, player_name): #this function simply creates an empty list and appends every hiddenboard line into list. 
    row_list = []                                       
    row_list.append(f"{player_name}'s Hidden Board")  
    uppercase_characters = string.ascii_uppercase[:10]
    row_list.append('  '+' '.join(uppercase_characters))
    
    for number in range(1,10+1): #this for loop takes values of hiddenboard as horizontally and appends to list
        row = f"{number}"
        for letter in uppercase_characters:
            if number<=9:
                row += " " + boardName[str(letter)+str(number)] 
            else:
                row += boardName[str(letter)+str(number)] + ' '
        row_list.append(row)


    row_list.append('')
    row_list.append('Carrier     {}       '.format(boardName['C']*'X '+(1-boardName['C'])*'- ')) #gets sinked ships and multiplies by X, multiplies unsinkable ships by -
    row_list.append('Battleship  {}     '.format(boardName['B']*'X '+(2-boardName['B'])*'- '))
    row_list.append('Destroyer   {}       '.format(boardName['D']*'X '+(1-boardName['D'])*'- '))
    row_list.append('Submarine   {}      '.format(boardName['S']*'X '+(1-boardName['S'])*'- '))
    row_list.append('Patrol Boat {} '.format(boardName['P']*'X '+(4-boardName['P'])*'- '))
    row_list.append('')

    return row_list


def ship_condition_checker(hiddenBoardName,dictName,changed_key): #checks if a ship is sinked or not
    for value in dictName[changed_key].values():
        if value == '-':
            return False
    else:
        hiddenBoardName[changed_key[0]] += 1


def inputShips_to_dict_converter(inputFile, dictName, optionalFile): 
    c_list, s_list, d_list, b1_list, b2_list, p1_list, p2_list, p3_list, p4_list = [], [], [], [], [], [], [], [], []
    y_coordinate = 1

    def coordinate_returner(direction, starting_coordinate,shipName): #it is a function to convert optional files into a dictionary like B1: {C2: '-', C3: '-', C4: '-', C5: '-'}
        uppercase_characters = string.ascii_uppercase[:10]
        coordinates_list = []
        if shipName[0] == 'B':
            if direction == 'right':
                index = uppercase_characters.find(starting_coordinate[0])
                for coordinate in uppercase_characters[index:index+4]:
                    coordinates_list.append(coordinate+starting_coordinate[1:])
            
            elif direction == 'down':
                for number in range(int(starting_coordinate[1:]),int(starting_coordinate[1:])+4):
                    coordinates_list.append(str(starting_coordinate[0])+str(number))
                    
        elif shipName[0] == 'P':
            if direction == 'right':
                index = uppercase_characters.find(starting_coordinate[0])
                for coordinate in uppercase_characters[index:index+2]:
                    coordinates_list.append(coordinate+starting_coordinate[1:])

            elif direction == 'down':
                for number in range(int(starting_coordinate[1:]),int(starting_coordinate[1:])+2):
                    coordinates_list.append(str(starting_coordinate[0])+str(number))

        return coordinates_list


    for line in inputFile.readlines():
        x_coordinate = 1
        for letter in line.replace("\n",''):
            if letter == ';':
                x_coordinate +=1
            else:
                if letter == 'C':
                    c_list.append(string.ascii_uppercase[x_coordinate-1]+str(y_coordinate))
                elif letter == 'D':
                    d_list.append(string.ascii_uppercase[x_coordinate-1]+str(y_coordinate))
                elif letter == 'S':
                    s_list.append(string.ascii_uppercase[x_coordinate-1]+str(y_coordinate)) 
        y_coordinate += 1
   
   
    for line in optionalFile.readlines():
        shipName, move = line.replace('\n','').split(';')[0].split(':')
        direction = line.replace('\n','').split(';')[1]
        starting_coordinate =str(move.split(',')[1])+str(move.split(',')[0])

        if shipName =='B1':
            b1_list = (coordinate_returner(direction, starting_coordinate,shipName))

        elif shipName =='B2':
            b2_list = (coordinate_returner(direction, starting_coordinate,shipName))

        elif shipName =='P1':
            p1_list = (coordinate_returner(direction, starting_coordinate,shipName))

        elif shipName =='P2':
            p2_list = (coordinate_returner(direction, starting_coordinate,shipName))  

        elif shipName =='P3':
            p3_list = (coordinate_returner(direction, starting_coordinate,shipName))  

        elif shipName =='P4':
            p4_list = (coordinate_returner(direction, starting_coordinate,shipName))  
    

    tempDict = {}
    dictName['B1'], dictName['B2'], dictName['P1'], dictName['P2'], dictName['P3'], dictName['P4'] =  tempDict.fromkeys(b1_list,'-'), tempDict.fromkeys(b2_list,'-'), tempDict.fromkeys(p1_list,'-'), tempDict.fromkeys(p2_list,'-'), tempDict.fromkeys(p3_list,'-'), tempDict.fromkeys(p4_list,'-')
    dictName['C'], dictName['D'], dictName['S']=tempDict.fromkeys(c_list,'-'), tempDict.fromkeys(d_list,'-'), tempDict.fromkeys(s_list,'-')
    try:
        assert len(dictName['B1'].keys())==4 and len(dictName['B2'].keys())==4 and \
        len(dictName['P1'].keys())==2 and len(dictName['P2'].keys())==2 and \
        len(dictName['P3'].keys())==2 and len(dictName['P4'].keys())==2 and \
        len(dictName['C'].keys())==5 and  len(dictName['D'].keys())==3 and \
        len(dictName['S'].keys())==3

    except AssertionError:
        save_output(outputFile,'AssertionError: Invalid Operation.')
        exit()


def make_move(move, hiddenBoardName, dictName, movesList): #this function hits the ship in the coordinate which is given. if it hits, it checks if ship is sinked.
    changed_key = None
    for key in dictName.keys():
        if dictName[key].get(move)!=None:
            hiddenBoardName[move] = 'X'
            dictName[key][move] = 'X'
            changed_key = key
            break
    else:
        hiddenBoardName[move] = "O"

    if changed_key!=None: #here it checks if ship is sinked
        ship_condition_checker(hiddenBoardName,dictName,changed_key)


def inputMoves_seperater_and_checker(movesList,dictName):

    move = movesList.pop(0) #it pops the first item which is the current move.
    try:
        error = [] #this is error list. if any error occures it adds error to this list.
        if ',' in move: #checks if current move has ,
            if len(move.split(','))!=2: #checks if current move has different than 2 variables. if it is that means we can't interpret this in our code (error).
                move_count = len(move.split(',')) 
                error.append(f'ValueError: There is/are {move_count} operands in current move!')
                raise ValueError
            else:
                first_part, second_part= move.split(',') #splits current move into two parts by ','
                if first_part.isnumeric() and second_part in string.ascii_uppercase: #checks if first part is numberic(positive integer) and for second part uppercase characters.

                    moveListIndex0 = first_part
                    moveListIndex1 = second_part       
                    assert moveListIndex1 in 'ABCDEFGHIJ' and moveListIndex0 in ['1','2','3','4','5','6','7','8','9','10']
                    
                    real_move = moveListIndex1+moveListIndex0
                    for key in dictName.keys():
                        if dictName[key].get(real_move)!=None:
                            assert dictName[key].get(real_move)=='-' #asserts the coordinate hadn't shot before

                    return real_move, move

                elif first_part == '' and second_part == '': #empty string
                    error.append('IndexError: Both operands are blank strings!')
                    raise IndexError

                elif first_part == '' and second_part.isnumeric(): #empty, number
                    error.append('IndexError: First operand is a blank string second operand is a number!')
                    raise IndexError
                
                elif first_part == '' and second_part in string.ascii_uppercase: #empty, uppercase character
                    error.append('IndexError: First operand is a blank string, second operand is a uppercase letter!')
                    raise IndexError
                
                elif first_part.isnumeric() and second_part =='': #number, empty
                    error.append('IndexError: First operand is a number, second operand is a blank space!')
                    raise IndexError
                
                elif first_part in string.ascii_uppercase and second_part =='': #uppercase character, empty
                    error.append('IndexError: First operand is a uppercase letter, second operand is a blank space!')
                    raise IndexError
                        
                elif first_part in string.ascii_uppercase and second_part.isnumeric(): #uppercase character, number
                    error.append('ValueError: First operand is an uppercase letter, second operand is a number!')
                    raise ValueError

                elif first_part in string.ascii_uppercase and second_part in string.ascii_uppercase: #uppercase character, uppercase character
                    error.append('ValueError: Both first and second operands are uppercase letters!')
                    raise ValueError

                elif first_part.isnumeric() and second_part.isnumeric(): #number, number
                    error.append('ValueError: Both first and second operands are numbers!')
                    raise ValueError
                else:
                    raise Exception
 
        else: #this executes if move has no , that means there is only one character
            if move == '': #if move is empty
                error.append('IndexError: Current move is only a blank space!')
                raise IndexError
            
            elif move in string.ascii_uppercase: #if move is uppercase
                error.append('IndexError: Currennt move is only an uppercase character!')
                raise IndexError

            elif move.isnumeric(): #if move is only number
                error.append('IndexError: Current move is only a number!')
                raise IndexError

            else:
                raise Exception

    except IndexError:
        save_output(outputFile,f'Enter your move: {move}')

        save_output(outputFile,','.join(error))
        return inputMoves_seperater_and_checker(movesList,dictName)

    except ValueError:
        save_output(outputFile,f'Enter your move: {move}')
    
        save_output(outputFile,','.join(error))
        return inputMoves_seperater_and_checker(movesList,dictName)

    except AssertionError:
        save_output(outputFile,f'Enter your move: {move}')
        
        save_output(outputFile,'AssertionError: Invalid Operation.')
        return inputMoves_seperater_and_checker(movesList,dictName)  

    except Exception:
        save_output(outputFile,f'Enter your move: {move}')
        
        save_output(outputFile,'kaBOOM: run for your life!')  
        return inputMoves_seperater_and_checker(movesList, dictName)


def hiddenBoard_finalizer(hiddenBoard,dictName): #this is executed when a player wins.
    dicts_list = "C,D,S,B1,B2,P1,P2,P3,P4".split(',') #it simply takes parts of the ships which haven't shot. updates this parts to current hiddenboard of the winner.
    for i in dicts_list:
        for j in (list(dictName[i].keys())):
            if dictName[i][j]=='-':
                hiddenBoard[j] = str(i[0])


def is_game_finished(dictName): #checks if game end
    for names_of_inner_dicts in dictName.values():
        for dict_values in names_of_inner_dicts.values():
            if dict_values == '-':
                return False
    else:
        return True




def play_round(round,playerName,movesList,p1HiddenBoard,p2HiddenBoard,hiddenBoard,shipsDict): #every round it is executed.
        save_output(outputFile, f"{playerName}'s Move\n")
        save_output(outputFile,f"Round : {round}\t\t\t\t\tGrid Size: 10x10\n")

        p1HiddenBoardList = hiddenboard_visualizer(p1HiddenBoard,'Player1')    #takes current output of players hiddenboards as list
        p2HiddenBoardList = hiddenboard_visualizer(p2HiddenBoard,'Player2')


        
        for index in range(len(p1HiddenBoardList)):
            save_output(outputFile,f"{p1HiddenBoardList[index]}\t\t{p2HiddenBoardList[index]}") #prints their output lists line by line
        


        move_coordinate, move = inputMoves_seperater_and_checker(movesList,shipsDict) #this code checks current move if it has any errors. if not returns move and move_coordinate for example: B1, 1,B

        save_output(outputFile,'Enter your move: {}\n'.format(move)) 
        
        make_move(move_coordinate,hiddenBoard,shipsDict,movesList) #it makes a new move, and updates hiddenboards and dictionaries
        

def main():
    global p1InputFile, p2InputFile, p1ShipsDict, p2ShipsDict,p1HiddenBoard, p2HiddenBoard, outputFile
    outputFile = open_file('Battleship.out','w')

    p1ShipsDict = {}
    p2ShipsDict = {}
    error_list = []

    try: #trys to open a file, it FileNotFoundError happens it adds the file name to error name.
        
        try:
            if sys.argv[1]=='Player1.txt': #checks if Player1.txt exists
                p1InputFile = open_file(sys.argv[1],'r') #Opens file
            else:
                raise FileNotFoundError #if Player1.txt doesnt exist
        except FileNotFoundError:
            error_list.append('Player1.txt')

        try:
            if sys.argv[2]=='Player2.txt': 
                p2InputFile = open_file(sys.argv[2],'r')
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            error_list.append('Player2.txt')

        
        try:
            if sys.argv[3]=='Player1.in':
                p1MovesFile = open_file(sys.argv[3],'r')
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            error_list.append('Player1.in')


        try:
            if sys.argv[4]=='Player2.in':
                p2MovesFile = open_file(sys.argv[4],'r')
            else:
                raise FileNotFoundError
        
        except FileNotFoundError:
            error_list.append('Player2.in')


        try:
            p1OptionalFile = open_file('OptionalPlayer1.txt','r')
        
        except FileNotFoundError:
            error_list.append('OptionalPlayer1.txt')


        try:
            p2OptionalFile = open_file('OptionalPlayer2.txt','r')
        
        except FileNotFoundError:
            error_list.append('OptionalPlayer2.txt')

    except:
        print('kaBOOM: run for your life!')
        exit()

    finally:
        if len(error_list)!=0:
            save_output(outputFile,f"IOError: input file(s) {','.join(error_list)} is/are not reachable.")
            exit()



    p1HiddenBoard = create_hiddenBoard('10x10') #creates an empty 10x10 hiddenboard
    p2HiddenBoard = create_hiddenBoard('10x10') 
    

    inputShips_to_dict_converter(p1InputFile,p1ShipsDict,p1OptionalFile) #turns Player.txt files into dictionary 
    inputShips_to_dict_converter(p2InputFile, p2ShipsDict,p2OptionalFile)

    p1Moves =  p1MovesFile.readlines()[0].replace('\n','').split(';') #turns Player.in files into a list which is seperated by ;
    p2Moves =  p2MovesFile.readlines()[0].replace('\n','').split(';')



    round = 1
    save_output(outputFile, 'Battle of Ships Game\n')
    while True:
        play_round(round,'Player1',p1Moves,p1HiddenBoard,p2HiddenBoard,p2HiddenBoard,p2ShipsDict) #makes move and prints to screen

        play_round(round,'Player2',p2Moves,p1HiddenBoard,p2HiddenBoard,p1HiddenBoard,p1ShipsDict) #makes move and prints to screen

        if is_game_finished(p1ShipsDict) or is_game_finished(p2ShipsDict): #checks both players dictionaries to find out if all ships in one of them or both has been shot.
            
            if is_game_finished(p1ShipsDict) and is_game_finished(p2ShipsDict): #if this is true that means it is DRAW
                hiddenBoard_finalizer(p1HiddenBoard,p1ShipsDict) #finalizes both hiddenboards
                hiddenBoard_finalizer(p2HiddenBoard,p2ShipsDict)
                
                p1HiddenBoardList = hiddenboard_visualizer(p1HiddenBoard,'Player1')    #takes outputs and prints
                p2HiddenBoardList = hiddenboard_visualizer(p2HiddenBoard,'Player2')
                save_output(outputFile,'Draw!\n\nFinal Information\n')
                for index in range(len(p1HiddenBoardList)):
                    save_output(outputFile,f"{p1HiddenBoardList[index]}\t\t{p2HiddenBoardList[index]}")
                break


            elif is_game_finished(p1ShipsDict): #if this is True that means Player2 won

                hiddenBoard_finalizer(p2HiddenBoard,p2ShipsDict) #converts Player2 output board to show remaining boots
                p1HiddenBoardList = hiddenboard_visualizer(p1HiddenBoard,'Player1') #converts hiddenboard to a list
                p2HiddenBoardList = hiddenboard_visualizer(p2HiddenBoard,'Player2') #converts hiddenboard to a list
                save_output(outputFile,'Player2 Wins!\n\nFinal Information\n')
                for index in range(len(p1HiddenBoardList)): #prints hiddenboards next to each other
                    save_output(outputFile,f"{p1HiddenBoardList[index]}\t\t{p2HiddenBoardList[index]}")
                break

                
            elif is_game_finished(p2ShipsDict): #if this is True that means Player1 won

                hiddenBoard_finalizer(p1HiddenBoard,p1ShipsDict) #converts Player1 output board to show remaining boots
                p1HiddenBoardList = hiddenboard_visualizer(p1HiddenBoard,'Player1')    #converts hiddenboard to a list
                p2HiddenBoardList = hiddenboard_visualizer(p2HiddenBoard,'Player2') #converts hiddenboard to a list
                save_output(outputFile,'Player1 Wins!\n\nFinal Information\n')
                for index in range(len(p1HiddenBoardList)):  #prints hiddenboards next to each other
                    save_output(outputFile,f"{p1HiddenBoardList[index]}\t\t{p2HiddenBoardList[index]}")
                break


        round += 1 #round counter for output.


if __name__=='__main__':
    main()
#Samed Ökçeci 2210356015
