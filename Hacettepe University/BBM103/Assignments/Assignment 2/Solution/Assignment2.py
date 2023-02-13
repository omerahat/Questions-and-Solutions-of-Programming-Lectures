#Samed Ökçeci 2210356015
def open_input_file():
    return open('doctors_aid_inputs.txt','r').readlines() #returns input_file.readlines()


def open_output_file():
    return open('doctors_aid_outputs.txt','w') #returns output file


def save_output(text):
    output_file.write(text+'\n') #Writes 'text' to output file 


def create(patient):
    if check_index(patient)==None: #Checks if person exists, continues if it does not exist
        patientsList.append(patient) #Adds patient and its values to the patientsList 
        return 'Patient {} is recorded.'.format(patient[0])
    else:
        return 'Patient {} cannot be recorded due to duplication.'.format(patient[0]) 


def remove(patient):
    if check_index(patient)!=None: #Checks if person exists, continues if it exists
        patientsList.pop(check_index(patient)) #First finds index of patient, then removes it from the list
        return 'Patient {} is removed.'.format(patient[0])
    else:
        return 'Patient {} cannot be removed due to absence.'.format(patient[0])


def recommendation(patient):    
    if check_index(patient)!=None: #Checks if person exists, continues if it exists.
        surgery_risk = float(patientsList[check_index(patient)][-1]) #takes last element of the patient into a value of surgery risk
        if probability_calculator(patient)>surgery_risk: #Checks if probability of being ill greater than surgery risk, continues if it is True
            return "System suggests {} to have the treatment.".format(patient[0]) #patient[0] refers to patient name
        else:
            return "System suggests {} NOT to have the treatment.".format(patient[0])
    else:
        return "Recommendation for {} cannot be calculated due to absence.".format(patient[0])


def list():
    if patientsList:
        save_output('''Patient Diagnosis   Disease         Disease     Treatment       Treatment
Name    Accuracy    Name            Incidence   Name            Risk''')
        save_output("-------------------------------------------------------------------------")
        
        for line in patientsList: #Reads patientsList line by line
            values = line[:] #Creates a new list and adds the contents of 'line'

            #multiply values[1] with 100 and converts it into string. converts values[5] into a form like'30%'
            values[1], values[5] = str(float(values[1])*100) ,str(int(float(values[5])*100))+'%' 

            while len(values[1])<5: #loops until values[1] has 4 significant numbers. For example: 98.00, 94.32
                values[1]+='0'
            values[1]+='%' #adds % at the and of the values[1]. For example 98.00%, 94.32%

            save_output("%-7s %-11s %-15s %-11s %-16s%s"%(values[0],values[1],values[2],values[3],values[4],values[5])) #Writes our output to output file


def line_splitter(line): 

    if '\n' in line: #checks if line consists '\n'. if it exists, it removes '\n'
        line = line.replace('\n','')
        
    if len(line.split(' ')) > 2: #if line has more than 2 words, it continues
        command, rest = line.split(' ',1) #splits line into two strings. For example: create - Hypatia, 0.9975, Stomach Cancer, 15/100000, Immunotherapy, 0.04
        line = rest.split(', ') #splits elements of rest into list. For example: ["Hypatia", "0.9975", "Stomach Cancer", "15/100000", "Immunotherapy", "0.04"]
        line.insert(0, command) #inserts first string into our list. In our example create added. Example: ["create", "Hypatia", "0.9975", "Stomach Cancer", "15/100000", "Immunotherapy", "0.04"] 
        
    else:
        line = line.split(' ') 

    return line


def check_index(name):
    if patientsList: #Checks if patientsList empty or not. Continues if it is not empy
        for index in range(len(patientsList)): #This loop uses our patient names as identifier. Returns 'index'(a number) if our name is in the main list
            if patientsList[index][0]==name[0]:
                return index


def probability_percent_converter(probability_value): 
    probability_value *= 100 #Multiplies value by 100. Example: 0.3332323233 33.32323233 
    probability_value= str(probability_value)[:5] #shortens our variable until 4th index. Example: 33.32  
    seperated=probability_value.split('.') #splits by '.'. Example ['33', '32']
    if int(seperated[1])==0:    #checks second element(index=1) equals 0. For example: ["80", "00"]
        return seperated[0] + '%' #adds '%' at the end of first element(index=0). 80% 
    else:
        return probability_value + '%' #adds '%' at the end of whole elements. 33.32%


def probability_calculator(patient):
    patientInfo = patientsList[check_index(patient)] #takes information of patient from patientsList 
    accuracy, ratio = float(patientInfo[1]), patientInfo[3].split('/') #converts patientInfo[1] to float. Splits eg '40/100000' refer to '/' stores output in patientInfo[3] 
    ratio[0], ratio[1] = float(ratio[0]), float(ratio[1]) 
    #calculates probability and returns it.
    nominator = accuracy * ratio[0] 
    denominator = (1-accuracy)*(ratio[1] - nominator)+nominator 
    return nominator/denominator


def probability_checker(patient):
    if check_index(patient)!=None: #Checks if person exists, True if exists
        patientInfos = patientsList[check_index(patient)] #takes patients info from main list 
        probability_percent = probability_percent_converter(probability_calculator(patient)) #calls probability converter function   
        return 'Patient {0} has a probability of {1} of having {2}.'\
        .format(patientInfos[0],probability_percent,patientInfos[2].lower()) 
    else:
        return 'Probability for {} cannot be calculated due to absence.'.format(patient[0])


def main():

    global patientsList, output_file 

    output_file = open_output_file() #returns output file named 'doctors_aid_output'
    fileContent = open_input_file() #returns input_file.readlines()
    
    patientsList = [] #creates main list

    for line in fileContent: 
        splittedLine = line_splitter(line) #calls line_splitter function to split lines into its elements
        command = splittedLine[0] #gets first element of list as command. Example: create, list, remove...

        if command == 'create':
            save_output(create(splittedLine[1:])) #puts values into create function, and writes output to output file

        elif command == 'remove':
            save_output(remove(splittedLine[1:])) #calls remove function and puts values into it, and writes output to output file

        elif command == 'recommendation':
           save_output(recommendation(splittedLine[1:])) #puts values into recommendation function, and writes output to output file

        elif command == 'probability':
            save_output(probability_checker(splittedLine[1:])) #puts values into probabity_checker function, and writes output to output file

        elif command == 'list':
            list() #calls list function
            

if __name__ == "__main__":
    main()

#Samed Ökçeci 2210356015

