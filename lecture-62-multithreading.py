#                                 Multithreading in Python 

# Multithreading in Python allows multiple threads (smaller units of a process) to execute concurrently, sharing the same resources, such as memory space. 


# threads : 
# process :



import threading


def car():
    for i in range(1, 100):
        print("yessssssssssss")

def bus():
    for i in range(1, 100):
        print("noooooooo")

# car()
# bus()

th1 = threading.Thread(target = car)
th2 = threading.Thread(target = bus)

th1.start()
th2.start()

print("hllloooo")


print("important code")

print("gpooooooo")

th1.join()
th2.join()

print("donneeee")


# a = 10
# b = 20
# c = a + b

# d = c + 100

# print(d)
