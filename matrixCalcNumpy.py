import numpy as np

matrix1 = np.array([[1, 2],
                    [3,4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

print(f"Matrix number 1\n{matrix1}")
print(f"Matrix number 2\n{matrix2}")

while True:
    userChoice = input("What operation do you want to do(*, /, -, +), any other button to end the program: ")
    if userChoice == "*":
        print(matrix1 * matrix2)
        continue
    elif userChoice == "/":
        print(matrix1 / matrix2)
        continue
    elif userChoice == "-":
        print(matrix1 - matrix2)
        continue
    elif userChoice == "+":
        print(matrix1 + matrix2)
        continue
    else:
        print("Program ended")
        break
