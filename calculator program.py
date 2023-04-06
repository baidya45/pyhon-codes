valid = 1
ans = 0

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

while valid:
    num1 = int(input("Enter the 1st number "))
    num2 = int(input("Enter the 2nd number "))
    choice = int(input("Enter your choice\n1.add\n2.sub\n3.mul\n4.div    "))
    if choice in (1,2,3,4):
        print("your ans is  ",end="")

    if choice == 1:
       ans = add(num1, num2)
       print(ans)
    elif choice == 2:
        ans=sub(num1, num2)
        print(ans)
    elif choice == 3:
        ans=mul(num1, num2)
        print(ans)
    elif choice == 4:
        ans=div(num1, num2)
        print(ans)
    else:
        print("wrong option")
    valid = int(input("do you want to perform again 1 for yes 0 for no   "))



