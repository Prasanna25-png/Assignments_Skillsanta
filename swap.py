list1=[4,17,83,6,8,3,8]
Temp=list1[0],list1[1]
list1[0],list1[1]=list1[-1],list1[-2]
list1[-1],list1[-2]=Temp
print(list1)