#                 Exception Handling 
#                     (in Python)
                    
# Types of Erros:
#     1) Compile time error
#     2) Logical Errors
#     3) Run time Errors

# try:
#     # doutable code

# except Exception:
#     # it execute only, if try block have any error

# else:
#     # if try block have no error
    
# finally:
#     # it execute both .....
    
    
  
try:      
    age = int(input("Enter your age : "))

except Exception as e:
    print("errro handel esucessfully..")

else:
    print("user age is : ", age)

finally:
    print("execption handling done....")


print("helo")

print("code done")
    