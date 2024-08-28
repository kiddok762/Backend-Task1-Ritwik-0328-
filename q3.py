x = int(input('enter total number of integers: '))
l = []
for i in range(x):
    data = int(input('Enter an integer: '))
    if data in l:
        print("Integer already entered.")
    else:
        l.append(data)
print('The given list is = ', l)
target = int(input('Please enter a possible target: '))
# if a+b=c then b=c-a
s = []
while l!=[]:
    a = l.pop()
    b = target-a
    if b in l:
        s.append((a,b))
print('The required combination is ',s)