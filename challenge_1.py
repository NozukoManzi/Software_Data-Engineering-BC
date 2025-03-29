import math
len_side_1= float(input("Enter the length of the first side: "))
len_side_2= float(input("Enter the length of the second side: "))
len_side_3= float(input("Enter the length of the third side: "))
lens_list= [len_side_1,len_side_2,len_side_3]
s= sum(lens_list)/2
print(f"Semi-perimeter of the triangle 's' is: {s}")
print(f"Area of the triangle is: {math.sqrt(s*(s-len_side_1)*(s-len_side_2)*(s-len_side_3))}")