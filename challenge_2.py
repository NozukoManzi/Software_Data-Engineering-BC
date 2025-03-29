'''The favorite restuarant cannot be cast as an integer unless it only contains
 numerical values. Hence if this is attempted on a name that contains some non 
 numerical characters an error will occur. Thus the name of the favourite 
 restaurant should be cast as a string. '''

string_fav = int(input("Enter the name of your favourite restuarant: "))
int_fav= int(input("Enter your favourite number: "))
print(string_fav)
print(int_fav)
