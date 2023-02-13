e_mail_adress = input("Please enter a e-mail adress")

def character_checker(e_mail_adress):
    at_exists = 0
    dot_exists = 0
    
    for chracter in e_mail_adress:
        if chracter == "@":
            at_exists = 1
        
        elif chracter == '.':
            dot_exists = 1
            
        else:
            pass
    
    if at_exists + dot_exists == 2:
        print('Your e-mail adress is a valid e-mail adress.')
    
    elif at_exists == 1:
        print("Your e-mail adress misses '.'!")
    
    elif dot_exists == 1:
        print("Your e-mail adress misses '@'!")
        
    else:
        print("Your e-mail adress misses '@' and '.'!")
    
character_checker(e_mail_adress)  

