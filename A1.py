from random import choice


while True :
    try:
        while True :
            age=int(input("how old are you?  "))
            if age >0 :
               break
    except ValueError:
        print("that's not a number")
    else:
        break



if age<18 :
    print("you're too young")
elif 18<=age<30 :
        print("hope you have a good wife")
else:
        print("hello grandpa")



name=input("what's your name?")

answer=input("i can make a square with your name do want me make it?").lower().strip()

if answer=="yes" :
    for k in range(3) :
        for j in range(3):
            print(name,end="-")
        print()
else:
    print("ok,as you like")

print("i can make a coin flip")


coin=choice(["ملك","كتابة"])
print(coin)

