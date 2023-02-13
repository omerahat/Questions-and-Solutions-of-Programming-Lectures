def str_to_list_ascii(str1):
	list1=[]
	for i in range(len(str1)):
		list1.append(ord(str1[i]))
	return list1

def deleting(list1,ind1):
	helplist=[]
	for i in range(26):
		if i not in ind1:
			helplist.append(list1[i])
		
		
	return helplist

def game(list1,list2):
	score_a=0
	score_b=0
	for i in range(len(list1)):
		if list1[i]>list2[i]:

			score_a+=(list1[i]-list2[i])
		elif list2[i]>list1[i]:

			score_b+=(list2[i]-list1[i])
	list_score=[score_a,score_b]

	return list_score	




str1=input()

ind1=[]
for i in range(10):
	x=int(input())
	ind1.append(x)
str2=input()

ind2=[]
for i in range(10):
	x=int(input())
	ind2.append(x)

str_list1=str_to_list_ascii(str1)
str_list2=str_to_list_ascii(str2)

del1=deleting(str_list1,ind2)
del2=deleting(str_list2,ind1)


result=game(del1,del2)
print(result)








