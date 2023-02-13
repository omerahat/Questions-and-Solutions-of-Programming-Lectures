import sys
numbers = sys.argv[1].split(',')

stage0 = [] #input list
stage1 = [] #odd numbers list
stage2 = [] #list of numbers that each 3rd number disgarded 
for i in numbers:
    i = int(i)
    stage0.append(i) #appends every number to input list
    if i>=0:
        if i%2!=0: #checks if our number odd. if it is odd, continues
            stage1.append(i) #appends our odd number to odds list
            if i%3!=2: #checks if our number one of every third number. if it is not 3rd number, continues
                stage2.append(i) #appends our non 3rd number to 3rd disgarded list 
                
    lucky_numbers = stage2[:] #defines lucky numbers with disgarded 3rd numbers list
    del lucky_numbers[6::7] #deletes every 7th number from lucky numbers list
print('input->',end="")
print(*stage0, sep=' ')
print('output->')
print(*stage1,'\n', sep=" ")
print(*stage2,'\n', sep=" ")
print(*lucky_numbers, sep=" ")