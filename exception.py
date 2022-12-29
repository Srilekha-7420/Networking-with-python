#string Error
def divide():
    try:
        print(hi)
    except:
        print("exception")
divide()

#Division Error and Value Error

def divide():
    try:
        a=int(input())
        b=a/0
    except ZeroDivisionError:
        print("DividedByZero")
    except ValueError:
        print("ValueError")
divide()
