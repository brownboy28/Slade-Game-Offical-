import time
def countdown(n) :
    while n > 0:
        print (n)
        n = n - 1
        if n == 0:
            print('Slade got you')
countdown(5)

############################################

count = 0
print("start pressing")
while count < 30:
    input("")
    count = count + 1
    print("number of presses", count)
