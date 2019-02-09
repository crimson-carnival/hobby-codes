def steps(number):
    if number <= 1:
        return 0
    elif (number % 2 == 0):
        return 1 + steps(number // 2)
    else:
        return 1 + min(steps(number + 1), steps(number - 1))

n = int(input("Enter the number: "))
print("Minimum steps = " + str(steps(n)))