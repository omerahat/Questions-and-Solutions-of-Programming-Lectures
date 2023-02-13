#Problem 1: Basketball Score Calculator
import sys  

try:
    #tries converting inputs to integers
    i = abs(int(sys.argv[1])) 
    ii = abs(int(sys.argv[2]))   
    iii= abs(int(sys.argv[3]))
    score = i*2 + ii*3 + iii*1            
    print(score)

except Exception:    
    pass

#Problem 2: Body Mass Index Calculator
def healthStatus(height, mass):
    #Samed Ökçeci 2210356015
    #Checks if height and mass are floats or integers
    if (type(height)==type(1.6) or type(height)==type(1)) and (type(mass)==type(1.8) or type(mass)==type(1)):
        #checks if height and mass are positive numbers
        if height<=0 or mass<=0:
            return 'Please enter positive quantities.'
        else:
            BMI = mass / (height ** 2)
            #if if statement false, the person is underweight
            if BMI >= 18.5:
                #if if statement false, the person is healty
                if BMI >= 24.9:
                    #if if statement false, the person is overweight; if statement is true, the person is obese
                    if BMI >= 30:
                        return "obese"
                    else:
                        return "overweight"
                else:
                    return "healty"
            else:
                return "underweight"
    else:
        return 'Please enter integer or float quantities'
