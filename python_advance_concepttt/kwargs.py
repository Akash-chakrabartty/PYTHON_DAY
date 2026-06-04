def info(**kwargs):
    print("your info is \n")
    for i in kwargs:
        print(f"{i} :{kwargs[i]}")
info(name="AKash",age=23,designation="ai/ml/data scientist")