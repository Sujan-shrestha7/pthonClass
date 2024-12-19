def sub(num1,num2):
    try:
        print(num1/num2)
    except:
        return "error"
    finally:
        return "run first"
        
sub(10,2)
# print(a)