import random

characters = ["#", "@", "&", "*"]
test = int(input())

case = 0

while test:
    case += 1
    case1 = 0               #for 7 characters
    case2 = 0               # for one uppercase letter
    case3 = 0               # one lowercase
    case4 = 0               # one digit
    case5 = 0               # one character

    pass_length = int(input())
    old_password = input()

    for letter in old_password:
        if letter.isupper():
            case2 += 1
        if letter.islower():
            case3 += 1
        if letter.isdecimal():
            case4 += 1
        if letter in characters:
            case5 += 1

    if case2 == 0:
        old_password += "A"

    if case3 == 0:
        old_password += "a"

    if case4 == 0:
        old_password += "1"

    if case5 == 0:
        old_password += random.choice(characters)

    if pass_length >= 7:
        case1 += 1

    if case1 == 0:
        shortest = 7 - len(old_password)
        for i in range(shortest):
            old_password += random.choice(characters)

    print(f"Case #{case}: {old_password}")
    test -= 1
