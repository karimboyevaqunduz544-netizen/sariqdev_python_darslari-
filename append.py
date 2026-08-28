# Python append() List Method
a = [1, 2, 3] # a ro'yxatga 1,2,3 qiymat kiritdik
print(a) #a ni chiqar 
#[1, 2, 3]
a.append(4) #append royxat oxiriga element qoshadi
print(a) #ani chiqar
#[1, 2, 3, 4]
print(type(a)) # < class 'list'' >
a.append([5 , 6, 7])
print(a) 
# [1 , 2, 3, 4, [5, 6, 7]]
a.append(" hey ")
print(a)
#[1, 2, 3, 4, [5, 6, 7], ' hey ']
a.append({1:2})
print(a)
# [1, 2, 3, 4, [5, 6, 7], ' hey ' , {1:2}]
a = [1, 2, 3]
print(a)
#[1, 2, 3]
a.append( [i for i in range(5)])
print(a)
#[1, 2, 3,[ 0, 1, 2, 3, 4]]
a.append('hey' + 'python')
print(a)
# [1, 2, 3, [0, 1, 2, 3, 4] , 'heypython']
None
a = [1, 2, 3]
a.append(4)
print(a)
#[1, 2, 3, 4]
a = a.append(4)
print(a) #None
a == None 
print(True) #True
a = None
print(a) #None 
my_list = [100]
my_list.append(100)
print(my_list)
#[100, 100]
