def check_for_line():
    word="like"
    data=True
    line_no=1
    with open("C:\\Users\\KIIT0001\\OneDrive\\Desktop\\60 days\\python\\day8\\practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
        return -1
    
check_for_line()
