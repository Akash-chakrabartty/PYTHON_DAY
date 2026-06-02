with open("C:\\Users\\KIIT0001\\OneDrive\\Desktop\\60 days\\python\\day8\\practice.txt","r") as f:
    # f.write(" Hi everyone\nWe are learning file I/O\n")
    # f.write("using java\n I like programming in Java.")
    data=f.read()
    print(data)
    new_data=data.replace("java","python")
    print(new_data)

    with open("C:\\Users\\KIIT0001\\OneDrive\\Desktop\\60 days\\python\\day8\\practice.txt","w") as f:
        f.write(new_data)