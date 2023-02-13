

import json


def input_al():
	result_input=""
	while True:
		input1=input()
		if input1=="END":
			break
		result_input+=input1
	return result_input

input1=input_al()
dict_class=json.loads(input1)


def get_results(dict_class):
	names=[]
	for i in dict_class.keys():

		notes=dict_class.get(i)
		note_counter=0
		note_amount=len(notes)
		for j in notes:
			res_notes=j.split("/")
			if res_notes[0]==res_notes[1]:
				note_counter+=1
			
			if note_amount==note_counter:
				names.append(i)
		
			
	return (sorted(names))
	

print(get_results(dict_class))
	



