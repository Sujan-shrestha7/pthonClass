##1st day

'''
name= "blablablackShip !!"
age = 19
height = 5.7
is_student = True
in_earth = None

''' 
#example no 2 

'''
print("yeah its working !!😁😁")
print(age)
print("!its  interesting" ,name)
print(type(name))

print("what is your name?")
print(name)

a = input("your age?")

print (float(a))


first_name="sujan "
last_name="shrestha"
full_name= first_name + last_name
print("full_name is", full_name)
print("full_name is ", full_name+" first name is ", first_name+"last name is ",last_name + "and age is",age)
print(f"my name is {first_name } {last_name} and i am {age} years old !!")


now_age = 19
print(f"I am {now_age}years old ! After 5 years i will be{ now_age + 5} years old")
'''

###2nd day

'''

name="sujan shrestha"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.count('a'))
print(name.title())
print(name.index("sujan"))
name_list = print(name.split())  #converts into list

print("--".join(name))
print(name.replace("sujan","susmita"))
string ="       test      "
print(string)
print(string.strip())

filename = "example.cs.py"
filename2="IMg_2"

print(filename.startswith(".py"))
print(filename.endswith("example"))
print(filename.startswith("example"))

list = ["hello its","its","me", 1,2,3,4,5,6,"to","you"]
list.append("suni")
print(list)
print(list[1])
print(list[0].replace("its","susmita"))
list.reverse()
print(list)

num_list=[53,5,6,8,9,9]
print(sum(num_list))
num_list.sort()
print(num_list)

tuple=("bimal",25,"sujan",True)
print(tuple)
print(tuple[3])

name_tuple = ("sujan","shrestha")
first_name,last_name = name_tuple
print(first_name,last_name)

sets = {5,6,3,7,7,5,5,5,7,5,6,7,8}

print(sets)
sets2 = {4,5,6,7,5,3,"hell"}

print(sets | sets2)
print(sets - sets2)
print(sets & sets2)


dictionary = {"name":"sujann", "age": 12,"address":"banepa"}
print(dictionary["name"])
dictionary["job"] = "Programmer"
print(dictionary)
'''

#day 3
'''
student = [
    {"name":"sulav","age":15, "grades":("A","A+","B-")},
    {"name":"labsu","age":17, "grades":("B+","A-","C+")},
    {"name":"sul","age":5, "grades":("D","A+","B-")},
    {"name":"subisu","age":18, "grades":("C","A+","B-")},
    {"name":"sunaina","age":13, "grades":("A","A+","B-")},
]

print(student[0]["name"])



nameValue = "hari"
if nameValue == "aawaj":
    print("hello", nameValue)
    print("sanchai xau?")

elif nameValue == "hari":
    print("koh hos ta? 🙄🙄")
else:
    print("hehe just kidding !!😁😁😁")




nummm = 46

match nummm:
    case 1:
        print("tah 1 hos !! ")
    case 2:
        print("tah 2 hos !! ")
    case 3:
        print("tah 3 hos !! ")
    case 4:
        print("tah 4 hos !! ")
    case 5:
        print("tah 5 hos !! ")
    case _:
        print("vaag number liyerw aija !!")



list = ["sujana","sushila","suamna","sumita","swastika","susmitha"]

for i in list: 
    print(i)
'''


#day4
'''

list = ["sujana","sushila","suamna","sumita","swastika","susmitha"]

for num in range(1,10,3):
    print("*"*num)

for name in list:
    print(name)



while  True:
    name = input("enter your name :")
    if name == "sushila":
        continue
        print("hello world !")
    if name == "hari":
        break
    if name == "harith":
        pass
    else:
        print(f"{name} is not in list")

'''

#day 5

'''def sum(num1, num2):
    return num1+num2



print(sum(20,5))'''
'''
def sub_traction(n1,n2): 
    print("sujan")
    try:
        return n1/n2
    except:
        return "error"
    finally:
        print("run first")
        
        
print(sub_traction(10,2))


# print(sub(10,2))
print("hellooo")
'''


#day 6


class Employee:



class Person(Employee):
    pass