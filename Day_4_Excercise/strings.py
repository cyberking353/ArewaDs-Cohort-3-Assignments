# 1
print("Thirty" +" "+"Days"+ " " +"Of"+" "+ "Python")

# 2

print("Coding" +" "+"For"+ " " +"All")

#3

company = "Coding For All"

#4

print(company)

#5

print(len(company))

#6 

print(company.upper())

#7

print(company.lower())

#8

print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[:6])

#10

check = company.find("coding")

if check > 0:
    print("Exist")
else:
    print("Does not Exist")

#11

company = company.replace('Coding','Python')

#12

tem_text = 'Python for Everyone'

company = company.replace('Python for Everyone',company)

#13
print('Coding For All'.split(' '))

#14

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

#15

text = "Coding For All"

print(text[0])

#16

print(len(text) - 1)

#17

print(text[10])

#18

accronym = ''
text = 'Python For Everyone'

word_list = text.split(' ')

for word in word_list:
    accronym += word[0]

print(f'Accronym for "{text}" is {accronym}')

#19 
accronym = ''
text = 'Coding For All'

word_list = text.split(' ')

for word in word_list:
    accronym += word[0]

print(f'Accronym for "{text}" is {accronym}')

#20

print('Coding For All'.index('C'))

#21

print('Coding For All'.index('F'))

#22

print('Coding For All'.rfind('l'))

#23

print("You cannot end a sentence with because because because is a conjunction".find('because'))


#24

print("You cannot end a sentence with because because because is a conjunction".rindex('because'))

#25

text = 'You cannot end a sentence with because because because is a conjunction'

print(text)

print(text[text.find('because'):text.rfind('because')])

#26

print("You cannot end a sentence with because because because is a conjunction".find('because'))

#27

text = 'You cannot end a sentence with because because because is a conjunction'

print(text)

print(text[text.find('because'):text.rfind('because')])

#28

print("Coding For All".startswith('Coding'))

#29

print("Coding For All".endswith('coding'))

#30

text = ' Coding For All  '

stripped_text = text.strip()

print(text)

#31 

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier()) # This Returns True

#32

lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(' # '.join(lib))

#33

print("I am enjoying this challenge.\nI just wonder what is next.")

#34

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35

radius = 10
area = 3.14 * radius ** 2

print("The area of a circle with radius %d is %.2f meters square." % (radius,area) )

#36

print("{} + {} = {}".format(8,6,8+6))
print("{} - {} = {}".format(8,6,8-6))
print("{} * {} = {}".format(8,6,8*6))
print("{} % {} = {}".format(8,6,8/6))
print("{} // {} = {}".format(8,6,8//6))
print("{} ** {} = {}".format(8,6,8**6))




