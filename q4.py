list=[]
for i in range(5):
    number = int(input("Enter the Number:"))
    list.append(number)
list.sort()
m=[]
i=1

def div(Dividend,Divisor): 
    if(Dividend%Divisor==0):
        return True
    else:
        return False


while i<=list[0]:
    if(div(list[0],i) & div(list[1],i) & div(list[2],i) & div(list[3],i) & div(list[4],i)):
        m.append(i)
    i=i+1
m.sort()
print("The GCD of the entered numbers is : ",m[-1])