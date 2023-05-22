import random

key = ''

def generate_key():
    global key
    day = random.randrange(1, 366)
    if day < 10:
        day_str = '00' + str(day)
    else:
        day = str(day)
        key = key + day

    year = random.randrange(1995, 2003)
    year_string = str(year)
    year = year_string[2:]
    key = key + year

    key = key + '-OEM-00'


    divisible_by_7 = False

    while not divisible_by_7:
        number = random.randint(10000, 99999)

        if number % 7 == 0:
            divisible_by_7 = True
            key = key + str(number)
        else:
            continue

    random_numbers = random.randrange(10000, 99999)

    key = key + '-' + str(random_numbers)

    print(key)




how_many = input('How many times would you like to attempt to generate a key? ')


done = 0

how_many = int(how_many)

while done != how_many:
    generate_key()
    done = done + 1
    key = ''
