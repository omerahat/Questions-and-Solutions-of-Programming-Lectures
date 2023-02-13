#Samed Ökçeci 2210356015
import sys
def open_input_output_files(input_file,output_file):
    input_file = open(input_file,'r',encoding='UTF-8') #opens input file
    output_file = open(output_file,'w',encoding='UTF-8') #opens output file
    return input_file, output_file 


def main():
    global message_list
    input_file, output_file = open_input_output_files(sys.argv[1],sys.argv[2]) #calls open_input_output_files function
    message_list = [line.replace('\n','').split('\t') for line in input_file] #deletes \n at the end of the line and splits lines into its tabs and 
    
    for line in message_list: #converts second element to integer 
        line[1]=int(line[1])

    message_list.sort() #sorts the list

    messageCount = 1 #this is the count of message. e.g. Message 1, Message 2
    previousID = None 
    
    for line in message_list: #takes lines in message_list
        if line[0]!=previousID: #Checks if our current ID equals to previousID
            output_file.write(f'Message\t{messageCount}\n') #writes Message 1, Message 2....
            previousID, messageCount = line[0], messageCount+1 #updates previous ID with current one, adds 1 to messageCount

        output_file.write(str(line[0])+'\t'+str(line[1])+'\t'+str(line[2])+'\n') #prints message


if __name__=='__main__':
    main()
#Samed Ökçeci 2210356015
