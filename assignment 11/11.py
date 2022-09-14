'''
#q1
'''
n=int(input("Enter the value of n "))
sum=0
for e in range(1,n+1,1):
    sum+=e
print(sum)
 '''
 #q2
'''
n=int(input("Enter the value of n "))
sum=0
for e in range(1,n+1,1):
    sum+=e*e
print(sum)
'''
#q3
'''
n=int(input("Enter the value of n "))
sum=0
for e in range(1,n+1,1):
    sum+=e*e*e
print(sum)
'''
#q4
'''
n=int(input("Enter the value of n "))
sum=0
for e in range(1,2*n,2):
    sum+=e
print(sum)
'''
#q5
'''
n=int(input("Enter the value of n "))
sum=0
for e in range(2,2*n+1,2):
    sum+=e
print(sum)
'''
#q6
'''
n=int(input("Enter the value of n "))
fact=1
for e in range(n,0,-1):
    fact*=e
print(fact)
'''
#q7
'''
n=int(input("Enter a number "))
count=0
while n!=0:
    count=count+1
    n=n//10
print(count)
'''
#q8
'''
n=int(input("Enter a number "))
sum=0
while n!=0:
    r=n%10
    sum+=r
    n=n//10
print(sum)
'''
#q9
'''
a=[]
n=int(input("Enter a decimal number "))
while n!=0:
    r=n%2
    a.append(r)
    n//=2
a.reverse
for i in a:
    print(i,end=" ")

'''
#q10
'''
a=[]
n=int(input("Enter a decimal number "))
while n!=0:
    r=n%8
    a.append(r)
    n//=8
a.reverse
for i in a:
    print(i,end=" ")
'''