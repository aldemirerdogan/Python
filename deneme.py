sum = 0.0
num = 0
done = False
while not done:
    height = float(input("Enter a height or 0 to finish: "))
    if height <= 0:
        done = True
    else:
        sum += height
        num += 1

print("Average height is ", sum / num)