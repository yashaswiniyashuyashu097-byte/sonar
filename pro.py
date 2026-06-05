try:
    # Put the code that might crash here
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result is {result}")
    
except ZeroDivisionError:
    # Runs if the user types 0
    print("Error: You cannot divide by zero!")

except ValueError:
    # Runs if the user types words instead of numbers
    print("Error: Please enter a valid number.")
