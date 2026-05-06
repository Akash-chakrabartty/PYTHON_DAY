base_id="Akash Chakrabartty"
base_password="Akash@123"
id=input("enter your id:")
password=input("enter your password:")
if id==base_id and password==base_password:
    print("log in complete in your account successfully")
elif id==base_id and password!=base_password:
    print("your password is incorrect")
elif id!=base_id and password==base_password:
    print("your id is incorrect")
else:
    print("both your id and password are incorrect")