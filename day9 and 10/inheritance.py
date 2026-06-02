class CityKhulna:
    a="wellcome in our speaceful city"
    def hello(self):
        print("lowest harragement city in Bangladesh")

class CityRajsahi(CityKhulna):
    pass

obj=CityKhulna()
obj2=CityRajsahi()

print(obj.hello())
print(obj2.a)