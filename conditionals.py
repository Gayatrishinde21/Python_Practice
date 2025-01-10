day_of_week = input("Enter the day of week: ").lower()    #convert lowercase
print(day_of_week)

if day_of_week == "sunday" or day_of_week == "saturday" : #true
    print("I will Practice the Devops")
else:  #false
    print("I will not Practice the Devops")



num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))

choice = input("Enter the operations: (Options: +, -, *, /) ")

if choice == "+":
    sum_of_num = num1 + num2
    print("addition:",sum_of_num,)
elif choice == "-":
    Diff_of_num = num1 - num2
    print("subtraction: ",Diff_of_num)
elif choice == "*":
    Mul_of_num = num1 * num2
    print("Multiflication: ",Mul_of_num)
elif choice == "/":
    div_of_num = num1 / num2
    print("Division: ",div_of_num)
else:
    print("Invalid choice")