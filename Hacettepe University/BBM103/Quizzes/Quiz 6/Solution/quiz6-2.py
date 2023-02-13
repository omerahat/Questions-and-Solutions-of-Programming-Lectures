import sys
number = int(sys.argv[1])
top_list = [(number-((i+1)//2))*' ' + (i)*'*' for i in range(1,2*number,2)]
below_list = [(((i+1)//2))*' ' + (2*number-i-2)*'*' for i in range(1,2*number-1,2)]
for line in top_list:
    print(line)
for line in below_list:
    print(line)