def errors():

    while True:
        try:
            x = int(input("Please enter a number: "))
            y = int(input("Please enter a number: "))
            div = x/y
            print("The division is: ", div)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except ZeroDivisionError:
            print("Division by zero is not allowed.")



if __name__=="__main__":
    errors()