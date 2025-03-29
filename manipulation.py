#Auto-graded task 2
str_manip= str(input("Enter your a sentence: "))
str_manip_length= len(str_manip)
str_manip_replace= str_manip.replace(str_manip[ -2:-1], "@")
reverse_last3_str_manip= str_manip[-4:-1]
reverse_last3_str_manip= reverse_last3_str_manip[ : :-1]
first_plus_last_letters= (str_manip[0:4]+ str_manip[-3:-1]).replace(" ", "")
print(str_manip) 
print(str_manip_length) 
print(str_manip_replace)
print(reverse_last3_str_manip) 
print(first_plus_last_letters) 