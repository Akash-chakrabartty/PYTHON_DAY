student={
    "name":"akash",
    "age": 22,
    "hight":6,
    "country":"bangladesh",
    "town":"khulna",
}

for keys in student.keys():
    print(keys)

for values in student.values():
    print(values)

for key,value in student.items():
    print(f"{key}:{value}")
