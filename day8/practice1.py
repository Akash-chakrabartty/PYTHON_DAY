word="learning"
with open("C:\\Users\\KIIT0001\\OneDrive\\Desktop\\60 days\\python\\day8\\practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")