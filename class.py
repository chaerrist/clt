# class Person :
#     name = "Python"
#     age = 23
#     number = "01012341234"
    
#     def getIntroduce(self):
# 	    return f"My name is {self.name}"

    
# p = Person()
# print(p.name)
# print(p.age)
# print(p.number)

# p1 = Person()
# print(p1.name)
# print(p1.age)
# print(p1.number)


# p = Person()
# print(p.number)
# print(p.age)
# print(p.getIntroduce())

class Person :
	count = 0
	
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
		Person.count +=1
  
@classmethod
def getCount(cls):
    return cls.count
  

  
p = Person("hello", 24, "01012345678")
print(p.name)
print(p.getCount())
p1 = Person("World!", 21, "0101231562")
print(p1.name)
print(p1.getCount())
p2 = Person("Python", 20, "010213564")
print(p2.name)
print(p2.getCount())