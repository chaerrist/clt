# import socket
# import sys

# import time

# HOST = '127.0.0.1'
# PORT = 8080

# BUFSIZE = 1024
# ADDR = (HOST,PORT)


# #1 서버에 접속하기 위한 소켓을 생성한다.
# clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #2. 서버에 접속을 시도한다.
# clientSocket.connect(ADDR)
# print('connect is success')

# import socket
# import sys

# import time

# HOST = '127.0.0.1'
# PORT = 8080

# BUFSIZE = 1024
# ADDR = (HOST,PORT)

# clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientSocket.connect(ADDR)

# while True:
#     message = input('client : ')
#     clientSocket.send(message.encode('utf-8'))
#     response = clientSocket.recv(1024)
#     print ('server : ', response.decode('utf-8'))

# clientSocket.close()

# import socket

# HOST = "127.0.0.1"
# PORT = 1234

# ADDR = (HOST, PORT)

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     msg = input("msg : ")

#     sock.sendto(msg.encode('utf-8'), ADDR)
#     rsp, srv = sock.recvfrom(1024)
#     print("msg : ", rsp)

# sock.close()



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