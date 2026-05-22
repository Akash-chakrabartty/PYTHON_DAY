#palindrome or not 
#list1=[1,2,3,2,1]
listed=[]
num1=input("please enter your first num of list:")
num2=input("please enter your 2nd num of list:")
num3=input("please enter your 3rd num of list:")
num4=input("please enter your 4thd num of list:")

listed.append(num1)
listed.append(num2)
listed.append(num3)
listed.append(num4)

print(listed)


list2=listed.copy()
print(listed)
print(list2)

list2.reverse()
print(list2)

if (listed==list2):
    print("the set is palindrome")
else:
    print("thats not a palindrome")

    
    