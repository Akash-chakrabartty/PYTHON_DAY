student={
    "name":"akash",
    "age": 22,
    "hight":6,
    "country":"bangladesh",
    "town":"khulna",
}
print(student)
print(student["name"])    #access name
print(student["age"])

student["age"]="24"
print(student)

student.pop("age")  #remove
print(student)

print(student.keys())
print(student.values())

print(student.items())

print(student.get("name"))
print(student["name"])
print(student.get("hight"))
print(student.get("country"))
print(student.get("town"))
print(student.get("last_name",'not available'))
del student["town"]
print(student)