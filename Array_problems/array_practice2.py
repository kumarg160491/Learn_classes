"""


A person saves his monthly saving according to given schema.
He saves same amount of money which is equal to the money saved in immediate previous two months.
Assume, initially he saved 1000 rupees and in first month he saved another 1000. Your task is to tell
how much he had totally saved at the end of ‘n’ months

Input Description:
You will be given a number ‘n’->No. of months

Output Description:
Print the total savings at the end of ‘n’ months

Sample Input :
1

Sample Output :
2000

Algorithm:
initial_month = 1000
first_month = 1000

if initial_month == 0 or first_month == 1:
    return 1000

for i in range(second_month to total):
    total = initial_month + first_month
    initial_month = pre_month
    pre_month = total
return total


"""


def monthly_saving(input_month):
    initial_month = 1000
    first_month = 1000

    if initial_month == 0 or first_month == 1:
        return 1000

    for i in range(2, input_month):
        total = initial_month + first_month
        initial_month = first_month
        first_month = total

    print(total)


monthly_saving(6)
