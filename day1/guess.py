# Author:Scott She

age_of_scott = 25

# while循环
'''
count = 0
while count < 3:
    guess_age = int(input("age "))

    if guess_age == age_of_scott:
        print("yes, you got it")
        break
    elif guess_age > age_of_scott:
        print("think smaller...")
    else:
        print("think bigger...")

    count += 1
else:
    print("you have tried too many... fuck off")
'''

# for循环
'''
for i in range(3):
    guess_age = int(input("age "))
    if guess_age == age_of_scott:
        print("yes, you got it")
        break
    elif guess_age > age_of_scott:
        print("think smaller...")
    else:
        print("think bigger...")
else:
    print("you have tried too many... fuck off")
'''


# for循环详解
''' 
类似于其他语言中的 
for (int i = 0; i < 10; i+=2) {
    print(i)
}
'''
for i in range(0, 10, 2):
    print(i)


count = 0
while count < 3:
    guess_age = int(input("age "))

    if guess_age == age_of_scott:
        print("yes, you got it")
        break
    elif guess_age > age_of_scott:
        print("think smaller...")
    else:
        print("think bigger...")

    count += 1

    if count == 3:
        print("Do you want to keep guessing... n or N for no, others for yes: ")
        continue_confirm = input()
        if continue_confirm != "n" and continue_confirm != "N":
            count = 0
