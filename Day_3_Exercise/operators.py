#1
my_age = 24

#2
my_height = 1.7

#3
complex = 1 + 7j


#4
base = int(input("Enter base: "))
height = int(input("Enter height: "))

print("the area of the triangle is",0.5*base*height)

#5

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
d = int(input("Enter side d: "))

print("The perimeter of the triangle is", a+b+c)

#6

length = float(input("Enter length of triangle: "))
width = float(input("Enter lenght of width: "))

print("The area of the triangle is", length*width)
print("The Perimeter of the Triangle is ", 2 * (length + width))

#7

radius = float(input("Enter a radius of the circle: "))

print("The area of the circle is: ",3.142 * radius * radius)
print("The Circumference of the Circle is: ",2 * 3.14 * radius)

#8

#since y = 2x-2 is in the form y = mx + c

slope_1 = 2

x = 0 # to find y intercept x = 0
y_intercept = 2 * x - 2

y = 0# to find x intercept y = 0
x_intercept = (y + 2) / 2

#9

x1 = 2
y1 = 2

x2 = 6
y2 = 10

slope_2 = (y2 - y1) / (x2 - x1)

# let (p1,p2) and (q1,q2) represent (2,2) and (6,10) 

p1 = 2
p2 = 2 
q1 = 6
q2 = 10

euclidean_dist = ((p1 - q1) ** 2 + (p2 - q2) ** 2) ** 0.5

print("The Euclidean distance between (2,2) and (6,10) is ", euclidean_dist)

#10

print(slope_1 == slope_2)

#11

x_values = list(range(-10,10))

for x_value in x_values:
    print(f"y = {x_value ** 2 + 6 * x_value + 9 } at x = {x_value}")

#12

p_len = len('python')
d_len = len('dragon')

print(p_len == d_len)

#13

print('on' in "python" and "dragon")

#14

sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

#15

print("on" not in "python" and "dragon")

#16

len_py = "python"

len_py = len(len_py)

float_len_py = float(len_py)

str_len_py = str(float_len_py)

print(str_len_py, type(str_len_py))

#17

num = int(input("Enter Number to check"))

even_or_odd = 'odd' if num % 2 == 0 else 'even'

print(f"The num {num} is {even_or_odd}")

#18

print((7//3 == int(2.7)))

#19

print(type(int('10')) == type(10))

#20

print(int(9.8) == 10)

#21

hour = int(input("Enter Hours: "))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is", hour*rate)

#22

years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {(years * 60 * 60 * 24 * 365)}")

#23

for i in range(1,6):
    row = []
    for j in range(5):
        print(i ** j ,end=" ")
    print()

