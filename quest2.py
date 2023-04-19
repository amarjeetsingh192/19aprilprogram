##rotated the list

##method 1

list=[1,2,3,4,5,6,7,8]

print(list[ : :-1])

##method 2

def rotate_list(lst, n):
    for i in range(n):
        lst.insert(0, lst.pop())
    return lst


list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(list,1)
print(rotated_list)