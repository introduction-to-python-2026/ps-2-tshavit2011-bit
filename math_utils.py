def find_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

num1 = 1
num2 = 3
num3 = -1
max_num = find_max_number(num1, num2, num3)
print("The maximum number is:", max_num)


  def find_mean(num1, num2, num3):
    mean = (num1 + num2 + num3) / 3
    return mean

num1 = 1
num2 = 3
num3 = 2
mean_value = find_mean(num1, num2, num3)
print("The mean is:", mean_value)

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    std = ((num1 - mean) ** 2 + (num2 - mean) ** 2 + (num3 - mean) ** 2) ** 0.5
    return mean, std
  num1 = 1
num2 = 3
num3 = 2
mean, std = find_mean_std(num1, num2, num3)
print("The mean is", mean)
print("The standard deviation is", std)
