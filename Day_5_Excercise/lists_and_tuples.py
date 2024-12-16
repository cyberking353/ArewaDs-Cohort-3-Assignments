#1

list_1 = []

#2

list_1 = [1,'salim','ahmad',True,'24','Yobe']

#3

print(len(list_1))

#4

mixed_data_types = ['Salim Bello', 24, 1.70, 'Single', 'Nasarawa']

#5

it_companies = ['Facebook', 'Google','Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7

print(it_companies)

#8

print(len(it_companies))

#9
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

#10

print(it_companies)
it_companies[0] = 'Meta'
print(it_companies)

#11

it_companies.append('OpenAI')

#12 

it_companies.insert(4,'X')

#13

it_companies[0] = it_companies[0].upper()

print(it_companies)

#14

it_companies = it_companies + ["#"]

#15

print('META' in it_companies)

#16

print(it_companies)
it_companies.sort()
print(it_companies)

#17

print(it_companies)

it_companies.reverse()

print(it_companies)

#18

print(it_companies[:3])

#19

print(it_companies[::-1][:3])

#20

middle_it_company = it_companies[4:5]
print(middle_it_company)

#21

print(it_companies)
it_companies.pop(0)

#22

print(it_companies)

del it_companies[3]

print(it_companies)

#23

it_companies.pop()

print(it_companies)

#24

it_companies.clear()

print(it_companies)

#25

del it_companies

#26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

web_tech = front_end + back_end

print(web_tech)

#27

full_stack = web_tech.copy()

full_stack.extend(['Python','SQL'])


#Exercise: Level 2

#1

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(ages)

min_age = min(ages)
max_age = max(ages)

ages.extend([min_age,max_age])

median_ages = (ages[4] + ages[5]) / 2

average_age = sum(ages) / len(ages)

ages_range = max(ages) - min(ages)

print(abs(min(ages)-average_age) == abs(max(ages)-average_age) )


#2

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#a Finding middle countries

middle_countries = []

num_countries = len(countries)

if (num_countries % 2) == 0:
    middle_countries.append(countries[(int(num_countries/2))-1])
    middle_countries.append(countries[(int(num_countries/2))])
else:
    middle_countries = countries[num_countries//2]

print(middle_countries)

#b

first_country_list = []
second_country_list = []

if (num_countries % 2) == 0:
    first_country_list = countries[:(int(num_countries/2))]
    second_country_list = countries[(int(num_countries/2)):]
else:
    first_country_list = countries[:num_countries//2]
    first_country_list.append('New Country')
    second_country_list = countries[num_countries//2:]

print(len(first_country_list))
print(len(second_country_list))

#c

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_country, secound_country, third_country, *scandic = countries

print(first_country)
print(secound_country)
print(third_country)
print(scandic)

## Tuple Exercise

#1

my_tuple = tuple()

#2

my_img_sis = ('Fatima','Khadija','Aisha','Halima')

my_brothers = ('Auwal','Hussaini','Muhammad','Abubakar')

#3
siblings = my_brothers + my_img_sis

#4

print("I have {} siblings".format(len(siblings)))

#5

family_members = siblings + (('Fatima','Sani'),)

##Tuple Exersises 2

#1

*siblings, parents = family_members

print(siblings)
print(parents)

#2

fruits = ('tomato','Orange')

vegies = ('Cabbage','Lettuce')

animal_prod = ('Milk','Meat')

food_stuff_tp = fruits + vegies + animal_prod

#3 

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)

#4

middle_item_list = food_stuff_lt[len(food_stuff_lt)//2]

#5

first_three_item_list = food_stuff_lt[:3]

print(first_three_item_list)

last_three_item_list = food_stuff_lt[::-1][:3]

print(last_three_item_list)

#6

del food_stuff_tp

#7 

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

#Set Exercises

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1

print(len(it_companies))

#2 

it_companies.add('Twitter')

#3

it_companies.update(['X','OpenAI','SapceX'])

print(it_companies)

#4

it_companies.pop()

print(it_companies)

#5

'''
The difference between remove() and discard() is that,

remove() raise an error when a spefied item is not in the set

while discard() does not raise any error when the item does not exist
'''

#Sets Exercises: Level 2

#1

print(A.union(B))

#2

print(A.intersection(B))

#3

print(A.issubset(B))

#4

print(A.isdisjoint(B))
print(B.isdisjoint(A))

#5

print(A.union(B))
print(B.union(A))

#6

print(A.symmetric_difference(B))

#7

del A,B


#Sets Exercises: Level 3

#1

print(ages)

list_c_set = set(ages) 

if len(ages) > len(list_c_set):
    print("Ages List is Bigger")

else:
    print("Ages Set is Bigger")

#2

'''
Strings is a combination of alphanumeric characters, list is a collection of different datatypes stored under 
a single identifier and each item can be retrived using an index, a tuple is just like a list but does not support
change of items (i.e Items in a tuple are immutable) while a set behave just like a list but contains only unique elements

'''

#3

sentence = 'I am a teacher and I love to inspire and teach people'

words = sentence.split(' ')

unique_words = set(words)

print(f'There are {len(unique_words)} in the sentence')