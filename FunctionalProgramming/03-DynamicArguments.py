# Dynamic Arguments
# *args, **kwargs

def add(a,b,*c):
    z = a + b
    #print(c)
    for num in c:
        z += num
    print("Sum is",z)

add(3,6,5,6,5,7,8,4,3)


def student(**details):
    print(details)

student(name = 'ram', age = 20, college = 'HMR')
student(name = 'raman', age = 18, college = 'BPIT', branch = 'CS')
student(name = 'shyam', age = 18, branch = 'IT', cgpa = 8)













