def add(a,b):  #Addition Function
    return a+b
def sub(a,b):  #Substract Function
    return a-b
def mul(a,b):  #Multiplication Function
    return a*b
def div(a,b):  #Divition Function
    return a/b
def choice(d,m): #Function for choice between operations
    if d.upper() == 'Y':
        print("\nHere You start ===> \n(press 'q' for quit)\n")
        while True:
            c = input("operator >> ")
            if c == 'q':
                break
            b = float(input("n >> "))
            if c == '+':
                m = add(m,b)
            if c == '-':
                m = sub(m,b)
            if c == '*':
                m = mul(m,b)
            if c == '/':
                m = div(m,b)
            print(">> ",m)
            d = c
    elif d.upper() == 'N':
        print("\nProgram Dead.... (x_x)\n")
    else:
        d = input("\nDO MORE OPERATION WITH THIS RESULT? (Y/N)\n")
        choice(d,m)

while True: #Use a while loop to do calculations
    print("\nCalculator starts..... ;)\n")
    a = float(input("n >> "))
    c = input("operator >> ")
    b = float(input("n >> "))
    if c == '+':
        m = add(a,b)
    if c == '-':
        m = sub(a,b)
    if c == '*':
        m = mul(a,b)
    if c == '/':
        m = div(a,b)
    print(">> ",m)
    d = input("\nDO MORE OPERATION WITH THIS RESULT? (Y/N)\n")
    choice(d,m)

"""# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select your operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do want to do another calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")"""