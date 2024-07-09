# Your task is to make a function that
# can take any non-negative integer as an
# argument and return it with its digits
# in descending order. Essentially, rearrange
# the digits to create the highest possible number.

def descending_order(num):
    if num >= 0:
        number_list = [int(digit) for digit in str(num)]
        for i in range(len(number_list)):
            for j in range(len(number_list)-i - 1):
                if number_list[j] < number_list[j+1]:
                    swap = number_list[j]
                    number_list[j] = number_list[j+1]
                    number_list[j+1] = swap
                    print(number_list)


num = 359
descending_order(num)
