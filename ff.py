try:
    num1=int(input("Enter your no."))
    num2=int(input("Enter your no."))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("division by zero is not allowed")
except NameError as ex:
    print("Error in the writing")
except ValueError:
    print("Please write correct value")
except:
    print("error")
finally:
    print("I will continue executing")