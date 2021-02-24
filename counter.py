
#Global counter variable
counter=0
def avg(n1,n2):
    global counter
    counter=counter+1
    return (n1+n2)/2.0

def printHowManyTimesAvgWasCalled():
    print counter

printHowManyTimesAvgWasCalled()

print avg(5,4) # (5+4)/2.0

printHowManyTimesAvgWasCalled()

x=avg(5,4)
print x
printHowManyTimesAvgWasCalled()

def avg2(n1,n2):
    print (n1+n2)/2.0
avg2(5,4)

#n1= float(raw_input('Give number 1: '))
#n2= float(raw_input('Give number 2: '))

#print avg(n2,n1)


# Given n, calculate the sum of 1 to n
n=4
totalSum=0
for i in range(1,n+1): #i = [1,2,3,4] because n=4
    #First iteration (i=1): totalSum=0+1=1
    #Second iteration (i=2): totalSum=1+2=3
    #Third iteration (i=3): totalSum=3+3=6
    #Forth iteration (i=4): totalSum=6+4=10
    totalSum=totalSum+i
print totalSum

# Given n, define a function that calculates the sum of 1 to n

def sum(n):
    totalSum=0
    i=1
    while i<=n:
        totalSum=totalSum+i #0+1; 1+2; 3+3 ...
        i=i+1
    return totalSum

totalSum= sum(4)
print totalSum


#Difference between a function with print and return
def function1():
    print 'Hello'

def printHello(name1):
    return 'Hello ' + name1

function1()
x=printHello('Sandra')
print x

print(printHello('Sandra'))