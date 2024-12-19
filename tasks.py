#  ##task 1
# now_age = 19
# print(f"I am {now_age}years old ! After 5 years i will be{ now_age + 5} years old")


# ##task 2

# varMyname="Sujan Shrestha"
# varNew= varMyname.split()
# print(varNew)
# print("--".join(varNew))

# #task 3

# varWheather  = "I like winter"
# print(varWheather.replace("winter","summer"))


# #task 4

# varSpace= "         whitee       "
# print(varSpace.strip())


# #task 5
# stringNew = "Lets Learn"

# print(stringNew.upper())
# print(stringNew.lower())
# print(stringNew.capitalize())
# print(stringNew.count('a'))
# print(stringNew.title())


# #task 6

# num_list=[53,5,6,8,9,9,8,0,5,3,67,98]
# print(sum(num_list))
# num_list.sort()
# print(num_list[8])

# #task 7
# name = ("sunjala","surpar","sunanda","bhanimsh","bhaharu","babita","bablu","balbbla")
# print(name[0])
# print(name[5])
# print(name[7])


# # task 8

# dictionary1 =[{"name":"rammuu", "age":8, "faculty":"bca"},{"name":"rammishu", "age":48, "faculty":"bmc"}]
# print(dictionary1)
# dictionary1.append({"name":"will smith", "age":17})
# print(dictionary1)

# #task 9
# setsA= {5,6,7,4,6,7,5,3,6}
# setsB={4,7,67,4,36,67,3,56}
# print(setsA | setsB)
# print(setsA & setsB)
# print(setsA - setsB)


# # task 10
 
# numberr= int(input("enter a number:"))
# if numberr>0:
#     print("number is positive")
# elif numberr<0:
#     print("number is negative")
# else:
#     print("number is zero")


# #task 11
# username = input("input username:")
# password = input("input password:")
# if username=="admin":
#     if password=="1234":
#         print("login successfull")
#     else:
#         print("invalid !")
# else:
#         print("invalid !")

# #task 12
# n= int(input("enter a number:"))
# for i in range(1,11):
#     print(i*n)

# #task 13
# fruits = ["apple","banana","cherry","date"]
# for i in fruits:
#     print(i)


# dictionaryBooks = []

# print("Welcome to the Book Management Program!")

# while True:
#     print("Choose an option:")
#     print("1. Add a new book")
#     print("2. Display all books")
#     print("3. Delete a book")
#     print("4. Exit")
    
#     ans = input("What would you like to do? ")

#     match ans:
#         case "1":
#             author = input("Enter author name: ")
#             title = input("Enter book title: ")
#             dictionaryBooks.append({"author": author, "title": title})
#             print(f'Book "{title}" by {author} added successfully!')

#         case "2":
#             if not dictionaryBooks:
#                 print("There is no books bro")
#             else:
#                 print(dictionaryBooks)

#         case "3":
#             Dtitle= input("Enter the title of the book to delete: ")
#             for book in dictionaryBooks:
#                 if book[f"{Dtitle}"] == dictionaryBooks.title:
#                     dictionaryBooks.remove(book)
#                     print(f'Book "{title}" removed successfully!')

#         case "4":
#             print("Exiting the program. Goodbye!")
#             break

#         case _:
#             print("Invalid option. Please choose a valid number.")



# def inputt():
#     x = int(input("enter first number:"))
#     y = int(input("enter second number:"))
#     return x,y

# print("enter 1 for sum")
# print("enter 2 for sub")
# print("enter 3 for div")
# print("enter 4 for mul")
# print("enter 5 for exit")
# c = int(input("what you wanna do?"))


# while True:
#     match c:
#         case 1:
#             a,b = inputt()
#             def sum(a,b):   
#                 print("sum of numbers are:", a+b)
#             sum(a,b)
        
#             c = int(input("what you wanna do?"))
#         case 2:
#             a,b = inputt()
#             def sub(a,b):   
#                 print("sum of numbers are:", a-b)
#             sub(a,b)
#             c = int(input("what you wanna do?"))
#         case 3:
#             a,b = inputt()
#             def div(a,b):
#                 try:
#                     print("divisoin of numbers are:", a/b)
#                 except:
#                     print("error")
#             div(a,b)
#             c = int(input("what you wanna do?"))
#         case 4:
#             a,b = inputt()
#             def mul(a,b):   
#                 print("multiplication of numbers are:", a*b)
#             mul(a,b)
#             c = int(input("what you wanna do?"))

#         case 5:
#             break

#         case _:
#             print("invalid input !!")
#             c = int(input("what you wanna do?"))
            


Employee = []
#  name, designation, salary\

print("enter 1 for add employee !! ")
print("enter 2 for display employee !! ")
print("enter 3 for delete employee !! ")
print("enter 4 for search employee !! ")
print("enter 5 for exit !! ")

d = int(input("Enter your choice : "))

while True:
    match d:
        case 1:
            E_name = input("Enter employee Name:")
            E_designation = input("enetr designation of employee:")
            E_Salary = int(input("Enter salary:"))
            Employee.append({"Name":E_name, "Designation":E_designation,"Salary":E_Salary})
            print("added successfully !!")
            d = int(input("Enter your choice : "))
        case 2:
            print(Employee)
            d = int(input("Enter your choice : "))
        case 3:
            Ename = input("input Name of employee:")
            for i in Employee:
                if i["Name"] == Ename:
                    Employee.remove(i)
            print("Employee deleted Successfully !!")
            d = int(input("Enter your choice : "))
        case 4:
            Sname = input("input Name of employee:")
            for i in Employee:
                if i["Name"] == Sname:
                    print(f"Found Employee: Name: {i['Name']}, Designation: {i['E_designation']}, Salary: {i['E_Salary']}") 
                    d = int(input("Enter your choice : "))
            d = int(input("Enter your choice : "))
        case 5:
            break
        case _:
            print("invalid input !!")


