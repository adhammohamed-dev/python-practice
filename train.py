k=input("what's your name?")
for _ in range(1):
    print("welcome my friend,",k)
x=6
while x<10:
    print("i'm your digital friend,",k)
    x+=5

    
y=int(input("pick a number i will meow for you"))
def meow(y):
    for _ in range(y):
        print("meow")
meow(y)

def square(n):
    return pow(n,2)

n=int(input("what's n?"))
print("n squared is",square(n))


w=int(input("what's w?"))
q=int(input("what's q?"))
if w!=q:
    print("they are not equal and then the multiplcation is",w*q)
else:
    print("they are equal and w*q=",square(w))
print("hahaha \n"*4,end="")
d=int(input("how is your day rate from 10"))
if d>7:
    print("say al hamdullah for having a great day")
elif 4<d<7:
    print("i hope i can help you to make it great")
else:
    print("don't bother your self it will pass fast")
print("see you soon")