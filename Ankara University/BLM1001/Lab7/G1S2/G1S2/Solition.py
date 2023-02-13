#ı,ğ,
turk_chars=[305,287,351,231,246,252,304,286,350,199,214,220]

def count_char_num(str1):
	char_count=0
	num_count=0
	for i in str1:
		if 65<=ord(i)<=90 or 97<=ord(i)<=122 or ord(i) in turk_chars:
			char_count+=1

		elif 48<=ord(i)<=57:
			num_count+=1

	result={"LETTERS":char_count,"DIGITS":num_count}
	return result

input1=input()
ans=count_char_num(input1)
print(ans)




"""
print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))
print(ord("0"))
print(ord("1"))
print(ord("2"))
print(ord("3"))
print(ord("4"))
print(ord("5"))
print(ord("6"))
print(ord("7"))
print(ord("8"))
print(ord("9"))
print(ord("İ"))
print(ord("Ğ"))
print(ord("Ş"))
print(ord("Ç"))
print(ord("Ö"))
print(ord("Ü"))
print(ord("Q"))
"""
