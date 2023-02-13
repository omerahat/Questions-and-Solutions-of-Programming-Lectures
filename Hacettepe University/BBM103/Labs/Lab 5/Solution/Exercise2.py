list = [1000, 298, 3579, 100, 200, -45, 900]
def nthbiggestnumber(n,list):
    if n>0:
        print(list)
        list.sort()
        print(list)
        list = list[-n:]
        if n!=1:
            print(list)
            list = [list[0]]
        print(list)
        print(list[0])

n = int(input())
nthbiggestnumber(n,list)
