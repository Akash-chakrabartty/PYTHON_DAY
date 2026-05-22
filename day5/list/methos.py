list=[2,1,3]
list.append(4)
print(list)
print(list.append(4))
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)    # 1,2,3,4,4
list.insert(1,100)
print(list)  #[1, 100, 2, 3, 4, 4]

list.remove(100)
print(list)  #[1, 2, 3, 4, 4]

list.pop(3)
print(list)

