#this is my attempt of making a code that will count down from 15 to 0


#while exit_command != "yes":
#    exit_command = input ("Do you really want to exit? (yes/no) ")("lower")
#    counter = 0

counter = 1
while counter <= 10:
    print(counter)
    exit_command = input("do you want to exit?")
    if exit_command != "no":
        continue
    elif exit_command == "yes":
        break
    counter += 1
#     exit_command = input

#while exit_command != "yes":
#        exit_command = input("Do you really want to exit? (yes/no) "),("lower")

