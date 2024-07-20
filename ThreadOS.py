import threading,random

def printAtoZ():
    data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in data:
        print(i)
def printNumber():
    for i in range(24):
        print(i+1)
def printNumberOneToTwenty():
    for i in range(20):
        print(random.choice([0,1,2,3,4,5,6,7,8,9]))

a = threading.Thread(target=printAtoZ)
b = threading.Thread(target=printNumber)
c = threading.Thread(target=printNumberOneToTwenty)

a.start()
b.start()
c.start()

a.join()
b.join()
c.join()
